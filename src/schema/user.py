from pydantic import BaseModel
from typing import Optional
class Userinput(BaseModel):
    question:str 
class Chatanswer(BaseModel):
    response:str


