Text Insight API

### OVERVIEW
Text Insight API is an internal FastAPI-based service that receives user text input and returns AI-generated processed insights. It includes:

1. REST API endpoints
2. Input validation using Pydantic
3. Async request handling
4. API key authentication
5. Azure OpenAI integration
6. Auto-generated OpenAPI (Swagger) documentation

### ARCHITECTURE OVERVIEW

text_insight_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── auth.py
│   └── azure_client.py
│
├── config.json        (not committed)
├── requirements.txt
├── .gitignore
└── venv/

### SAMPLE CURL REQUESTS

1. Health Check (Public)

curl http://127.0.0.1:8000/health
Output: {
            "status":"ok"
        }

2. Process Text (Protected)

Header: Authorization:  "X-API-Key: gaurikbansal"

curl -X POST "http://127.0.0.1:8000/process-text" \
-H "Content-Type: application/json" \
-H "X-API-Key: gaurikbansal" \
-d "{\"text\": \"Write your query here.\"}"
Output:
{
  "original_text": "Write your query here.",
  "processed_insight": "This will be the response given by the LLM model",
  "word_count": 4,
  "model_used": "Azure OpenAI"
}

3. MetaData (Protected)

curl -H "X-API-Key: gaurikbansal" \
http://127.0.0.1:8000/metadata
Output:
{
  "service_name": "Text Insight API",
  "version": "1.0.0",
  "description": "Internal AI service for processing text insights.",
  "auth_protected": true
}

### HOW TO RUN

Step 1: 
Clone the repository

git clone <repository-url>
cd text_insight_api

Step 2:
Create the virtual environment

python -m venv venv
venv\Scripts\activate

Step 3:
Install dependencies

pip install -r requirements.txt

Step 4:

Create a file named config.json
and enter the following data in it.

{
  "INTERNAL_API_KEY": "apple_sauce",
  "AZURE_OPENAI_API_KEY": "your-azure-key",
  "AZURE_OPENAI_ENDPOINT": "https://your-resource-name.openai.azure.com/",
  "AZURE_OPENAI_DEPLOYMENT": "your-deployment-name"
}

Step 5:
Run your application
python -m uvicorn app.main:app --reload
http://127.0.0.1:8000/docs






