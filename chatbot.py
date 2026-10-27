
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("AI Chatbot Started!")
print("Type 'exit' to quit.")

previous_response_id = None

while True:
    message = input("\nYou: ").strip()

    if message.lower() == "exit":
        break

    if not message:
        continue

    params = {
        "model": "gpt-4.1-mini",
        "instructions": (
            "You are a helpful customer support "
            "assistant. Never invent company policies."
        ),
        "input": message,
        "store": True,
    }

    if previous_response_id:
        params["previous_response_id"] = (
            previous_response_id
        )

    try:
        response = client.responses.create(**params)
        print("\nBot:", response.output_text)
        previous_response_id = response.id

    except Exception as e:
        print("Error:", e)
