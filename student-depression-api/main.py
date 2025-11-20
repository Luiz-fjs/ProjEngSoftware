from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
from pathlib import Path
import pandas as pd

origins = [
        "http://localhost:3000"
    ]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {}


# Nova rota para retornar o conteúdo de questions.json
@app.get("/questions")
async def get_questions():
    questions_path = Path(__file__).parent / "src" / "data" / "questions.json"
    if not questions_path.exists():
        raise HTTPException(status_code=404, detail="Arquivo questions.json não encontrado.")
    try:
        import json
        with open(questions_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
        return questions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler questions.json: {str(e)}")
