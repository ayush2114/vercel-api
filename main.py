# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///


from fastapi import FastAPI, Query
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
    students = json.load(file)

@app.get("/")
def read_root():
    return {"message": "Hello, World! from Ayush"}

@app.get("/marks")
def get_marks(names: Optional[List[str]] = Query(None, alias="name")):
    marks = []
    if names is None:
        # If no names provided, return all marks
        marks = [student["marks"] for student in students]
    for student in students:
        if student["name"] in names:
            marks.append(student["marks"])
    return {"marks": marks}