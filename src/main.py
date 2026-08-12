from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from pydantic import ValidationError
import os

from src.routers.chat import router as chat_router
from src.services.resume_extract import extract_resume
from src.services.personal_doc_extract import extract_peersonal_doc
from src.systemprompt.resume_to_json import resume_prompt
from src.services.llm_reponse import extract_resume_content
from src.schema.resume import ResumeUpload
from src.exception.exception import (
    DocumentNotFoundError,
    DocumentParseError,
    LLMResponseError,
    DataNotLoadedError,
    FileNotFoundError
)
from src.exception.handler import (
    document_not_found_handler,
    document_parse_error_handler,
    llm_response_error_handler,
    data_not_loaded_handler,
    validation_error_handler,
    file_not_found_handler
)


@asynccontextmanager
async def load_data(app: FastAPI):
    """Lifespan context manager: extract, parse, validate, and cache resume + personal doc at startup."""
    resume_text = extract_resume()
    resume_json_prompt = resume_prompt(resume_text)
    raw_json = extract_resume_content(resume_json_prompt, resume_text)
    print(raw_json)

    # Parse and validate raw JSON into ResumeUpload Pydantic model
    app.state.resume_json = ResumeUpload.model_validate_json(raw_json)
    app.state.personal_data = extract_peersonal_doc()
    yield

# create FastAPI app with lifespan so data is loaded at startup

app = FastAPI(
    title="Personal AI Assistant",
    description="A FastAPI-based personal AI that answers questions about a person using their resume and personal document.",
    version="1.0.0",
    lifespan=load_data,
)

# Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register custom exception handlers
app.add_exception_handler(DocumentNotFoundError, document_not_found_handler)
app.add_exception_handler(DocumentParseError, document_parse_error_handler)
app.add_exception_handler(LLMResponseError, llm_response_error_handler)
app.add_exception_handler(DataNotLoadedError, data_not_loaded_handler)
app.add_exception_handler(ValidationError, validation_error_handler)
app.add_exception_handler(FileNotFoundError,file_not_found_handler)


# Include routers
app.include_router(chat_router)

# Serve frontend static files
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
if os.path.isdir(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

              
@app.get("/profile.jpg", tags=["ui"])
async def profile_image():
    """Serve profile image directly at /profile.jpg."""
    profile_path = os.path.join(frontend_dir, "profile.jpg")
    if os.path.isfile(profile_path):
        return FileResponse(profile_path)
    return {"error": "Profile image not found"}


@app.get("/", tags=["ui"])
async def root():
    """Serve the ThinkAI frontend UI."""
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.isfile(index_path):
        return FileResponse(index_path)
    return {
        "status": "ok",
        "resume_loaded": bool(getattr(app.state, "resume_json", None)),
        "personal_data_loaded": bool(getattr(app.state, "personal_data", None)),
    }


@app.get("/health", tags=["health"])
async def health():
    """Health check endpoint — reports whether the resume data has been loaded."""
    return {
        "status": "ok",
        "resume_loaded": bool(getattr(app.state, "resume_json", None)),
        "personal_data_loaded": bool(getattr(app.state, "personal_data", None)),
    }
