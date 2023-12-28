import pdfplumber
import fitz  

class PDFAnalyzer:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def get_text(self) -> str:
        """ 
        Extracts text from a PDF file, preserving spaces using the x_tolerance parameter.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Text from the PDF file.
        """

        with pdfplumber.open(self.pdf_path) as pdf:
            all_text = ''
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=2)
                all_text = all_text + '\n' + text
        return all_text

    def get_links(self) -> list:
        """ 
        Extracts links from a PDF file using the pyMuPDF library.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            list: List of links from the PDF file.
        """
        
        urls = []
        pdf_document = fitz.open(self.pdf_path)
        for page in pdf_document:
            for link in page.get_links():
                urls.append(link['uri'])
        return urls

