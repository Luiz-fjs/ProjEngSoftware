![App name](/images/terappia_name.png)
## Integrantes: <br/>
  - Luiz Felipe 170.294 <br/>
  - Laura Tomasin Barbosa 163.884 <br/>
  - Rafael da Rocha 163.973 <br/>
  - Reberth Kelvin 141.589 <br/>
  - Emanuella Santos 163.696 <br/>

## Projeto:
  O Terapp.IA é uma aplicação que combinará análise preditiva de Machine Learning com uma interface web intuitiva para avaliar fatores de risco de depressão em estudantes. O sistema usará a analise de múltiplas variáveis psicossociais e acadêmicas para fornecer insights personalizados e feedback detalhado.

## Visão geral do projeto
![General architecture](/images/terappia_geral_arch.png)

### Protótipo no Figma  
<a href="https://www.figma.com/design/VRxuzMZySmUrqWpRSeHHk7/Projeto-EngenhariadeSoftware?node-id=0-1&p=f&t=xfqKJBAuqdWSb6hc-0">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" width="60">
</a>

## Tech Stack
  #### Front-end:
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Next.js** | 15.3.4 | Framework React com SSR e otimizações automáticas |
| **React** | 19.0.0 | Biblioteca para construção de interfaces de usuário |
| **TypeScript** | 5.x | Superset do JavaScript com tipagem estática |
| **Tailwind CSS** | 4.x | Framework CSS utilitário para estilização |
| **Material Icons** | 1.13.14 | Biblioteca de ícones do Google Material Design |
| **Node.js** | 18+ | Ambiente de execução JavaScript |

  #### Backend:
| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **FastAPI** | 0.116.1 | Framework web moderno e de alta performance |
| **Python** | 3.12+ | Linguagem de programação |
| **Pydantic** | 2.11.7 | Validação de dados e serialização |
| **scikit-learn** | 1.6.1 | Biblioteca de Machine Learning |
| **pandas** | 2.3.1 | Manipulação e análise de dados |
| **NumPy** | 2.3.1 | Computação científica |
| **joblib** | 1.5.1 | Persistência de modelos ML |


###  Arquitetura do Sistema

Arquitetura baseada Arquitetura Limpa e de monorepo
```
TerappIA/
├── terappIA-frontend/          
├── terappIA-api/    
└── README.md                  
```


### Configuração e Execução

#### Frontend (Desenvolvimento)

```bash
cd terappIA-frontend/

# Instalar dependências
npm install

# Executar em modo desenvolvimento
npm run dev

# Build para produção
npm run build

# Executar produção
npm start
```

#### Backend (Desenvolvimento)

```bash
cd terappIA-api/

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
uvicorn main:app --reload

# Documentação interativa
# Acesse: http://localhost:8000/docs
```
