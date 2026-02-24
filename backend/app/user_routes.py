from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User
from .auth import hash_password, verify_password, create_token
from .subscription_service import has_active_subscription
from .ai_service import generate_lesson_content
from .document_service import save_lesson_doc, save_presentation

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    user = User(
        full_name=data["full_name"],
        birth_date=data["birth_date"],
        email=data["email"],
        password_hash=hash_password(data["password"])
    )
    db.add(user)
    db.commit()
    return {"message": "Регистрация успешна"}

@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=data["email"]).first()
    if not user or not verify_password(data["password"], user.password_hash):
        raise HTTPException(401, "Неверные данные")

    return {"token": create_token(user.id)}

@router.post("/generate")
def generate(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).get(data["user_id"])

    if user.free_generations_used >= 3 and not has_active_subscription(db, user):
        raise HTTPException(403, "Лимит бесплатных генераций исчерпан")

    content = generate_lesson_content(
        data["class_name"],
        data["subject"],
        data["topic"],
        data["lesson_type"],
        data.get("extra_prompt","")
    )

    lesson_path = save_lesson_doc(content)
    ppt_path = save_presentation(content)

    user.free_generations_used += 1
    db.commit()

    return {
        "lesson_doc": lesson_path,
        "presentation": ppt_path
    }