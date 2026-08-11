from pydantic import BaseModel
from typing import Optional
class Project(BaseModel):
    title:Optional[str]=None
    discription:Optional[str]=None
    technology: list[str] = []
    livedemo:Optional[str]=None
    github_link:Optional[str]=None

class Education(BaseModel):
    degree:Optional[str]=None
    cgpa:Optional[str]=None
    year:Optional[str]=None
class Expireance(BaseModel):
    years:Optional[str]=None
    company:Optional[str]=None
    role:Optional[str]=None
    discription:Optional[str]=None
class Contact(BaseModel):
    email: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None

class ResumeUpload(BaseModel):
    name:Optional[str]=None
    skills:list[str]=[]
    expireance:list[Expireance]=[]
    project:list[Project]=[]
    contact:Optional[Contact]=None
    education:list[Education]=[]




