from fastapi import FastAPI
from pydantic import BaseModel

from app import askllm

from datetime import datetime

START_TIME = datetime.now()

app = FastAPI(title="Insurance Copilot API")

conversation_memory = []

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def home():
    return {"message": "Insurance API is running"}


@app.get("/health")
def health():

    uptime = datetime.now() - START_TIME

    return {
        "status": "healthy",
        "model": "gpt-4o-mini",
        "uptime": str(uptime)
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    print("CHAT ENDPOINT CALLED")
    print("Message received:", request.message)

    try:

        answer = askllm(request.message)

        return ChatResponse(
            response=answer
        )

    except Exception as e:

        return ChatResponse(
            response=f"Error: {str(e)}"
        )
    
@app.post("/reset")
def reset():

    return {
         "message": "Backend is stateless. No server-side memory to reset."
    } 