from fastapi import APIRouter, Depends
from src.schema.user import Userinput, Chatanswer
from src.schema.resume import ResumeUpload
from src.services.llm_reponse import answser_user_question
from src.core.dependencies import get_resume_json, get_personal_data


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=Chatanswer)
def send_msg(
    msg: Userinput,
    resume_json: ResumeUpload = Depends(get_resume_json),
    personal: str = Depends(get_personal_data),
):
    # Pass resume_json as a JSON string or model to answer_user_question
    resume_str = resume_json.model_dump_json()
    answer = answser_user_question(msg.question, resume_str, personal)
    return {"response": answer}