import os
from fastapi import FastAPI,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List
#key
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=key)
app = FastAPI()
#通信
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def read_root():
    return{"status":"ok"}
class ChatRequest(BaseModel):
    message:str
#py=js
@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    message = request.message
    #API
try:
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=message
    )
    ai_reply = response.text
except Exception as e:
    print(f"error:{e}")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="error"
    )
    return {"reply":ai_reply}
