This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Arquitetura do Frontend

Esta aplicação é a interface visual do **Terapp.IA**, um sistema para avaliação de risco de depressão em estudantes. O frontend é responsável por apresentar o questionário, coletar as respostas e exibir o feedback personalizado.

### 📁 Estrutura de Pastas

```
src/app/
├── page.tsx                    # Página inicial
├── layout.tsx                  # Layout geral da aplicação
├── globals.css                 # Estilos globais
├── context/                    # Gerenciamento de estado
│   └── survey_context.tsx      # Contexto do questionário
├── model/                      # Definição dos tipos de dados
│   ├── interfaces.tsx          # Interfaces principais
│   ├── question-base.tsx       # Base para todas as perguntas
│   ├── alternative-question.tsx # Perguntas de múltipla escolha
│   ├── slider-question.tsx     # Perguntas com escala deslizante
│   ├── date-question.tsx       # Perguntas de data
│   ├── number-question.tsx     # Perguntas numéricas
│   └── question-decorator.tsx  # Decoradores para perguntas
├── mappers/                    # Transformação de dados
│   └── question-maper.tsx      # Converte dados da API em componentes
├── repository/                 # Comunicação com o backend
│   └── student-depression-repository.tsx # Envia respostas e recebe resultados
└── survey/                     # Páginas do questionário
    ├── page.tsx                # Tela inicial do questionário
    ├── [surveyId]/             # Páginas dinâmicas por questão
    │   └── page.tsx
    ├── processing/             # Tela de processamento
    │   └── page.tsx
    └── component/              # Componentes específicos
        └── detailed_feedback.tsx # Exibição do feedback detalhado

public/
├── animated/                   # Animações e loading
│   ├── loading.tsx
│   └── loading.css
└── svgs/                       # Ícones e ilustrações
    ├── robot.tsx
    ├── survey-init.tsx
    ├── survey-processing.tsx
    └── survey-feedback.tsx
```

### 📄 Páginas da Aplicação

#### 1. **Página Inicial** (`/` - `app/page.tsx`)
A porta de entrada da aplicação. É onde o usuário tem o primeiro contato com o Terapp.IA.

**O que acontece aqui:**
- Apresenta o logotipo e nome da aplicação (Terapp.IA)
- Mostra cards informativos sobre a tecnologia de IA utilizada
- Explica o objetivo da análise personalizada
- Destaca a importância da privacidade e confidencialidade
- Possui um botão "Começar Avaliação" que direciona para o questionário

**Para que serve:** Dar as boas-vindas, explicar o propósito da ferramenta e preparar o usuário para responder o questionário.

---

#### 2. **Início do Questionário** (`/survey` - `app/survey/page.tsx`)
A página que antecede as perguntas. É uma preparação amigável antes de começar.

**O que acontece aqui:**
- Cumprimenta o usuário de forma acolhedora
- Explica que as perguntas são simples e sobre a rotina
- Esclarece o objetivo: entender como a pessoa tem se sentido
- Reforça que não há respostas certas ou erradas
- Lembra sobre a confidencialidade das informações
- Botão "Iniciar Questionário" que leva para a primeira pergunta

**Para que serve:** Deixar o usuário confortável e confiante para começar a responder as questões.

---

#### 3. **Perguntas Dinâmicas** (`/survey/[surveyId]` - `app/survey/[surveyId]/page.tsx`)
O coração do questionário. Esta página exibe uma pergunta de cada vez.

**O que acontece aqui:**
- Mostra uma barra de progresso no topo (ex: "Pergunta 3 de 20 - 15% concluído")
- Exibe a pergunta atual com suas opções de resposta
- Os tipos de pergunta variam: múltipla escolha, escalas deslizantes, data, número
- Botão "Próxima" só é habilitado quando uma resposta é selecionada
- Ao clicar em "Próxima", salva a resposta e vai para a próxima pergunta
- Na última pergunta, redireciona para a página de processamento

**Para que serve:** Coletar todas as respostas do usuário de forma organizada e interativa, uma pergunta por vez.

**Detalhe técnico:** O `[surveyId]` é uma rota dinâmica - significa que a mesma página serve para todas as perguntas, mudando apenas o conteúdo baseado no ID da pergunta na URL.

