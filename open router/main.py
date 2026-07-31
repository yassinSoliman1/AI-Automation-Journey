import os
import sys
import requests
from dotenv import load_dotenv

# Fix Arabic
sys.stdout.reconfigure(encoding="utf-8")
sys.stdin.reconfigure(encoding="utf-8")

# Load .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Models
models = [
    "google/gemma-4-26b-a4b-it:free",
    "openai/gpt-oss-20b:free",
    "cohere/north-mini-code:free",
    "inclusionai/ling-3.0-flash:free"
]

# Memory
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("=" * 40)
print("         yassin GBT")
print("=" * 40)

while True:

    prompt = input("\nYou: ")

    if prompt.lower() == "exit":
        print("\nGood Bye 👋")
        break

    # حفظ رسالة المستخدم
    messages.append({
        "role": "user",
        "content": prompt
    })

    success = False

    for model in models:

        print(f"\nTrying {model}...")

        data = {
            "model": model,
            "messages": messages
        }

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        result = response.json()

        if "choices" in result:

            ai_reply = result["choices"][0]["message"]["content"]

            print(f"\n✅ Using: {model}")
            print("\nAI:")
            print(ai_reply)

            # حفظ رد الـ AI
            messages.append({
                "role": "assistant",
                "content": ai_reply
            })

            success = True
            break

        else:
            print(f"❌ {model} failed.")

    if not success:
        print("\nNo available model right now. Try again later.")