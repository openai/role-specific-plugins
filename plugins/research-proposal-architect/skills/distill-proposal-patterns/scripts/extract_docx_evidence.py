#!/usr/bin/env python3
import argparse
import hashlib
import json
import struct
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def image_dimensions(blob):
    if blob.startswith(b"\x89PNG\r\n\x1a\n") and len(blob) >= 24:
        return struct.unpack(">II", blob[16:24])
    if blob.startswith(b"\xff\xd8"):
        index = 2
        while index + 9 < len(blob):
            if blob[index] != 0xFF:
                index += 1
                continue
            marker = blob[index + 1]
            index += 2
            if marker in {0xD8, 0xD9}:
                continue
            if index + 2 > len(blob):
                break
            length = struct.unpack(">H", blob[index:index + 2])[0]
            if marker in range(0xC0, 0xC4) and index + 7 < len(blob):
                height, width = struct.unpack(">HH", blob[index + 3:index + 7])
                return width, height
            index += max(length, 2)
    return None, None


def load_relationships(archive):
    path = "word/_rels/document.xml.rels"
    if path not in archive.namelist():
        return {}
    root = ET.fromstring(archive.read(path))
    result = {}
    for rel in root.findall("pr:Relationship", NS):
        result[rel.attrib.get("Id")] = rel.attrib.get("Target")
    return result


def resolve_media_target(target):
    if not target:
        return None
    target_path = PurePosixPath(target)
    if target_path.is_absolute():
        return str(target_path).lstrip("/")
    return str(PurePosixPath("word") / target_path)


def paragraph_text(paragraph):
    return "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()


def extract_evidence(docx_path, start=None, end=None, extract_images=None):
    docx_path = Path(docx_path)
    with zipfile.ZipFile(docx_path) as archive:
        document_root = ET.fromstring(archive.read("word/document.xml"))
        relationships = load_relationships(archive)
        paragraphs = document_root.findall(".//w:body//w:p", NS)
        records = []
        images = {}

        for index, paragraph in enumerate(paragraphs):
            text = paragraph_text(paragraph)
            style_node = paragraph.find("./w:pPr/w:pStyle", NS)
            style = (
                style_node.attrib.get(f"{{{NS['w']}}}val", "")
                if style_node is not None
                else ""
            )
            rel_ids = []
            for blip in paragraph.findall(".//a:blip", NS):
                rel_id = blip.attrib.get(f"{{{NS['r']}}}embed")
                if not rel_id:
                    continue
                rel_ids.append(rel_id)
                target = resolve_media_target(relationships.get(rel_id))
                if not target or target not in archive.namelist():
                    continue
                blob = archive.read(target)
                width, height = image_dimensions(blob)
                images[rel_id] = {
                    "relationship_id": rel_id,
                    "archive_path": target,
                    "filename": PurePosixPath(target).name,
                    "width": width,
                    "height": height,
                    "sha256": hashlib.sha256(blob).hexdigest(),
                }
                if extract_images:
                    output_dir = Path(extract_images)
                    output_dir.mkdir(parents=True, exist_ok=True)
                    (output_dir / PurePosixPath(target).name).write_bytes(blob)

            kind = "caption" if text.startswith(("图", "表")) else "paragraph"
            records.append(
                {
                    "index": index,
                    "style": style,
                    "kind": kind,
                    "text": text,
                    "image_relationship_ids": rel_ids,
                }
            )

    start_index = 0
    if start:
        matches = [record["index"] for record in records if start in record["text"]]
        if not matches:
            raise ValueError(f"start marker not found: {start}")
        start_index = matches[0]

    end_index = len(records)
    if end:
        matches = [
            record["index"]
            for record in records
            if record["index"] > start_index and end in record["text"]
        ]
        if not matches:
            raise ValueError(f"end marker not found after start: {end}")
        end_index = matches[0]

    selected = [
        record for record in records if start_index <= record["index"] < end_index
    ]
    selected_rel_ids = {
        rel_id
        for record in selected
        for rel_id in record["image_relationship_ids"]
    }
    selected_images = [
        images[rel_id] for rel_id in selected_rel_ids if rel_id in images
    ]
    selected_images.sort(key=lambda item: item["filename"])

    return {
        "source_name": docx_path.name,
        "start_marker": start,
        "end_marker": end,
        "paragraph_count": len(selected),
        "paragraphs": selected,
        "images": selected_images,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract DOCX section text and image relationships as JSON."
    )
    parser.add_argument("docx", type=Path)
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--output", default="-")
    parser.add_argument("--extract-images")
    args = parser.parse_args()

    evidence = extract_evidence(
        args.docx,
        start=args.start,
        end=args.end,
        extract_images=args.extract_images,
    )
    payload = json.dumps(evidence, ensure_ascii=False, indent=2)
    if args.output == "-":
        print(payload)
    else:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
