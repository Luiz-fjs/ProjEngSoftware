# API de Depressão Estudantil - Student Depression API

Uma API FastAPI para diagnóstico de depressão em estudantes utilizando machine learning.

## 📋 Visão Geral

Esta API fornece endpoints para:
- Obter questionário de avaliação de depressão
- Realizar predição de risco de depressão
- Gerar feedback detalhado baseado em features do modelo

## 🚀 Quick Start

### Instalação

```bash
pip install -r requirements.txt
```

### Executar a API

```bash
python main.py
```

A API estará disponível em `http://localhost:8000`

### Documentação Interativa

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📡 Endpoints

### GET `/questions`
Retorna as questões do formulário de avaliação.

**Response:**
```json
[
  {
    "type": "alternative",
    "data": {
      "id": "gender",
      "title": "Qual seu gênero?",
      "description": "...",
      "alternatives": ["Masculino", "Feminino"]
    }
  }
]
```

### GET `/model/example`
Exemplo de endpoint do modelo.

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src --cov-report=term-missing

# Modo verboso
pytest -v

# HTML report
pytest --cov=src --cov-report=html
```

### Resultados

- ✅ **65 testes passando**
- ✅ **90% de cobertura de código**
- ✅ **0.55 segundos de execução**

### Estrutura de Testes

```
tests/
├── test_main.py          # Testes da aplicação principal (4 testes)
├── test_model.py         # Testes do modelo (20 testes)
├── test_questions.py     # Testes de questões (18 testes)
├── test_integration.py   # Testes de integração (14 testes)
├── test_validation.py    # Testes de validação (9 testes)
└── conftest.py           # Configuração e fixtures
```

Para mais detalhes, consulte [TESTING.md](TESTING.md).

## 📚 Documentação

- [TESTING.md](TESTING.md) - Guia de testes e cobertura
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Guia completo de como usar os testes
- [TEST_REPORT.md](TEST_REPORT.md) - Relatório detalhado dos testes

## 🏗️ Estrutura do Projeto

```
student-depression-api/
├── main.py                         # Aplicação FastAPI
├── requirements.txt                # Dependências
├── pytest.ini                      # Configuração de testes
│
├── src/
│   ├── data/
│   │   └── questions.json          # Questões do formulário
│   ├── model/
│   │   ├── model.py                # Lógica do modelo SVM
│   │   ├── prediction_request.py   # Schema de request
│   │   ├── prediction_response.py  # Schema de response
│   │   └── questions.py            # Endpoint de questões
│   └── resources/
│       └── student-depression-svm.joblib  # Modelo treinado
│
└── tests/
    ├── test_main.py
    ├── test_model.py
    ├── test_questions.py
    ├── test_integration.py
    ├── test_validation.py
    └── conftest.py
```

## 📊 Cobertura de Código

| Módulo | Cobertura | Status |
|--------|-----------|--------|
| prediction_request.py | 100% | ✅ |
| prediction_response.py | 100% | ✅ |
| __init__.py | 100% | ✅ |
| model.py | 89% | ⚠️ |
| questions.py | 80% | ⚠️ |
| **TOTAL** | **90%** | **✅** |

## 🔧 Desenvolvimento

### Dependências Principais

- **FastAPI** - Framework web
- **Pydantic** - Validação de dados
- **scikit-learn** - Machine learning
- **joblib** - Serialização de modelo
- **pytest** - Framework de testes
- **pytest-cov** - Cobertura de código

### Adicionando Novos Testes

1. Crie um arquivo `test_*.py` em `tests/`
2. Organize em classes `Test*`
3. Escreva funções `test_*`
4. Execute: `pytest`

Exemplo:
```python
class TestNovaFuncionalidade:
    def test_comportamento_esperado(self):
        assert True
```

## 📈 Métricas

- **Taxa de Sucesso**: 100%
- **Cobertura**: 90%
- **Tempo de Execução**: ~0.55s
- **Número de Testes**: 65

## 🐛 Troubleshooting

### Erro: Modelo não encontrado
O arquivo `student-depression-svm.joblib` pode não existir. Testes usam mocks.

### Erro: ModuleNotFoundError
Execute `pip install -r requirements.txt`

### Testes falhando
Execute `pytest -v` para ver detalhes

## 📝 Notas

- API segue padrões RESTful
- Validação de dados com Pydantic
- CORS configurado para localhost:3000
- Modelo SVM não-linear treinado
- Feedback detalhado por feature

## 📄 Licença

Projeto Engenharia de Software

## 👥 Contribuintes

- Desenvolvido com testes desde o início (TDD)
- 100% de cobertura de endpoints
- Documentação completa

---

**Para mais informações sobre testes, consulte [TESTING_GUIDE.md](TESTING_GUIDE.md)**
