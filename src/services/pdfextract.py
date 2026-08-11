import pymupdf
from pathlib import Path
from src.exception.exception import DocumentNotFoundError, DocumentParseError


def extract_pdf(file_path: str) -> str:
    """Extract all text from every page of a PDF file.

    Args:
        file_path: Absolute or relative path to the PDF.

    Returns:
        Full text of the document as a single string.

    Raises:
        DocumentNotFoundError: If the file does not exist.
        DocumentParseError: If the file exists but cannot be opened/read.
    """
    path = Path(file_path)
    if not path.exists():
        raise DocumentNotFoundError(path.name)

    try:
        doc = pymupdf.open(str(path))
        pages_text = []
        for page in doc:
            pages_text.append(page.get_text())
        doc.close()
        return "\n".join(pages_text)
    except Exception as exc:
        raise DocumentParseError(path.name, reason=str(exc)) from exc
