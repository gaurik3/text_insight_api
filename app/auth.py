import json
from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


async def verify_api_key(api_key: str = Security(api_key_header)):
    config = load_config()
    expected_api_key = config.get("INTERNAL_API_KEY")

    if not expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal API key not configured."
        )

    if api_key is None or api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key."
        )

    return api_key
