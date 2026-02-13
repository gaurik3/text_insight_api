from pydantic import BaseModel, Field
from typing import Optional


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text to be processed")


class InsightResponse(BaseModel):
    original_text: str
    processed_insight: str
    word_count: int
    model_used: Optional[str] = None
