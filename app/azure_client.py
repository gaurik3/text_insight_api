import json
from openai import AsyncAzureOpenAI


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


async def generate_insight(text: str) -> str:
    config = load_config()

    api_key = config.get("AZURE_OPENAI_API_KEY")
    endpoint = config.get("AZURE_OPENAI_ENDPOINT")
    deployment = config.get("AZURE_OPENAI_DEPLOYMENT")

    if not api_key or not endpoint or not deployment:
        raise RuntimeError("Azure configuration missing in config.json.")

    client = AsyncAzureOpenAI(
        api_key=api_key,
        azure_endpoint=endpoint,
        api_version="2024-12-01-preview"
    )

    response = await client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You extract concise insights from text."},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content
