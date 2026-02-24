import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY", "change_me")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@edvanta.kz")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

    SUBSCRIPTION_PRICE = 5000

settings = Settings()