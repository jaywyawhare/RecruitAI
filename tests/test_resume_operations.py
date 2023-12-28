from src.parser.resume_operations import ResumeAnalyzer
import unittest

class TestResumeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.resume = ResumeAnalyzer("ML.pdf")

    def test_get_headings(self):
        self.assertIsInstance(self.resume.get_headings(), list)

    def get_formatted_output(self):
        self.assertIsInstance(self.resume.get_formatted_output(), list)

if __name__ == "__main__":
    unittest.main()
