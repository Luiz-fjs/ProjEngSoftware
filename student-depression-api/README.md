# Student Depression API - Backend Terapp.IA

API REST construída com FastAPI para análise de risco de depressão em estudantes usando Machine Learning.

## Arquitetura do Backend

Esta é a parte "inteligente" do Terapp.IA, responsável por processar os dados dos questionários e fazer previsões usando um modelo de Machine Learning já treinado.

### 📁 Estrutura de Pastas

```
student-depression-api/
├── main.py                     # Ponto de entrada da aplicação
├── requirements.txt            # Dependências Python
├── render.yaml                 # Configuração para deploy
├── pytest.ini                  # Configuração de testes
├── run-tests.sh               # Script para executar testes
│
├── src/                        # Código fonte
│   ├── data/
│   │   └── questions.json      # Perguntas do questionário
│   ├── model/
│   │   ├── model.py           # Lógica de predição e feedback
│   │   ├── questions.py       # Endpoint de questões
│   │   ├── prediction_request.py   # Modelo de entrada
│   │   └── prediction_response.py  # Modelo de saída
│   └── resources/
│       └── student-depression-svm.joblib  # Modelo ML treinado
│
└── tests/                      # Testes automatizados
    ├── test_main.py           # Testes da aplicação principal
    ├── test_model.py          # Testes do modelo ML
    ├── test_questions.py      # Testes de questões
    ├── test_validation.py     # Testes de validação
    └── test_integration.py    # Testes de integração
```

---

## 🔌 Endpoints da API

### **1. GET `/questions`**
Retorna todas as perguntas do questionário.

**Para que serve:** O frontend busca essas perguntas quando a aplicação inicia, para montar o questionário dinamicamente.

**Resposta:**
```json
[
  {
    "id": "gender",
    "text": "Qual é o seu gênero?",
    "type": "alternative",
    "options": ["Masculino", "Feminino", "Outro"]
  },
  {
    "id": "age",
    "text": "Qual é a sua data de nascimento?",
    "type": "date"
  },
  {
    "id": "academic_pressure",
    "text": "Como você avalia a pressão acadêmica?",
    "type": "slider",
    "min": 1,
    "max": 5
  }
]
```

**Implementação:**
- Localização: `src/model/questions.py`
- Lê o arquivo `src/data/questions.json`
- Retorna em formato JSON para o frontend

---

### **2. POST `/model/predict`**
Recebe as respostas do questionário e retorna a análise de risco de depressão.

**Para que serve:** Processar todas as respostas do usuário e gerar uma previsão usando o modelo de Machine Learning.

**Entrada esperada:**
```json
{
  "gender": "Female",
  "age": 22,
  "academic_pressure": 4,
  "cgpa": 7.5,
  "study_satisfaction": 3,
  "sleep_duration": "7-8 horas",
  "dietary_habits": "Moderadamente saudáveis",
  "suicidal_thoughts": "Não",
  "work_study_hours": 6,
  "financial_stress": 3,
  "family_history": "Não"
}
```

**Saída:**
```json
{
  "prediction": 0,
  "probability": [0.85, 0.15],
  "depression_risk": "Não depressivo",
  "feature_feedback": [
    {
      "feature": "Pensamentos Suicidas",
      "user_value": "Não",
      "importance": 48.5,
      "impact_level": "CRÍTICO",
      "message": "Sua resposta 'Não' é extremamente protetiva...",
      "context": "Este é o fator mais importante do modelo..."
    },
    {
      "feature": "Pressão Acadêmica",
      "user_value": "4",
      "importance": 26.1,
      "impact_level": "ALTO",
      "message": "Nível de pressão acadêmica elevado...",
      "context": "Segundo fator mais importante..."
    }
    // ... mais feedbacks para cada fator
  ]
}
```

**Implementação:**
- Localização: `src/model/model.py`
- Valida os dados recebidos usando Pydantic
- Transforma os dados em formato aceito pelo modelo (DataFrame)
- Carrega o modelo treinado (`student-depression-svm.joblib`)
- Faz a predição
- Gera feedback personalizado para cada fator
- Retorna resultado estruturado

---

## 🧠 Como Funciona o Modelo de Machine Learning

### **Tipo de Modelo**
- **SVM (Support Vector Machine)** não linear
- Treinado com dados reais de estudantes
- Arquivo salvo: `student-depression-svm.joblib`

### **Fatores Analisados (por ordem de importância)**

1. **Pensamentos Suicidas** (48.5%) - CRÍTICO
   - O fator mais importante de todos
   - Quase metade do peso da predição

2. **Pressão Acadêmica** (26.1%) - ALTO
   - Segundo fator mais relevante
   - Avalia estresse relacionado aos estudos

