# Modelo de Machine Learning - Terapp.IA

Este projeto contém o notebook Jupyter usado para treinar o modelo de Machine Learning que detecta risco de depressão em estudantes.

## 📓 Sobre o Notebook (`terappia_model.ipynb`)

O notebook documenta todo o processo de criação do modelo de predição, desde a obtenção dos dados até a exportação do modelo final para ser usado na API.

---

## 🎯 Objetivo do Projeto

Criar um modelo de Machine Learning capaz de **identificar estudantes em risco de depressão** com base em fatores psicossociais e acadêmicos, para permitir intervenções preventivas e direcionadas.

---

## 📊 Dataset Utilizado

**Fonte:** [Student Depression Dataset - Kaggle](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)

O dataset original contém informações sobre estudantes incluindo:
- Dados demográficos (idade, gênero, cidade)
- Informações acadêmicas (curso, CR, satisfação com estudos)
- Fatores de risco (pressão acadêmica, estresse financeiro, pensamentos suicidas)
- Hábitos de vida (sono, alimentação, horas de estudo)
- Histórico familiar de doenças mentais

---

## 🔧 Processamento dos Dados

### **Dados Removidos**
Algumas colunas foram removidas por não serem relevantes para o modelo:
- **ID**: Identificador único, não tem valor preditivo
- **Cidade**: Localização geográfica não mostrou relevância
- **Curso/Degree**: Tipo de graduação não impactou significativamente
- **Profissão**: Focado apenas em estudantes
- **Job Satisfaction**: Relacionado a trabalho, não a estudos
- **Work Pressure**: Pressão de trabalho (mantemos apenas pressão acadêmica)

### **Limpeza de Dados**
- Remoção de valores inválidos (ex: "?" em estresse financeiro)
- Remoção de linhas com dados faltantes (NaN)

### **Tradução para Português**
Para facilitar o uso na aplicação brasileira, os dados foram traduzidos:
- **Gênero**: Male → Masculino, Female → Feminino
- **Duração do Sono**: Less than 5 hours → Menos de 5 horas, etc.
- **Hábitos Alimentares**: Healthy → Muito saudáveis, Moderate → Moderadamente saudáveis
- **Respostas Sim/Não**: Yes → Sim, No → Não

---

## 🧠 Modelo Utilizado: SVM (Support Vector Machine)

### **O que é SVM?**
SVM (Máquina de Vetores de Suporte) é um algoritmo de Machine Learning usado para classificação. Ele funciona encontrando o melhor "limite de decisão" entre duas classes de dados.

**Imagine assim:**
- Você tem pontos vermelhos (estudantes com depressão) e pontos azuis (estudantes sem depressão) espalhados em um gráfico
- O SVM desenha uma linha (ou superfície) que melhor separa esses dois grupos
- Novos estudantes são classificados baseado em qual lado da linha eles caem

### **Por que SVM com Kernel RBF?**
Usamos SVM com **kernel RBF (Radial Basis Function)** porque:

✅ **Não Linear**: A relação entre os fatores e a depressão não é uma linha reta simples. O kernel RBF permite capturar padrões complexos e curvas nos dados.

✅ **Relações Complexas**: Consegue identificar interações entre múltiplos fatores (ex: pressão acadêmica + falta de sono = risco maior)

✅ **Boa Performance**: Mostrou alta acurácia e recall nos testes

✅ **Robusto**: Funciona bem mesmo com dados que têm distribuições complexas

### **Configurações do Modelo**
```python
SVC(kernel='rbf', probability=True, random_state=42)
```
- **kernel='rbf'**: Usa função de base radial (não linear)
- **probability=True**: Permite calcular probabilidades das predições
- **random_state=42**: Garante reprodutibilidade dos resultados

---

## 🔄 Pipeline de Processamento

O modelo usa um **Pipeline** que combina pré-processamento e classificação:

### **1. Pré-processamento Automático**

**Para Dados Numéricos** (idade, CR, horas de estudo, etc.):
- **StandardScaler**: Normaliza os valores para terem a mesma escala
- Por quê? Evita que features com valores grandes dominem o modelo

**Para Dados Categóricos** (gênero, sono, alimentação, etc.):
- **OneHotEncoder**: Transforma categorias em números binários
- Exemplo: "Masculino" vira [1, 0], "Feminino" vira [0, 1]
- Por quê? Modelos de ML só entendem números

### **2. Classificação**
Após o pré-processamento, o SVM faz a classificação:
- Entrada: 11 características do estudante
- Saída: Depressivo (1) ou Não Depressivo (0)

---

## 📈 Métricas de Performance

O modelo foi avaliado usando:

### **Acurácia**
Percentual de predições corretas no total.
- Mede o quão frequente o modelo acerta

### **Recall (Sensibilidade)**
Percentual de casos de depressão que o modelo conseguiu identificar.
- **Métrica mais importante neste projeto!**
- Por quê? É melhor ter um "falso alarme" do que perder um caso real de depressão

---

## 🎯 Importância das Features (Fatores)

Através da análise de **Permutation Feature Importance**, descobrimos o quanto cada fator contribui para a predição:

### **Como funciona?**
Embaralhamos os valores de uma feature e medimos quanto a performance do modelo piora:
- Se piorar muito = feature muito importante
- Se piorar pouco = feature pouco importante

### **Ranking de Importância**

**🔴 ALTO IMPACTO (>15%)**
1. **Pensamentos Suicidas** (~48.5%) 🚨 CRÍTICO
   - De longe o fator mais importante
   - Indicador direto de risco grave

