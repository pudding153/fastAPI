import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=[*],
    allow_headers=[*]
)
@app.get("/")
def read_root():
    return{"status":"ok"}
