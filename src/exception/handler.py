"""FastAPI exception handlers — register these on the app instance."""

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.exception.exception import (
    DocumentNotFoundError,
    DocumentParseError,
    LLMResponseError,
    DataNotLoadedError,
    FileNotFoundError
)


async def document_not_found_handler(request: Request, exc: DocumentNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "DocumentNotFound",
            "detail": str(exc),
            "document": exc.document_name,
        },
    )


async def document_parse_error_handler(request: Request, exc: DocumentParseError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "DocumentParseError",
            "detail": str(exc),
            "document": exc.document_name,
        },
    )


async def llm_response_error_handler(request: Request, exc: LLMResponseError):
    return JSONResponse(
        status_code=502,
        content={
            "error": "LLMResponseError",
            "detail": str(exc),
        },
    )


async def data_not_loaded_handler(request: Request, exc: DataNotLoadedError):
    return JSONResponse(
        status_code=503,
        content={
            "error": "DataNotLoaded",
            "de   tail": str(exc),
        },
    )


async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "ValidationError",
            "detail": "Failed to validate structured LLM data schema.",
            "errors": exc.errors(),
        },
    )

async def file_not_found_handler(req:Request,exc:FileNotFoundError):
    return JSONResponse(
        status_code=500,
        content={
            "error":"filenotfound",
            "detail":"the file is not found or corrupted",
            "filename":exc.file_name

        }
    )