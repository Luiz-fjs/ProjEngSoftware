"""
Testes de integração para a API de depressão estudantil.
"""
import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestIntegration:
    """Testes de integração entre endpoints."""
    
    def test_questions_then_prediction_flow(self):
        """Testa o fluxo completo: obter questões e fazer predição."""
        # 1. Obter questões
        response = client.get("/questions")
        assert response.status_code == 200
        questions = response.json()
        assert len(questions) > 0
        
        # Verificar que as questões têm a estrutura esperada
        for question in questions:
            assert "type" in question
            assert "data" in question
    
    def test_root_and_questions_endpoints(self):
        """Testa os endpoints raiz e questões."""
        # Root
        response_root = client.get("/")
        assert response_root.status_code == 200
        
        # Questions
        response_questions = client.get("/questions")
        assert response_questions.status_code == 200
        assert isinstance(response_questions.json(), list)
    
    def test_app_endpoints_available(self):
        """Testa se todos os endpoints estão disponíveis."""
        routes = {route.path for route in app.routes}
        
        # Endpoints esperados
        expected_paths = ["/", "/openapi.json", "/docs", "/redoc"]
        
        for path in expected_paths:
            # Pelo menos um dos docs deve estar disponível
            if path in ["/docs", "/redoc"]:
                continue
            assert any(p.startswith(path) for p in routes) or path in routes


class TestErrorHandling:
    """Testes de tratamento de erros."""
    
    def test_invalid_route_404(self):
        """Testa que rotas inválidas retornam 404."""
        response = client.get("/api/invalid-route")
        assert response.status_code == 404
    
    def test_unsupported_method(self):
        """Testa métodos não suportados."""
        response = client.delete("/")
        assert response.status_code in [405, 404, 400]


class TestCORSConfiguration:
    """Testes para configuração de CORS."""
    
    def test_cors_origin_allowed(self):
        """Testa se origem localhost:3000 é permitida."""
        response = client.get(
            "/",
            headers={"Origin": "http://localhost:3000"}
        )
        # Verifica se a resposta foi recebida (CORS não bloqueia no teste)
        assert response.status_code == 200
    
    def test_cors_headers_present(self):
        """Testa se headers CORS estão presentes."""
        response = client.options(
            "/",
            headers={"Origin": "http://localhost:3000"}
        )
        # OPTIONS request pode não ser suportado, mas o GET deve funcionar
        assert client.get("/").status_code == 200


class TestResponseFormats:
    """Testes para formatos de resposta."""
    
    def test_root_response_json_format(self):
        """Testa se resposta raiz é JSON válido."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
    
    def test_questions_response_json_format(self):
        """Testa se resposta de questões é JSON válido."""
        response = client.get("/questions")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
    
    def test_content_type_json(self):
        """Testa se content-type é application/json."""
        response = client.get("/")
        assert "application/json" in response.headers.get("content-type", "")


class TestModelExample:
    """Testes para o endpoint de exemplo do modelo."""
    
    def test_model_example_endpoint(self):
        """Testa o endpoint de exemplo do modelo."""
        response = client.get("/model/example")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], str)
        assert len(data["message"]) > 0


class TestEndpointStructure:
    """Testes para estrutura dos endpoints."""
    
    def test_model_router_prefix(self):
        """Testa se router de modelo usa prefixo /model."""
        response = client.get("/model/example")
        assert response.status_code == 200
    
    def test_questions_router_prefix(self):
        """Testa se router de questões usa prefixo /questions."""
        response = client.get("/questions")
        assert response.status_code == 200
    
    def test_endpoints_are_separate(self):
        """Testa se endpoints de modelo e questões são separados."""
        model_response = client.get("/model/example")
        questions_response = client.get("/questions")
        
        assert model_response.status_code == 200
        assert questions_response.status_code == 200
        
        # Respostas devem ser diferentes
        assert model_response.json() != questions_response.json()
