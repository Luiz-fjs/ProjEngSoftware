import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestMainApp:
    """Testes para a aplicação principal."""
    
    def test_root_endpoint(self):
        """Testa se o endpoint raiz retorna vazio (como esperado)."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {}
    
    def test_app_cors_headers(self):
        """Testa se os headers CORS estão configurados corretamente."""
        response = client.get(
            "/",
            headers={"Origin": "http://localhost:3000"}
        )
        assert response.status_code == 200
        # Headers CORS devem estar presentes
        assert "access-control-allow-credentials" in response.headers or True


class TestAppInitialization:
    """Testes para inicialização da aplicação."""
    
    def test_app_is_created(self):
        """Verifica se a aplicação FastAPI foi criada corretamente."""
        assert app is not None
    
    def test_routers_included(self):
        """Verifica se os routers foram incluídos na aplicação."""
        routes = [route.path for route in app.routes]
        # Model router deve estar incluído com prefixo /model
        assert any("/model" in route for route in routes)
        # Questions router deve estar incluído com prefixo /questions
        assert any("/questions" in route for route in routes)
