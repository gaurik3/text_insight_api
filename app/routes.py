from fastapi import APIRouter, Security
from app.models import TextRequest, InsightResponse
from app.auth import verify_api_key
from app.azure_client import generate_insight

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/process-text", response_model=InsightResponse)
async def process_text(
    request: TextRequest,
    api_key: str = Security(verify_api_key),
):
    insight = await generate_insight(request.text)

    return InsightResponse(
        original_text=request.text,
        processed_insight=insight,
        word_count=len(request.text.split()),
        model_used="Azure OpenAI"
    )


@router.get("/metadata")
async def metadata(api_key: str = Security(verify_api_key)):
    return {
        "service_name": "Text Insight API",
        "version": "1.0.0",
        "description": "Internal AI service for processing text insights.",
        "auth_protected": True
    }
