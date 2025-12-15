from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Question
from schemas import QuestionCreate, QuestionResponse

app = FastAPI()

# Create table
Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL App"}

@app.post("/questions", response_model=QuestionResponse)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):
    new_question = Question(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

@app.get("/questions", response_model=list[QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()
