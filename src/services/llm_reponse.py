from fastapi import responses
from fastapi import responses
from fastapi import responses
from fastapi import responses
# pyrefly: ignore [missing-import]
from google import genai
from src.core.config import setting
from src.exception.exception import LLMResponseError
from src.systemprompt.main_system import chat_prompt

client = genai.Client(
    api_key=setting.llm_api_key,
)


def answser_user_question(question: str, resume_json: str, personal_doc: str) -> str:
    """Ask the LLM a question using the combined system prompt built from resume and personal doc.

    Args:
        question: The user's question.
        resume_json: Structured resume data (string or dict).
        personal_doc: Personal document content (string or dict).

    Returns:
        The assistant's text response.

    Raises:
        LLMResponseError: If the LLM call fails or returns an empty response.
    """
    system = chat_prompt(resume_json, personal_doc)

    try:
        response=client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question,
            config={"system_instruction":system}
        )
     
        answer = response.text
        if not answer:
            raise LLMResponseError("Empty response from LLM.")
        return answer
    except LLMResponseError:
        raise
    except Exception as exc:
        raise LLMResponseError(reason=str(exc)) from exc


def extract_resume_content(resume_prompt: str, resume_text: str) -> str:
    """Send the resume text to the LLM and get back a JSON string matching the ResumeUpload schema.

    Args:
        resume_prompt: System prompt that instructs the model to extract structured data.
        resume_text: Raw text extracted from the resume PDF.

    Returns:
        A JSON string conforming to the ResumeUpload schema.

    Raises:
        LLMResponseError: If the LLM call fails or returns an empty response.
    """
    try:
        response=client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=resume_text,
            config={"system_instruction":resume_prompt}
        )
        content = response.text
        if not content:
            raise LLMResponseError("Empty JSON response from LLM during resume extraction.")
        return content
    except LLMResponseError:
        raise
    except Exception as exc:
        raise LLMResponseError(reason=str(exc)) from exc
