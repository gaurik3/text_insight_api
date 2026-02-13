import os
from openai import AsyncAzureOpenAI


async def generate_insight(text: str) -> str:
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not api_key or not endpoint or not deployment:
        raise RuntimeError("Azure OpenAI environment variables are not properly configured.")

    client = AsyncAzureOpenAI(
        api_key=api_key,
        azure_endpoint=endpoint,
        api_version="2024-02-15-preview"
    )

    response = await client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are an AI that extracts concise insights from text."},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content
