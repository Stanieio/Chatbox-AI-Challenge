from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ OPENROUTER --------------
API_KEY = "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"

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "FastAPI running"}

@app.post("/ai")
def chat(request: ChatRequest):

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "HTTP-Referer": "http://localhost",
                "X-Title": "AI Chatbot",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": request.message}
                ]
            }
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        data = response.json()

        if response.status_code != 200:
            return {"reply": f"OpenRouter Error: {data}"}

        reply = data["choices"][0]["message"]["content"]

        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Server Error: {str(e)}"}