3. **Estresse Financeiro** (11.4%) - ALTO
   - Preocupações com dinheiro e despesas

4. **Idade** (5.9%) - MODERADO
   - Diferentes faixas etárias têm vulnerabilidades distintas

5. **Horas de Estudo/Trabalho** (2.4%) - BAIXO

6. **Hábitos Alimentares** (2.4%) - BAIXO

7. **Satisfação com Estudos** (2.3%) - BAIXO

8. **Duração do Sono** (0.6%) - MUITO BAIXO

9. **Gênero** (0.4%) - MUITO BAIXO

10. **Histórico Familiar** (0.1%) - MUITO BAIXO

11. **Coeficiente de Rendimento/CR** (-0.1%) - MUITO BAIXO

### **Como a Predição Funciona**

1. **Recebe os dados** do usuário em formato JSON
2. **Converte em DataFrame** (formato que o modelo entende)
3. **Aplica o modelo SVM** treinado
4. **Calcula probabilidades** de cada classe (depressivo/não depressivo)
5. **Gera feedback personalizado** analisando cada fator individualmente
6. **Retorna resultado estruturado** com:
   - Predição (0 = não depressivo, 1 = depressivo)
   - Probabilidades
   - Nível de risco
   - Feedback detalhado por fator

### **Função de Feedback**
A função `generate_feature_feedback()` analisa cada resposta do usuário e gera mensagens personalizadas baseadas em:
- Valor informado pelo usuário
- Importância do fator no modelo
- Contexto e interpretação do valor

---

## 🔄 Fluxo Completo da API

```
Frontend solicita perguntas
     ↓
GET /questions
     ↓
[Lê questions.json]
     ↓
Retorna perguntas em JSON
     ↓
[Usuário responde no frontend]
     ↓
Frontend envia respostas
     ↓
POST /model/predict
     ↓
[Valida dados com Pydantic]
     ↓
[Converte para DataFrame]
     ↓
[Carrega modelo SVM do disco]
     ↓
[Executa predição]
     ↓
[Calcula probabilidades]
     ↓
[Gera feedback personalizado]
     ↓
Retorna análise completa
     ↓
Frontend exibe resultado
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **FastAPI** | 0.116.1 | Framework web moderno e rápido |
| **Python** | 3.12+ | Linguagem de programação |
| **scikit-learn** | 1.6.1 | Biblioteca de Machine Learning |
| **joblib** | 1.5.1 | Para salvar/carregar modelos ML |
| **pandas** | 2.3.1 | Manipulação de dados |
| **Pydantic** | 2.11.7 | Validação de dados |
| **pytest** | - | Testes automatizados |

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório**
```bash
cd student-depression-api
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # No Mac/Linux
# ou
venv\Scripts\activate     # No Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o servidor**
```bash
uvicorn main:app --reload
```

5. **Acesse a documentação interativa**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🧪 Testes

A API possui testes automatizados para garantir qualidade e confiabilidade.

### Executar todos os testes
```bash
pytest
```

### Executar com cobertura
```bash
pytest --cov=src --cov-report=html
```

### Tipos de Testes
- **test_main.py**: Testa endpoints principais
- **test_model.py**: Testa lógica de predição
- **test_questions.py**: Testa endpoint de questões
- **test_validation.py**: Testa validação de dados
- **test_integration.py**: Testa fluxo completo

---

## 🌐 Deploy

A API está configurada para deploy automático no **Render.com**.

**URL de produção:** `https://api-terapp-ia.onrender.com`

O arquivo `render.yaml` contém todas as configurações necessárias.

---

## 🔒 Segurança e CORS

A API está configurada para aceitar requisições de:
- `http://localhost:3000` (desenvolvimento)
- `https://projengsoftware-o465.onrender.com/` (produção)

Configuração em `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📊 Modelos de Dados

### PredictionRequest (Entrada)
Define o formato esperado das respostas do usuário.

### PredictionResponse (Saída)
Define a estrutura da resposta com análise e feedback.

Ambos usam **Pydantic** para validação automática de tipos e valores.

---

## 📝 Observações Importantes

1. **Modelo Pré-treinado**: O modelo SVM já vem treinado no arquivo `.joblib`. Não é necessário treinar novamente.

2. **Dados Sensíveis**: A API não armazena respostas dos usuários. Tudo é processado em tempo real.

3. **Validação Rigorosa**: Pydantic garante que apenas dados válidos sejam processados.

4. **Feedback Personalizado**: Cada predição gera análise específica baseada nas respostas individuais.

5. **Documentação Automática**: FastAPI gera documentação interativa automaticamente em `/docs`.
