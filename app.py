import streamlit
from src.resume_parser import ResumeParser

streamlit.title("Recruit.AI")

pdf = streamlit.file_uploader("Upload a PDF file", type=["pdf"])

if pdf:
    with open(pdf.name, "wb") as f:
        f.write(pdf.read())
    path2pdf = pdf.name
    resume_parser = ResumeParser(path2pdf)
    data = resume_parser.get_output()
    streamlit.write(data)
