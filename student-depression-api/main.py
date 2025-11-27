from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
from pathlib import Path
import pandas as pd
from src.model.model import router as model_router
from src.model.questions import router as questions_router

origins = [
        "http://localhost:3000"
    ]

app = FastAPI()

app.include_router(model_router, prefix="/model", tags=["Model"])
app.include_router(questions_router, prefix="/questions", tags=["Questions"])

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


