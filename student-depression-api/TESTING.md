# Testes Unitários - API de Depressão Estudantil

Este diretório contém testes unitários e de integração para a API.

## Estrutura dos Testes

```
tests/
├── __init__.py              # Inicialização do pacote de testes
├── conftest.py              # Fixtures compartilhadas do pytest
├── test_main.py             # Testes da aplicação principal
├── test_model.py            # Testes do módulo de modelo e predição
├── test_questions.py        # Testes do endpoint de questões
├── test_integration.py      # Testes de integração entre endpoints
└── test_validation.py       # Testes de validação de dados
```

## Cobertura de Testes

### test_main.py
- ✅ Endpoint raiz (`GET /`)
- ✅ Inicialização da aplicação
- ✅ Inclusão de routers
- ✅ Configuração de CORS

### test_model.py
- ✅ Validação de `PredictionRequest`
- ✅ Validação de `PredictionResponse`
- ✅ Função `generate_feature_feedback`
- ✅ Importância das features
- ✅ Mapeamento de features para português
- ✅ Carregamento do modelo
- ✅ Casos especiais (pensamentos suicidas, pressão acadêmica, etc.)

### test_questions.py
- ✅ Endpoint de questões (`GET /questions`)
- ✅ Estrutura das questões
- ✅ Tipos válidos de questões
- ✅ Campos obrigatórios em cada questão
- ✅ Questões específicas (gênero, idade, CGPA, etc.)
- ✅ Headers de resposta

### test_integration.py
- ✅ Fluxo completo de requisições
- ✅ Tratamento de erros
- ✅ Configuração de CORS
- ✅ Formatos de resposta
- ✅ Estrutura de endpoints

### test_validation.py
- ✅ Validação de tipos de dados
- ✅ Campos obrigatórios
- ✅ Conversão de tipos
- ✅ Validação de strings

## Instalação

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. As dependências incluem:
   - `pytest`: Framework de testes
   - `pytest-asyncio`: Suporte para testes assincronos
   - `pytest-cov`: Relatório de cobertura de código

## Executar Testes

### Executar todos os testes:
```bash
pytest
```

### Executar com saída verbosa:
```bash
pytest -v
```

### Executar arquivo específico:
```bash
pytest tests/test_main.py
```

### Executar classe de testes específica:
```bash
pytest tests/test_model.py::TestGenerateFeatureFeedback
```

### Executar teste específico:
```bash
pytest tests/test_model.py::TestGenerateFeatureFeedback::test_feedback_generation_complete
```

### Executar com relatório de cobertura:
```bash
pytest --cov=src --cov-report=html --cov-report=term-missing
```

O relatório HTML será salvo em `htmlcov/index.html`

### Executar testes em modo watch (reexecuta ao salvar):
```bash
pytest-watch
```
(requer `pip install pytest-watch`)

## Fixtures Disponíveis

As fixtures estão definidas em `conftest.py`:

### `client`
Fornece um cliente TestClient para fazer requisições HTTP aos endpoints.

```python
def test_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
```

### `valid_prediction_data`
Dados válidos para predição (risco moderado).

### `high_risk_prediction_data`
Dados indicando alto risco de depressão.

### `low_risk_prediction_data`
Dados indicando baixo risco de depressão.

## Casos de Teste Principais

### 1. Validação de Entrada
- Campos obrigatórios presentes
- Tipos de dados corretos
- Valores dentro de ranges válidos

### 2. Geração de Feedback
- Feedback gerado para cada feature
- Mensagens apropriadas para cada faixa de valor
- Importância corretamente atribuída

### 3. Endpoints
- Status HTTP correto
- Estrutura de resposta esperada
- Content-type correto (application/json)

### 4. Integração
- Fluxo completo de uso
- Tratamento de erros
- CORS configurado corretamente

## Exemplo de Uso

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_questions():
    response = client.get("/questions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
```

## Relatório de Cobertura

Para gerar um relatório detalhado de cobertura:

```bash
pytest --cov=src --cov-report=html --cov-report=term
```

Após executar, abra `htmlcov/index.html` no navegador para ver a cobertura visual.

## Contribuindo

Ao adicionar novas features:

1. Escreva testes primeiro (TDD)
2. Execute testes para garantir que falham
3. Implemente a feature
4. Execute testes novamente para garantir que passam
5. Verifique cobertura de código

## Troubleshooting

### ImportError ao executar testes
Certifique-se de estar na raiz do projeto:
```bash
cd student-depression-api
pytest
```

### "No module named 'src'"
O pytest precisa encontrar os módulos. Certifique-se que há `__init__.py` em:
- `src/`
- `src/model/`
- `tests/`

### Testes falham com "model not found"
O arquivo do modelo (`student-depression-svm.joblib`) pode não existir. Alguns testes usam mock para este arquivo.

## Métricas Esperadas

- **Cobertura de Código**: > 80%
- **Taxa de Sucesso**: 100%
- **Tempo Total**: < 5 segundos

## Próximos Passos

Para melhorar ainda mais a cobertura:

1. Adicionar testes de endpoint POST (quando disponível)
2. Adicionar testes de performance
3. Adicionar testes de segurança
4. Adicionar testes de rate limiting (quando implementado)
5. Adicionar testes de autenticação (quando implementada)

