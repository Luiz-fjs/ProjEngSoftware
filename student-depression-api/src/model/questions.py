import json
from fastapi import APIRouter, HTTPException
from pathlib import Path

router = APIRouter()


@router.get("")
async def get_questions():
    """Retorna todas as questions do arquivo questions.json"""
    questions_path = Path(__file__).parent.parent / "data" / "questions.json"
    if not questions_path.exists():
        raise HTTPException(status_code=404, detail="Arquivo questions.json não encontrado.")
    try:
        with open(questions_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
        return questions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler questions.json: {str(e)}")
