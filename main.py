# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

with open("q-vercel-python.json", "r") as file:
    marks = json.load(file)

@app.get("/")
def read_root():
    return {"message": "Hello, World! from Ayush"}

@app.get("/marks")
def get_marks(names: Optional[List[str]] = None):
    return marks