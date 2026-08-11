import pymupdf
from pathlib import Path
from fastapi import HTTPException
from src.services.pdfextract import extract_pdf

def extract_resume():
    base_dir=Path(__file__).resolve().parent
    resume_path = base_dir/ ".." / "document" / "aieng_resume.pdf"
    resume_path = resume_path.resolve()
    return extract_pdf(resume_path)
