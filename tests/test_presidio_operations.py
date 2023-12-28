from src.parser.presidio_operations import PresidioAnalyzer
import unittest

class TestPresidioAnalyzer(unittest.TestCase):
    def setUp(self):
        self.resume = PresidioAnalyzer("ML.pdf")

    def test_get_name(self):
        self.assertIsInstance(self.resume.get_name(), str)

    def test_get_personal_details(self):
        self.assertIsInstance(self.resume.get_personal_details(), dict)


if __name__ == "__main__":
    unittest.main()
