import os
from fastapi import FastAPI,HTTPException,status,Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List
import types
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

#受取  #リクエスト
@app.post("/api/chat")
async def chat_endpoint(req: Request):
    body = await req.json()
    message = body.get("message","")
#会話履歴
    talk = body.get("history", [])
    talk.append({"role":"user","parts":[{"text":message}]})
