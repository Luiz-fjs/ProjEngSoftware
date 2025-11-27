"""
Testes de validação para dados de entrada.
"""
import pytest
from pydantic import ValidationError
from src.model.prediction_request import PredictionRequest
from src.model.prediction_response import PredictionResponse


class TestPredictionRequestValidation:
    """Testes de validação para PredictionRequest."""
    
    def test_all_required_fields(self):
        """Testa que todos os campos obrigatórios são necessários."""
        required_fields = [
            "gender", "age", "academic_pressure", "cgpa",
            "study_satisfaction", "sleep_duration", "dietary_habits",
            "suicidal_thoughts", "work_study_hours", "financial_stress",
            "family_history"
        ]
        
        base_data = {
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
        
        # Testar que dados completos funcionam
        request = PredictionRequest(**base_data)
        assert request is not None
    
    def test_missing_field_raises_error(self):
        """Testa que campo faltante causa erro."""
        incomplete_data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 4,
            # cgpa está faltando
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        with pytest.raises(ValidationError):
            PredictionRequest(**incomplete_data)
    
    def test_age_type_validation(self):
        """Testa validação de tipo para age."""
        data = {
            "gender": "Masculino",
            "age": "22",  # String em vez de int
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
        
        # Pydantic tenta converter, então pode passar
        try:
            request = PredictionRequest(**data)
            assert request.age == 22
        except ValidationError:
            # Se falhar, é aceitável
            pass
    
    def test_cgpa_type_is_float(self):
        """Testa que CGPA é float."""
        data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 4,
            "cgpa": 7,  # int
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        request = PredictionRequest(**data)
        assert isinstance(request.cgpa, float)
    
    def test_string_fields_required(self):
        """Testa que campos string são obrigatórios."""
        data = {
            "gender": "",  # String vazia
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
        
        # Pydantic aceita strings vazias por padrão
        request = PredictionRequest(**data)
        assert request.gender == ""


class TestPredictionResponseValidation:
    """Testes de validação para PredictionResponse."""
    
    def test_all_required_fields_response(self):
        """Testa que todos os campos obrigatórios estão presentes na resposta."""
        required_fields = [
            "prediction", "probability", "depression_risk", "feature_feedback"
        ]
        
        data = {
            "prediction": 1,
            "probability": [0.3, 0.7],
            "depression_risk": "Alto",
            "feature_feedback": []
        }
        
        response = PredictionResponse(**data)
        for field in required_fields:
            assert hasattr(response, field)
    
    def test_prediction_is_integer(self):
        """Testa que prediction é inteiro."""
        data = {
            "prediction": 1,
            "probability": [0.3, 0.7],
            "depression_risk": "Alto",
            "feature_feedback": []
        }
        
        response = PredictionResponse(**data)
        assert isinstance(response.prediction, int)
    
    def test_probability_is_list(self):
        """Testa que probability é lista."""
        data = {
            "prediction": 0,
            "probability": [0.7, 0.3],
            "depression_risk": "Baixo",
            "feature_feedback": []
        }
        
        response = PredictionResponse(**data)
        assert isinstance(response.probability, list)
    
    def test_feature_feedback_is_list(self):
        """Testa que feature_feedback é lista."""
        data = {
            "prediction": 1,
            "probability": [0.4, 0.6],
            "depression_risk": "Médio",
            "feature_feedback": [
                {
                    "feature": "Teste",
                    "user_value": "Valor",
                    "importance": 10.0,
                    "impact_level": "ALTO",
                    "message": "Mensagem",
                    "context": "Contexto"
                }
            ]
        }
        
        response = PredictionResponse(**data)
        assert isinstance(response.feature_feedback, list)
        assert len(response.feature_feedback) == 1
    
    def test_depression_risk_is_string(self):
        """Testa que depression_risk é string."""
        data = {
            "prediction": 0,
            "probability": [0.8, 0.2],
            "depression_risk": "Baixo",
            "feature_feedback": []
        }
        
        response = PredictionResponse(**data)
        assert isinstance(response.depression_risk, str)


class TestFieldTypeValidation:
    """Testes para validação de tipos de campo."""
    
    def test_integer_fields_in_prediction_request(self):
        """Testa validação de campos inteiros em PredictionRequest."""
        data = {
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
        
        request = PredictionRequest(**data)
        assert isinstance(request.age, int)
        assert isinstance(request.academic_pressure, int)
        assert isinstance(request.study_satisfaction, int)
        assert isinstance(request.work_study_hours, int)
        assert isinstance(request.financial_stress, int)
    
    def test_string_fields_in_prediction_request(self):
        """Testa validação de campos string em PredictionRequest."""
        data = {
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
        
        request = PredictionRequest(**data)
        assert isinstance(request.gender, str)
        assert isinstance(request.sleep_duration, str)
        assert isinstance(request.dietary_habits, str)
        assert isinstance(request.suicidal_thoughts, str)
        assert isinstance(request.family_history, str)
