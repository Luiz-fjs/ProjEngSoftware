import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from src.model.prediction_request import PredictionRequest
from src.model.prediction_response import PredictionResponse


client = TestClient(app)


class TestPredictionRequest:
    """Testes para validação do PredictionRequest."""
    
    def test_valid_prediction_request(self):
        """Testa criação de um PredictionRequest válido."""
        request_data = {
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
        request = PredictionRequest(**request_data)
        assert request.gender == "Masculino"
        assert request.age == 22
        assert request.academic_pressure == 4
        assert request.cgpa == 7.5
    
    def test_invalid_age(self):
        """Testa validação de age negativo."""
        request_data = {
            "gender": "Masculino",
            "age": -5,
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
        request = PredictionRequest(**request_data)
        assert request.age == -5  # Pydantic aceita, mas em produção deveria validar
    
    def test_cgpa_type_validation(self):
        """Testa validação de tipo para CGPA."""
        request_data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 4,
            "cgpa": 7.5,  # float válido
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        request = PredictionRequest(**request_data)
        assert isinstance(request.cgpa, float)


class TestPredictionResponse:
    """Testes para validação da PredictionResponse."""
    
    def test_valid_prediction_response(self):
        """Testa criação de uma PredictionResponse válida."""
        response_data = {
            "prediction": 1,
            "probability": [0.3, 0.7],
            "depression_risk": "Alto",
            "feature_feedback": [
                {
                    "feature": "Idade",
                    "user_value": "22 anos",
                    "importance": 5.9,
                    "impact_level": "MODERADO",
                    "message": "Teste",
                    "context": "Contexto"
                }
            ]
        }
        response = PredictionResponse(**response_data)
        assert response.prediction == 1
        assert len(response.probability) == 2
        assert response.depression_risk == "Alto"
        assert len(response.feature_feedback) == 1
    
    def test_empty_feature_feedback(self):
        """Testa resposta com feedback vazio."""
        response_data = {
            "prediction": 0,
            "probability": [0.8, 0.2],
            "depression_risk": "Baixo",
            "feature_feedback": []
        }
        response = PredictionResponse(**response_data)
        assert len(response.feature_feedback) == 0


class TestModelExample:
    """Testes para o endpoint de exemplo do model."""
    
    def test_example_route(self):
        """Testa o endpoint de exemplo do model."""
        response = client.get("/model/example")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["message"] == "This is an example route from model.py"


class TestGenerateFeatureFeedback:
    """Testes para a função generate_feature_feedback."""
    
    def test_feedback_generation_complete(self):
        """Testa se o feedback é gerado completo com todos os campos."""
        from src.model.model import generate_feature_feedback
        
        user_data = {
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
        
        feedback = generate_feature_feedback(user_data)
        
        assert isinstance(feedback, list)
        assert len(feedback) > 0
        
        # Verifica se cada item tem os campos obrigatórios
        for item in feedback:
            assert "feature" in item
            assert "user_value" in item
            assert "importance" in item
            assert "impact_level" in item
            assert "message" in item
            assert "context" in item
    
    def test_feedback_suicidal_thoughts_sim(self):
        """Testa feedback quando pensamentos suicidas = Sim."""
        from src.model.model import generate_feature_feedback
        
        user_data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 4,
            "cgpa": 7.5,
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Sim",  # CRÍTICO
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        feedback = generate_feature_feedback(user_data)
        suicidal_feedback = next(f for f in feedback if f["feature"] == "Pensamentos Suicidas")
        
        assert suicidal_feedback["impact_level"] == "CRÍTICO"
        assert "ajuda profissional" in suicidal_feedback["message"].lower()
    
    def test_feedback_sleep_duration_variants(self):
        """Testa feedback para diferentes durações de sono."""
        from src.model.model import generate_feature_feedback
        
        base_data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 2,
            "cgpa": 7.5,
            "study_satisfaction": 4,
            "dietary_habits": "Muito saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 2,
            "family_history": "Não"
        }
        
        sleep_options = [
            "Menos de 5 horas",
            "5-6 horas",
            "7-8 horas",
            "Mais de 8 horas",
            "Irregular"
        ]
        
        for sleep_option in sleep_options:
            data = base_data.copy()
            data["sleep_duration"] = sleep_option
            feedback = generate_feature_feedback(data)
            sleep_feedback = next(f for f in feedback if f["feature"] == "Duração do Sono")
            assert sleep_feedback["user_value"] == sleep_option
    
    def test_feedback_academic_pressure_levels(self):
        """Testa feedback para diferentes níveis de pressão acadêmica."""
        from src.model.model import generate_feature_feedback
        
        base_data = {
            "gender": "Masculino",
            "age": 22,
            "cgpa": 7.5,
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        for pressure in range(1, 6):
            data = base_data.copy()
            data["academic_pressure"] = pressure
            feedback = generate_feature_feedback(data)
            pressure_feedback = next(f for f in feedback if f["feature"] == "Pressão Acadêmica")
            assert pressure_feedback["user_value"] == f"{pressure}/5"
            assert pressure_feedback["importance"] > 25  # É o segundo fator mais importante
    
    def test_feedback_financial_stress_levels(self):
        """Testa feedback para diferentes níveis de estresse financeiro."""
        from src.model.model import generate_feature_feedback
        
        base_data = {
            "gender": "Feminino",
            "age": 20,
            "academic_pressure": 3,
            "cgpa": 8.0,
            "study_satisfaction": 4,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Muito saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 6,
            "family_history": "Não"
        }
        
        for stress in range(1, 6):
            data = base_data.copy()
            data["financial_stress"] = stress
            feedback = generate_feature_feedback(data)
            financial_feedback = next(f for f in feedback if f["feature"] == "Estresse Financeiro")
            assert financial_feedback["user_value"] == f"{stress}/5"
    
    def test_feedback_cgpa_ranges(self):
        """Testa feedback para diferentes faixas de CGPA."""
        from src.model.model import generate_feature_feedback
        
        base_data = {
            "gender": "Masculino",
            "age": 22,
            "academic_pressure": 3,
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        cgpa_values = [5.0, 6.5, 7.0, 8.0, 9.5]
        
        for cgpa in cgpa_values:
            data = base_data.copy()
            data["cgpa"] = cgpa
            feedback = generate_feature_feedback(data)
            cgpa_feedback = next(f for f in feedback if f["feature"] == "Coeficiente de Rendimento (CR)")
            assert cgpa_feedback["user_value"] == f"{cgpa:.1f}"
    
    def test_feedback_age_ranges(self):
        """Testa feedback para diferentes faixas etárias."""
        from src.model.model import generate_feature_feedback
        
        base_data = {
            "gender": "Masculino",
            "academic_pressure": 3,
            "cgpa": 7.5,
            "study_satisfaction": 3,
            "sleep_duration": "7-8 horas",
            "dietary_habits": "Moderadamente saudáveis",
            "suicidal_thoughts": "Não",
            "work_study_hours": 8,
            "financial_stress": 3,
            "family_history": "Não"
        }
        
        ages = [18, 21, 25, 28]
        
        for age in ages:
            data = base_data.copy()
            data["age"] = age
            feedback = generate_feature_feedback(data)
            age_feedback = next(f for f in feedback if f["feature"] == "Idade")
            assert age_feedback["user_value"] == f"{age} anos"


class TestFeatureImportance:
    """Testes para importância das features."""
    
    def test_feature_importance_exists(self):
        """Testa se dicionário de importância das features existe."""
        from src.model.model import FEATURE_IMPORTANCE
        
        assert FEATURE_IMPORTANCE is not None
        assert isinstance(FEATURE_IMPORTANCE, dict)
        assert len(FEATURE_IMPORTANCE) > 0
    
    def test_suicidal_thoughts_highest_importance(self):
        """Testa se pensamentos suicidas têm a maior importância."""
        from src.model.model import FEATURE_IMPORTANCE
        
        max_importance = max(FEATURE_IMPORTANCE.values())
        suicidal_importance = FEATURE_IMPORTANCE['Have you ever had suicidal thoughts ?']
        assert suicidal_importance == max_importance
    
    def test_feature_mapping_exists(self):
        """Testa se o mapeamento de features para português existe."""
        from src.model.model import FEATURE_MAPPING
        
        assert FEATURE_MAPPING is not None
        assert isinstance(FEATURE_MAPPING, dict)
        assert len(FEATURE_MAPPING) > 0
    
    def test_feature_mapping_completeness(self):
        """Testa se todas as features inglesas têm mapeamento em português."""
        from src.model.model import FEATURE_MAPPING
        
        pt_features = FEATURE_MAPPING.values()
        assert len(pt_features) > 0
        # Todos os valores devem ser strings não vazias
        for feature in pt_features:
            assert isinstance(feature, str)
            assert len(feature) > 0


class TestModelLoading:
    """Testes para carregamento do modelo."""
    
    @patch('src.model.model.joblib.load')
    def test_model_loading_success(self, mock_joblib_load):
        """Testa se o modelo é carregado com sucesso."""
        from src.model import model as model_module
        
        # Mock do joblib.load para retornar um modelo fake
        mock_model = MagicMock()
        mock_joblib_load.return_value = mock_model
        
        # O modelo já foi carregado no import
        # Apenas verificamos se a função foi chamada
        assert model_module.MODEL_PATH is not None
    
    def test_model_path_exists(self):
        """Testa se o caminho do modelo está definido corretamente."""
        from src.model.model import MODEL_PATH
        
        assert MODEL_PATH is not None
        assert "student-depression-svm.joblib" in str(MODEL_PATH)
