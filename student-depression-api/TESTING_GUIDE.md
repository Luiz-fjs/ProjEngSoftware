# Guia Completo de Testes - API de Depressão Estudantil

## 📚 Índice

1. [Instalação](#instalação)
2. [Executando Testes](#executando-testes)
3. [Estrutura dos Testes](#estrutura-dos-testes)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Interpretando Resultados](#interpretando-resultados)
6. [Troubleshooting](#troubleshooting)

## 🔧 Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Passos

1. **Navegar para o diretório da API**:
```bash
cd student-depression-api
```

2. **Instalar dependências** (incluso pytest):
```bash
pip install -r requirements.txt
```

3. **Verificar instalação**:
```bash
pytest --version
```

## 🚀 Executando Testes

### Comando Básico

```bash
pytest
```

**Resultado esperado:**
```
65 passed in 0.55s
```

### Modo Verboso (mais detalhes)

```bash
pytest -v
```

Mostra cada teste sendo executado:
```
tests/test_main.py::TestMainApp::test_root_endpoint PASSED
tests/test_main.py::TestMainApp::test_app_cors_headers PASSED
...
```

### Com Relatório de Cobertura

```bash
pytest --cov=src --cov-report=term-missing
```

Mostra:
- Quais linhas de código foram executadas
- Quais não foram (missing)
- Percentual de cobertura

### Gerar Relatório HTML

```bash
pytest --cov=src --cov-report=html
```

Cria pasta `htmlcov/` com relatório interativo. Abra `htmlcov/index.html` no navegador.

### Executar Arquivo Específico

```bash
pytest tests/test_main.py
```

### Executar Classe de Testes

```bash
pytest tests/test_model.py::TestGenerateFeatureFeedback
```

### Executar Teste Específico

```bash
pytest tests/test_model.py::TestGenerateFeatureFeedback::test_feedback_generation_complete -v
```

### Parar no Primeiro Erro

```bash
pytest -x
```

### Executar e Mostrar Prints

```bash
pytest -v -s
```

### Executar com Timeout

```bash
pytest --timeout=5
```

(requer `pip install pytest-timeout`)

## 📁 Estrutura dos Testes

```
tests/
├── __init__.py              # Marca como pacote Python
├── conftest.py              # Configuração e fixtures compartilhadas
│
├── test_main.py             # Testes da aplicação principal
│   ├── TestMainApp
│   └── TestAppInitialization
│
├── test_model.py            # Testes do módulo de modelo
│   ├── TestPredictionRequest
│   ├── TestPredictionResponse
│   ├── TestModelExample
│   ├── TestGenerateFeatureFeedback
│   ├── TestFeatureImportance
│   └── TestModelLoading
│
├── test_questions.py        # Testes do endpoint de questões
│   ├── TestQuestionsEndpoint
│   ├── TestQuestionsEndpointErrors
│   ├── TestQuestionsContent
│   ├── TestQuestionsDescriptions
│   └── TestQuestionsResponseHeaders
│
├── test_integration.py      # Testes de integração
│   ├── TestIntegration
│   ├── TestErrorHandling
│   ├── TestCORSConfiguration
│   ├── TestResponseFormats
│   ├── TestModelExample
│   └── TestEndpointStructure
│
└── test_validation.py       # Testes de validação
    ├── TestPredictionRequestValidation
    ├── TestPredictionResponseValidation
    └── TestFieldTypeValidation
```

## 💡 Exemplos Práticos

### Exemplo 1: Testar um Endpoint

```python
def test_get_questions():
    # Fazer requisição
    response = client.get("/questions")
    
    # Verificar status
    assert response.status_code == 200
    
    # Verificar tipo de resposta
    data = response.json()
    assert isinstance(data, list)
```

### Exemplo 2: Testar Validação de Dados

```python
from src.model.prediction_request import PredictionRequest

def test_valid_prediction_request():
    request_data = {
        "gender": "Masculino",
        "age": 22,
        "academic_pressure": 4,
        "cgpa": 7.5,
        # ... outros campos
    }
    
    request = PredictionRequest(**request_data)
    assert request.age == 22
```

### Exemplo 3: Testar Lógica de Negócio

```python
from src.model.model import generate_feature_feedback

def test_feedback_generation():
    user_data = {
        "gender": "Masculino",
        "age": 22,
        "academic_pressure": 4,
        # ... outros campos
    }
    
    feedback = generate_feature_feedback(user_data)
    
    # Verificar se feedback foi gerado
    assert isinstance(feedback, list)
    assert len(feedback) > 0
    
    # Verificar estrutura
    for item in feedback:
        assert "feature" in item
        assert "message" in item
```

### Exemplo 4: Testar com Fixtures

```python
def test_with_fixture(client, valid_prediction_data):
    # client vem de conftest.py
    response = client.get("/questions")
    
    # valid_prediction_data vem de conftest.py
    assert valid_prediction_data["age"] == 22
```

## 📊 Interpretando Resultados

### Status de Sucesso

```
======================== 65 passed in 0.55s ========================
```

✅ Todos os testes passaram

### Com Falhas

```
======================== 60 passed, 5 failed in 1.2s ========================
```

❌ Alguns testes falharam. Ver detalhes abaixo.

### Relatório de Cobertura

```
Name                               Stmts   Miss  Cover
------------------------------------------------------
src/model/model.py                   108     12    89%
src/model/prediction_request.py       13      0   100%
```

Significa:
- `model.py` tem 108 linhas, 12 não foram executadas, 89% cobertura
- `prediction_request.py` tem 100% de cobertura

## 🔍 Entendendo Outputs

### PASSED ✅
```
tests/test_main.py::TestMainApp::test_root_endpoint PASSED
```
O teste foi executado com sucesso.

### FAILED ❌
```
tests/test_main.py::TestMainApp::test_root_endpoint FAILED
```
O teste falhou. Use `-v` para ver o motivo.

### SKIPPED ⏭️
```
tests/test_main.py::TestMainApp::test_root_endpoint SKIPPED
```
O teste foi pulado (geralmente por @pytest.mark.skip ou condicional).

### ERROR 🚨
```
tests/test_main.py::TestMainApp::test_root_endpoint ERROR
```
Erro durante a coleta ou setup do teste.

## 🛠️ Troubleshooting

### Erro: ModuleNotFoundError: No module named 'fastapi'

**Solução:**
```bash
pip install -r requirements.txt
```

### Erro: No such file or directory: 'pytest.ini'

**Solução:**
Certifique-se de estar no diretório correto:
```bash
cd student-depression-api
```

### Testes lentos

**Solução:** Execute apenas testes específicos
```bash
pytest tests/test_main.py  # Apenas main
```

### Importação de módulos falhando

**Solução:** Certifique-se que há `__init__.py` em:
- `student-depression-api/tests/`
- `student-depression-api/src/`
- `student-depression-api/src/model/`

### Erro com cobertura

**Solução:**
```bash
pip install pytest-cov
```

## 📈 Casos de Uso Comuns

### CI/CD Pipeline

```bash
# Executar com cobertura e falhar se < 80%
pytest --cov=src --cov-report=term --cov-fail-under=80
```

### Desenvolvimento Local

```bash
# Executar tests em modo watch
pip install pytest-watch
ptw
```

### Antes de Commit

```bash
# Executar testes + linter
pytest && pylint src/ && black src/
```

### Relatório Detalhado

```bash
# Gerar vários relatórios
pytest \
  --cov=src \
  --cov-report=html \
  --cov-report=term \
  --cov-report=xml \
  -v
```

## 🎯 Boas Práticas

1. **Executar testes antes de commit**
2. **Manter cobertura > 80%**
3. **Nomear testes descritivamente**
4. **Usar fixtures para dados compartilhados**
5. **Agrupar testes em classes**
6. **Testar casos de erro**

## 📞 Suporte

Para dúvidas sobre pytest, consulte:
- [Documentação Oficial](https://docs.pytest.org/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

---

**Última atualização:** 27 de Novembro de 2025