---

#### 4. **Processamento** (`/survey/processing` - `app/survey/processing/page.tsx`)
A página de espera enquanto a IA analisa as respostas.

**O que acontece aqui:**
- **Fase 1 - Loading:** Mostra uma animação de carregamento enquanto:
  - Pega todas as respostas do contexto
  - Organiza os dados no formato correto
  - Envia para a API do backend
  - Aguarda a resposta com a análise
- **Fase 2 - Resultado:** Assim que a API responde:
  - Para a animação de loading
  - Exibe um ícone de feedback
  - Mostra o resultado da análise (risco baixo, moderado ou alto)
  - Apresenta recomendações personalizadas
  - Exibe gráficos e detalhes sobre os fatores analisados
  - Oferece botão para voltar à página inicial

**Para que serve:** Fazer a ponte entre as respostas coletadas e o resultado da análise, mantendo o usuário informado durante o processamento.

**Fluxo de dados:**
1. Coleta as respostas do contexto
2. Converte data de nascimento em idade
3. Envia para `StudentDepressionRepository`
4. Repository faz chamada HTTP para a API
5. Recebe `SurveyPredictDepressionResponse` com a análise
6. Exibe o feedback visual usando o componente `DetailedFeedback`

---

### 🔄 Fluxo Completo da Aplicação

```
Aplicação Inicia
     ↓
[Carrega Questões do Backend]
  Repository.getQuestions()
  GET /questions
     ↓
Página Inicial (/)
     ↓
Início do Questionário (/survey)
     ↓
Pergunta 1 (/survey/1)
     ↓
Pergunta 2 (/survey/2)
     ↓
... (continua até a última pergunta)
     ↓
Processamento (/survey/processing)
   [Envia dados para API]
   POST /model/predict
   [Aguarda análise]
   [Recebe resultado]
     ↓
Exibe Feedback Detalhado
```

### 🔌 Comunicação com o Backend

#### **1. Obter Questões** (Executado na inicialização)
- **Quando:** Logo que a aplicação carrega, antes de qualquer página ser exibida
- **Onde:** `SurveyProvider` no contexto (`context/survey_context.tsx`)
- **Método:** `GET`
- **Endpoint:** `https://api-terapp-ia.onrender.com/questions`
- **O que faz:**
  1. Repository faz requisição para buscar todas as perguntas
  2. Recebe um array de perguntas em JSON (formato "raw")
  3. Mapper transforma os dados raw em objetos `QuestionBase`
  4. Armazena no contexto para serem usadas em todas as páginas
- **Exemplo de resposta:**
  ```json
  [
    {
      "id": "1",
      "text": "Qual é o seu gênero?",
      "type": "alternative",
      "options": ["Masculino", "Feminino", "Outro"]
    },
    ...
  ]
  ```

#### **2. Enviar Respostas e Obter Análise** (Executado após última pergunta)
- **Quando:** Usuário termina o questionário e chega na página de processamento
- **Onde:** `Processing` page (`survey/processing/page.tsx`)
- **Método:** `POST`
- **Endpoint:** `https://api-terapp-ia.onrender.com/model/predict`
- **O que envia:**
  ```json
  {
    "age": 22,
    "gender": "Female",
    "academic_pressure": 4,
    "study_satisfaction": 3,
    ...
  }
  ```
- **O que recebe:**
  ```json
  {
    "prediction": "Low Risk",
    "probability": 0.85,
    "recommendations": ["..."],
    "factors": {...}
  }
  ```

**Fluxo técnico completo:**
1. `SurveyProvider` carrega questões via `getQuestions()`
2. Usuário responde questões (salvas no contexto)
3. Na última pergunta → redireciona para `/survey/processing`
4. Processing pega respostas do contexto
5. Envia para `repository.requestFeedback()`
6. Exibe resultado usando `DetailedFeedback`

### 🛠️ Tecnologias Utilizadas

- **Next.js 15**: Framework React com renderização no servidor
- **React 19**: Biblioteca para construção de interfaces
- **TypeScript**: Tipagem estática para maior segurança no código
- **Tailwind CSS**: Estilização rápida e responsiva
- **Material Icons**: Ícones do Google Material Design

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
