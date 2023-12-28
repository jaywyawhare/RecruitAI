from src.parser.pdf_operations import PDFAnalyzer
import unittest
import sys

class TestPDFAnalyzer(unittest.TestCase):
    def setUp(self):
        self.resume = PDFAnalyzer("ML.pdf")

    def test_get_text(self):
        self.assertIsInstance(self.resume.get_text(), str)

    def test_get_links(self):
        self.assertIsInstance(self.resume.get_links(), list)

if __name__ == "__main__":
    unittest.main()



