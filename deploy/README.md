# Deploy - Terapp.IA

Este documento descreve como o sistema Terapp.IA é implantado na plataforma **Render** ([https://render.com/](https://render.com/)).

---

## 🌐 Visão Geral do Deploy

O projeto utiliza dois serviços separados na plataforma Render:

1. **Backend (API)** - FastAPI hospedado como Web Service
2. **Frontend (App)** - Next.js hospedado como Web Service

Ambos estão integrados com o **GitHub** para deploy automático sempre que há mudanças no código.

---

## 🔧 Backend - API FastAPI

### **Tipo de Serviço**
- **Web Service** (Render)
- Plano: **Free** (gratuito)
- Runtime: **Python 3.12**

### **Configuração**
A API está configurada através do arquivo `render.yaml` localizado em `student-depression-api/`:

```yaml
services:
  - type: web
    name: fastapi-example
    runtime: python
    plan: free
    autoDeploy: false
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### **Como Funciona**

1. **Integração GitHub**
   - O repositório está conectado ao Render
   - Quando há push/merge para a branch principal, o Render é notificado

2. **Processo de Build**
   ```bash
   pip install -r requirements.txt
   ```
   - Instala todas as dependências Python listadas no `requirements.txt`
   - Inclui FastAPI, scikit-learn, pandas, joblib, etc.

3. **Inicialização do Servidor**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
   - Inicia o servidor FastAPI
   - `--host 0.0.0.0`: Aceita conexões de qualquer IP
   - `--port $PORT`: Usa a porta fornecida pelo Render (variável de ambiente)

4. **URL de Produção**
   - `https://api-terapp-ia.onrender.com`

---

## 🎨 Frontend - Next.js App

### **Tipo de Serviço**
- **Web Service** (Render)
- Plano: **Free** (gratuito)
- Framework: **Next.js 15**

### **Configuração**
O frontend não possui arquivo `render.yaml`. A configuração é feita diretamente no painel do Render.

### **Como Funciona**

1. **Integração GitHub**
   - Repositório conectado ao Render
   - Branch monitorada: `main` ou `master`

2. **Processo de Build**
   ```bash
   npm install
   npm run build
   ```
   - Instala dependências (React, Next.js, Tailwind CSS)
   - Gera build otimizado de produção

3. **Comando de Start**
   ```bash
   npm start
   ```
   - Inicia servidor Next.js em modo produção
   - Serve páginas estáticas e dinâmicas

4. **URL de Produção**
   - `https://projengsoftware-o465.onrender.com/`

---

## 🔄 Fluxo de Deploy Completo

```
Desenvolvedor faz commit
        ↓
    git push origin main
        ↓
GitHub recebe o código
        ↓
    ┌─────────────────┴──────────────────┐
    ↓                                    ↓
Render (Backend)              Render (Frontend)
    ↓                                    ↓
Detecta mudanças              Detecta mudanças
    ↓                                    ↓
Clona repositório            Clona repositório
    ↓                                    ↓
pip install -r              npm install
requirements.txt            npm run build
    ↓                                    ↓
Build completo               Build completo
    ↓                                    ↓
uvicorn main:app             npm start
    ↓                                    ↓
✅ API Online                ✅ App Online
    ↓                                    ↓
api-terapp-ia.onrender.com   projengsoftware-o465.onrender.com
```

---

## 🔗 Integração GitHub

### **Como Conectar**
1. **Criar conta no Render** ([render.com](https://render.com))

2. **Conectar GitHub**
   - No dashboard do Render, clique em "New +"
   - Selecione "Web Service" (tanto para API quanto para frontend)
   - Conecte sua conta GitHub
   - Autorize acesso ao repositório
   - Autorize acesso ao repositório

3. **Configurar o Serviço**
   - Selecione o repositório: `reberthkss/ProjEngSoftware`
   - Escolha a branch: `main`
   - Defina o diretório raiz (se necessário)

4. **Deploy Automático**
   - Por padrão, `autoDeploy` pode ser `true` ou `false`
   - Se `true`: Deploy automático a cada push
   - Se `false`: Deploy manual através do dashboard

---

## ⚙️ Variáveis de Ambiente

### **Backend**
O Render fornece automaticamente:
- `PORT`: Porta onde o servidor deve rodar
- `PYTHON_VERSION`: Versão do Python (3.12)

### **Frontend**
Pode adicionar variáveis personalizadas no dashboard:
- `NEXT_PUBLIC_API_URL`: URL da API (se necessário)

---

## 🔗 Links Úteis

- 📚 [Documentação Render](https://render.com/docs)
- 🐍 [Deploy FastAPI no Render](https://render.com/docs/deploy-fastapi)
- ⚛️ [Deploy Next.js no Render](https://render.com/docs/deploy-nextjs)
- 🆓 [Render Free Tier](https://render.com/docs/free)

---

## 📌 URLs do Projeto

- **API (Backend)**: https://api-terapp-ia.onrender.com
- **App (Frontend)**: https://projengsoftware-o465.onrender.com/
- **Repositório GitHub**: https://github.com/reberthkss/ProjEngSoftware
