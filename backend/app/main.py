from fastapi import FastAPI
from .database import Base, engine
from .user_routes import router as user_router

app = FastAPI(title="EDVANTA AI")

Base.metadata.create_all(bind=engine)

app.include_router(user_router)