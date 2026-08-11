"""FastAPI dependency functions for injecting app-level state into routes."""

from fastapi import Request, HTTPException
from src.schema.resume import ResumeUpload


def get_resume_json(request: Request) -> ResumeUpload:
    """Dependency that retrieves the validated ResumeUpload model from app state.

    Raises:
        HTTPException 503: If resume data has not been loaded yet.
    """
    data = getattr(request.app.state, "resume_json", None)
    if data is None:
        raise HTTPException(
            status_code=503,
            detail="Server not ready: resume data not loaded.",
        )
    return data


def get_personal_data(request: Request) -> str:
    """Dependency that retrieves the personal document from app state.

    Raises:
        HTTPException 503: If personal data has not been loaded yet.
    """
    data = getattr(request.app.state, "personal_data", None)
    if data is None:
        raise HTTPException(
            status_code=503,
            detail="Server not ready: personal data not loaded.",
        )
    return data
