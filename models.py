from sqlalchemy import Column, Integer, String, Text
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    question_text = Column(Text)
    level = Column(String(20))
    topic = Column(String(50))
