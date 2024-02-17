from parser.resume_operations import ResumeAnalyzer
from parser.pdf_operations import PDFAnalyzer
from parser.presidio_operations import PresidioAnalyzer
from similarity.vectorization_operations import VectorAnalyzer
from similarity.similarity_operations import SimilarityAnalyzer
from typing import Union
import re


class ResumeParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.text = PDFAnalyzer(self.pdf_path).get_text()
        self.text = re.sub(r'[^\x00-\x7F]+', '', self.text)
        self.links = PDFAnalyzer(self.pdf_path).get_links()
        self.name = PresidioAnalyzer(self.text).get_name()
        self.personal_details = PresidioAnalyzer(self.text).get_personal_details()
        self.formatted_output = ResumeAnalyzer(self.text).get_formatted_output()

    output: dict[str, Union[str, list[str]]] = {
        "Name": [],
        "Links": [],
        "Personal Details": [], 
        "Formatted Output": [] 
    }
    

    def get_output(self) -> dict[str, Union[str, list[str]]]:
        """ 
        Formats the resume data into a dictionary of headings and their corresponding data.

        Args:
            text (str): Text from the PDF file.

        Returns:
            dict: Dictionary containing the formatted output.
        """

        self.output: dict[str, Union[str | None, list[str] | str]] = {
            "Name": [], 
            "Links": [],
            "Personal Details": [],  
            "Formatted Output": [],
        }

        self.output["Name"] = self.name if self.name is not None else ""
        self.output["Links"] = self.links
        self.output["Personal Details"] = self.personal_details
        self.output["Formatted Output"] = self.formatted_output

        return self.output