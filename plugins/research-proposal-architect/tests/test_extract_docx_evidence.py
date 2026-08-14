import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "skills"
    / "distill-proposal-patterns"
    / "scripts"
    / "extract_docx_evidence.py"
)
SPEC = importlib.util.spec_from_file_location("extract_docx_evidence", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


DOCUMENT_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
 <w:body>
  <w:p><w:r><w:t>七、研究目标及内容</w:t></w:r></w:p>
  <w:tbl><w:tr><w:tc><w:p><w:r><w:t>表格内研究内容</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
  <w:p>
   <w:r><w:drawing><a:blip r:embed="rId1"/></w:drawing></w:r>
   <w:r><w:t>图1 合成示意图</w:t></w:r>
  </w:p>
  <w:p><w:r><w:t>八、其他章节</w:t></w:r></w:p>
 </w:body>
</w:document>
"""

RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
  Target="media/image1.png"/>
</Relationships>
"""

PNG_1X1 = (
    b"\x89PNG\r\n\x1a\n"
    b"\x00\x00\x00\rIHDR"
    b"\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00"
)


class ExtractDocxEvidenceTests(unittest.TestCase):
    def test_extracts_table_paragraph_and_image_relationship(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", DOCUMENT_XML)
                archive.writestr("word/_rels/document.xml.rels", RELS_XML)
                archive.writestr("word/media/image1.png", PNG_1X1)

            evidence = MODULE.extract_evidence(
                path,
                start="七、研究目标及内容",
                end="八、其他章节",
            )

            texts = [item["text"] for item in evidence["paragraphs"]]
            self.assertIn("表格内研究内容", texts)
            self.assertEqual(evidence["images"][0]["width"], 1)
            self.assertEqual(evidence["images"][0]["height"], 1)

    def test_missing_end_marker_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", DOCUMENT_XML)
                archive.writestr("word/_rels/document.xml.rels", RELS_XML)
                archive.writestr("word/media/image1.png", PNG_1X1)

            with self.assertRaisesRegex(ValueError, "end marker not found"):
                MODULE.extract_evidence(
                    path,
                    start="七、研究目标及内容",
                    end="不存在的章节",
                )


if __name__ == "__main__":
    unittest.main()