2. **Pressão Acadêmica** (~26.1%) ⚠️ MUITO ALTO
   - Segundo fator mais relevante
   - Relacionado a estresse e sobrecarga

**🟡 MÉDIO IMPACTO (5-15%)**
3. **Estresse Financeiro** (~11.4%)
   - Preocupações econômicas impactam saúde mental

4. **Idade** (~5.9%)
   - Diferentes faixas etárias têm vulnerabilidades distintas

**🟢 BAIXO IMPACTO (<5%)**
5. Horas de Estudo/Trabalho (~2.4%)
6. Hábitos Alimentares (~2.4%)
7. Satisfação com Estudos (~2.3%)
8. Duração do Sono (~0.6%)
9. Gênero (~0.4%)
10. Histórico Familiar (~0.1%)
11. CR/CGPA (~-0.1%)

### **Insights Importantes**

✅ **Foco em Fatores de Alto Impacto**: Pensamentos suicidas e pressão acadêmica representam mais de 70% da importância total.

✅ **Modelo Não Linear é Essencial**: As interações complexas entre fatores só são capturadas pelo kernel RBF.

✅ **Recall é Prioridade**: Melhor identificar mais casos (incluindo falsos positivos) do que perder casos reais.

⚠️ **Limitação**: O modelo não mostra a direção da influência (positiva ou negativa), apenas a importância.

---

## 💾 Exportação do Modelo

Após o treinamento, o modelo completo (pipeline com pré-processamento + SVM) é salvo:

```python
joblib.dump(svm_pipeline, 'student-depression-svm.joblib')
```

Este arquivo `.joblib` contém:
- O modelo SVM treinado
- O pré-processador (StandardScaler + OneHotEncoder)
- Todos os parâmetros e configurações

**Onde é usado?**
O arquivo é carregado pela API (`student-depression-api`) para fazer predições em tempo real quando usuários respondem o questionário.

---

## 🔬 Tecnologias Utilizadas

| Biblioteca | Versão | Uso |
|------------|--------|-----|
| **scikit-learn** | - | Modelo SVM e pré-processamento |
| **pandas** | - | Manipulação de dados |
| **numpy** | - | Cálculos numéricos |
| **seaborn** | - | Visualização de dados |
| **matplotlib** | - | Gráficos |
| **joblib** | - | Salvar/carregar modelo |
| **kagglehub** | - | Download do dataset |

---

## 📚 Estrutura do Notebook

1. **Setup**: Instalação de dependências
2. **Download Dataset**: Obtém dados do Kaggle
3. **Visualização**: Gráficos exploratórios dos dados
4. **Processamento**: Limpeza e transformação
5. **Treinamento**: Criação do pipeline e treino do SVM
6. **Análise**: Métricas e importância das features
7. **Exportação**: Salvamento do modelo final

---

## 🚀 Como Usar Este Notebook

### **Pré-requisitos**
- Python 3.8+
- Conta no Kaggle (para download do dataset)
- Jupyter Notebook ou Google Colab

### **Executar Localmente**

1. **Instalar dependências**
```bash
pip install kaggle kagglehub pandas scikit-learn seaborn matplotlib joblib
```

2. **Configurar credenciais do Kaggle**
- Baixe seu `kaggle.json` da sua conta
- Coloque em `~/.kaggle/kaggle.json`

3. **Executar o notebook**
```bash
jupyter notebook terappia_model.ipynb
```

### **Executar no Google Colab**
1. Faça upload do notebook para o Colab
2. Execute as células sequencialmente
3. Faça upload do `kaggle.json` quando solicitado

---

## 📊 Resultados Esperados

Após executar o notebook completo, você terá:

✅ Modelo SVM treinado e validado
✅ Análise detalhada da importância de cada feature
✅ Métricas de performance (acurácia e recall)
✅ Arquivo `.joblib` pronto para uso na API
✅ Visualizações dos dados e resultados

---

## 🔄 Integração com o Sistema

```
Notebook (terappia_model.ipynb)
     ↓
[Treina modelo SVM]
     ↓
Exporta: student-depression-svm.joblib
     ↓
Copia para: student-depression-api/src/resources/
     ↓
API carrega modelo
     ↓
Frontend faz requisições
     ↓
Usuários recebem predições
```

---

## 📝 Observações Importantes

⚠️ **Não é Diagnóstico Médico**: Este modelo é uma ferramenta de triagem, não substitui avaliação profissional.

🔒 **Privacidade**: Não armazenamos dados dos usuários. As predições são feitas em tempo real e descartadas.

🎯 **Recall Prioritário**: O modelo é configurado para ser mais sensível (identificar mais casos), aceitando alguns falsos positivos para não perder casos reais.

🔄 **Modelo Estático**: O modelo não aprende com novos dados automaticamente. Necessita retreinamento periódico.

---

## 🤝 Contribuindo

Para melhorar o modelo:
1. Experimente diferentes hiperparâmetros do SVM
2. Teste outros algoritmos para comparação
3. Adicione novas features relevantes
4. Aumente o dataset com mais dados
5. Implemente validação cruzada

---

## 📚 Referências

- [Dataset Original - Kaggle](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)
- [Documentação scikit-learn SVM](https://scikit-learn.org/stable/modules/svm.html)
- [Permutation Feature Importance](https://scikit-learn.org/stable/modules/permutation_importance.html)
