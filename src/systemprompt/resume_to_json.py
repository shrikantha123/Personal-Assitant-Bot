from src.schema.resume import ResumeUpload
def resume_prompt(resume_txt:str):
    return f'''You are a resume information extraction assistant.
Your task is to extract structured information from the
provided resume text.
Use ONLY the information present in the resume.
Do not invent or assume any information.
The required response schema is:{ResumeUpload.model_json_schema()}
Return the extracted resume information according to this strictly as this schema.
Return ONLY the JSON object.
Do not include explanations, markdown, or additional text.'''
