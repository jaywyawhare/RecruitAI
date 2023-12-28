from presidio_analyzer import AnalyzerEngine
import re
from typing import Union


class PresidioAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def get_name(self) -> Union[str, None]:
        """
        Extracts the name from a PDF file using basic logic.

        Args:
            text (str): Text from the PDF file.

        Returns:
            str: Name from the PDF file.
        """

        lines = self.text.split("\n")
        for line in lines:
            if line.strip() != "":
                name = line.title()  
                return name
        
        return None  
            


    def get_personal_details(self) -> dict:
        """ 
        Extracts personal details from a PDF file using the Presidio Analyzer library.

        Args:
            text (str): Text from the PDF file.

        Returns:
            dict[str, list[str]]: Dictionary containing the extracted personal details.
        """

        analyzer = AnalyzerEngine()
        
        personal_details: dict[str, list[str]] = {
            "Name": [],
            "Email": [],
            "Phone": [],
            "Address": [],
        }

        analyzer_results = analyzer.analyze(text=self.text, language='en')

        for result in analyzer_results:
            if result.entity_type == "PERSON":
                personal_details["Name"].append(self.text[result.start:result.end])
            elif result.entity_type == "EMAIL_ADDRESS":
                personal_details["Email"].append(self.text[result.start:result.end])
            elif result.entity_type == "PHONE_NUMBER":
                personal_details["Phone"].append(self.text[result.start:result.end])
            elif result.entity_type == "ADDRESS":
                personal_details["Address"].append(self.text[result.start:result.end])
                

        personal_details["Name"].insert(0, self.get_name() or "")

        for key in personal_details.keys():
            personal_details[key] = list(set(personal_details[key]))
        
        personal_details["Name"] = [name for name in personal_details["Name"] if re.match(r"^[A-Z][a-z]+ [A-Z][a-z]+$", name)]

        return personal_details


