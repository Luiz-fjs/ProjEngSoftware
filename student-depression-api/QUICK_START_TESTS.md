# 🚀 GUIA RÁPIDO - Testes da API

## ⚡ Começar em 30 Segundos

### 1. Instalar Dependências
```bash
cd student-depression-api
pip install -r requirements.txt
```

### 2. Executar Testes
```bash
pytest tests/ -v
```

**Resultado esperado:**
```
✅ 65 passed in 0.17s
```

## 📊 Opções de Teste

### Teste Rápido (sem detalhes)
```bash
pytest -q
# Resultado: 65 passed in 0.15s
```

### Teste Completo (com saída detalhada)
```bash
pytest tests/ -v
```

### Com Cobertura de Código
```bash
pytest --cov=src --cov-report=term-missing
```

### Relatório HTML Interativo
```bash
pytest --cov=src --cov-report=html
# Abrir: htmlcov/index.html no navegador
```

### Usar Script Auxiliar
```bash
./run-tests.sh all        # Todos os testes
./run-tests.sh quick      # Teste rápido
./run-tests.sh coverage   # Com cobertura
./run-tests.sh html       # Relatório HTML
```

## 📁 Arquivos Principais

### Testes (7 arquivos)
- `tests/conftest.py` - Configuração e fixtures
- `tests/test_main.py` - Testes da app principal (4)
- `tests/test_model.py` - Testes do modelo (20)
- `tests/test_questions.py` - Testes de questões (18)
- `tests/test_integration.py` - Testes de integração (14)
- `tests/test_validation.py` - Testes de validação (9)

### Documentação (6 arquivos)
- `TESTING.md` - Guia completo
- `TESTING_GUIDE.md` - Tutorial detalhado
- `TEST_REPORT.md` - Relatório completo
- `TESTS_SUMMARY.md` - Resumo visual
- `README_TESTS.md` - README focado em testes
- `pytest.ini` - Configuração do pytest

## 📊 Estatísticas

```
✅ 65 testes passando
✅ 90% cobertura de código
✅ 0.17s tempo de execução
✅ 100% taxa de sucesso
```

## 🎯 Modelos de Uso

### Desenvolvimento Local
```bash
# Executar enquanto desenvolve
pip install pytest-watch
ptw
```

### Antes de Commit
```bash
pytest && git add . && git commit
```

### CI/CD Pipeline
```bash
pytest --cov=src --cov-fail-under=80 --junitxml=report.xml
```

### Debug de Teste Específico
```bash
pytest tests/test_model.py::TestGenerateFeatureFeedback -vv -s
```

## 🔍 Entender Resultados

```
===== 65 passed in 0.17s =====
✅ Sucesso! Todos os testes passaram
```

```
===== 60 passed, 5 failed =====
❌ Falhou! Ver detalhes com pytest -v
```

## 📚 Documentação Completa

Para documentação detalhada, consulte:
- [TESTING.md](TESTING.md) - Como usar os testes
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Tutorial com exemplos
- [TEST_REPORT.md](TEST_REPORT.md) - Relatório completo

## 💡 Dicas

1. **Sempre rodar testes antes de commitar**
   ```bash
   pytest && git add .
   ```

2. **Usar fixtures para dados compartilhados**
   ```python
   def test_com_fixture(valid_prediction_data):
       assert valid_prediction_data["age"] == 22
   ```

3. **Testar antes de implementar (TDD)**
   ```bash
   pytest  # Falha
   # Implementar código
   pytest  # Sucesso!
   ```

4. **Acompanhar cobertura**
   ```bash
   pytest --cov=src --cov-report=html
   ```

## 🚨 Troubleshooting

### Erro: No module named pytest
```bash
pip install -r requirements.txt
```

### Erro: No such file or directory
```bash
cd student-depression-api
```

### Testes muito lentos
```bash
pytest tests/test_main.py  # Apenas um arquivo
```

## 📞 Ajuda Rápida

```bash
# Ver toda ajuda do pytest
pytest --help

# Ver apenas testes
pytest --collect-only

# Parar no primeiro erro
pytest -x

# Mostrar print statements
pytest -s

# Testes últimas 3 vezes falhadas
pytest --lf
```

---

**Status**: ✅ 100% Funcional
**Próximo Passo**: Rodar `pytest` agora mesmo! 🚀
