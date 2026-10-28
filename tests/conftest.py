import os

os.environ.setdefault("SECRET_KEY", "test-only-key")
os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("CORS_ORIGINS", "http://localhost:3000")
