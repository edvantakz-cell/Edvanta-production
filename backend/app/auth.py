from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(user_id):
    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")