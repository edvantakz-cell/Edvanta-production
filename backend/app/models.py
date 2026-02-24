from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    birth_date = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    is_verified = Column(Boolean, default=False)
    free_generations_used = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=False)
    expires_at = Column(DateTime)