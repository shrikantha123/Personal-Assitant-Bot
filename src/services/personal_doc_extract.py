import pymupdf
from pathlib import Path
from fastapi import HTTPException
from src.services.pdfextract import extract_pdf
def extract_peersonal_doc():
    base_dir=Path(__file__).resolve().parent
    personal_doc_path = base_dir/ ".." / "document" / "personal-doc.pdf"
    personal_doc_path = personal_doc_path .resolve()
    return extract_pdf(personal_doc_path)