from pydantic import BaseModel

class QuestionCreate(BaseModel):
    title: str
    question_text: str
    level: str
    topic: str

class QuestionResponse(QuestionCreate):
    id: int

    class Config:
        from_attributes = True
