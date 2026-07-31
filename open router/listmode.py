import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers=headers
)

models = response.json()

for model in models["data"]:
    model_id = model["id"]

    # اطبع الموديلات المجانية فقط
    if ":free" in model_id:
        print(model_id)