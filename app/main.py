from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Text Insight API",
    version="1.0.0",
    description="Internal AI service that processes user text and returns insights."
)

app.include_router(router)
