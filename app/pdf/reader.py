from PyPDF2 import PdfReader

from app.definitions import ROOT_DIR


def read_pdf(filename="demo.pdf"):
    filepath = ROOT_DIR / "files" / filename

    reader = PdfReader(filepath)
    page = reader.pages[0]
    return page.extract_text()
