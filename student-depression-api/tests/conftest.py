"""
Configuração compartilhada para todos os testes.
"""
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from main import app

# Mock do modelo carregado
@pytest.fixture(scope="session", autouse=True)
def mock_model():
    """Mock do modelo SVM para os testes."""
    with patch('src.model.model.joblib.load') as mock_load:
        mock_model = MagicMock()
        mock_load.return_value = mock_model
        yield mock_model


@pytest.fixture
def client():
    """Fornece um cliente de teste FastAPI."""
    return TestClient(app)


@pytest.fixture
def valid_prediction_data():
    """Fornece dados válidos para predição."""
    return {
        "gender": "Masculino",
        "age": 22,
        "academic_pressure": 4,
        "cgpa": 7.5,
        "study_satisfaction": 3,
        "sleep_duration": "7-8 horas",
        "dietary_habits": "Moderadamente saudáveis",
        "suicidal_thoughts": "Não",
        "work_study_hours": 8,
        "financial_stress": 3,
        "family_history": "Não"
    }


@pytest.fixture
def high_risk_prediction_data():
    """Fornece dados de alto risco para predição."""
    return {
        "gender": "Feminino",
        "age": 20,
        "academic_pressure": 5,
        "cgpa": 5.0,
        "study_satisfaction": 1,
        "sleep_duration": "Menos de 5 horas",
        "dietary_habits": "Muito pouco saudáveis",
        "suicidal_thoughts": "Sim",
        "work_study_hours": 14,
        "financial_stress": 5,
        "family_history": "Sim"
    }


@pytest.fixture
def low_risk_prediction_data():
    """Fornece dados de baixo risco para predição."""
    return {
        "gender": "Masculino",
        "age": 25,
        "academic_pressure": 1,
        "cgpa": 9.0,
        "study_satisfaction": 5,
        "sleep_duration": "7-8 horas",
        "dietary_habits": "Muito saudáveis",
        "suicidal_thoughts": "Não",
        "work_study_hours": 6,
        "financial_stress": 1,
        "family_history": "Não"
    }
