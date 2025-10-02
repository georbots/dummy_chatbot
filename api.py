# fastapi_rasa_wrapper.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI(title="Rasa Chatbot API Demo")

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

class ChatRequest(BaseModel):
    message: str
    sender_id: str = "demo_user"

@app.post("/chat")
def chat(req: ChatRequest):
    payload = {"sender": req.sender_id, "message": req.message}
    response = requests.post(RASA_URL, json=payload).json()
    return {"rasa_response": response}
