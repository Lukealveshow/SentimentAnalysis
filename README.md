# 🔍 Sentiment Analysis App (PT-BR + EN)

Aplicação completa de **Análise de Sentimentos multilíngue** (Português e Inglês), utilizando Machine Learning, API REST e interface web moderna.

---

## 🚀 Demonstração

O sistema permite analisar textos e identificar automaticamente se o sentimento é:

* ✅ Positivo
* ⚖️ Neutro
* ❌ Negativo

Além disso, retorna:

* Idioma detectado (PT ou EN)
* Confiança da predição
* Probabilidades detalhadas por classe

---

## 🧠 Tecnologias Utilizadas

### 🔙 Backend (API + ML)

* Python
* Flask
* Scikit-learn
* spaCy (NLP)
* Pandas
* Langdetect

### 🎨 Frontend

* Angular (Standalone Components)
* TypeScript
* HTML5 + CSS3

---

## 📊 Dataset

O modelo foi treinado com datasets reais:

* 🎬 IMDb Movie Reviews Dataset (Inglês)
* 🛒 B2W Reviews Dataset (Português)

### 🔄 Tratamento dos dados

* Unificação dos datasets
* Conversão de ratings em sentimento
* Limpeza e normalização de texto
* Lematização com spaCy
* Remoção de stopwords

---

## 🤖 Modelo de Machine Learning

* Algoritmo: Logistic Regression
* Vetorização: TF-IDF (unigram + bigram)
* Features: até 10.000
* Divisão: 80% treino / 20% teste

---

## 📈 Resultados do Modelo

```bash
Accuracy: 0.83

Classe      Precision   Recall   F1-score
Negative      0.84       0.86      0.85
Neutral       0.42       0.11      0.18
Positive      0.85       0.93      0.89
```

### 🔎 Análise dos resultados

* 🔥 Excelente performance para **positivo e negativo**
* ⚠️ Classe **neutra é mais difícil**, com baixo recall (11%)
* 📊 Dataset naturalmente desbalanceado impacta o modelo

> 💡 Esse comportamento é comum em problemas reais de NLP — identificar neutralidade é mais complexo do que polaridade.

---

## 🏗️ Arquitetura do Projeto

```bash
backend/
│
├── app.py
├── train.py
├── prepare_data.py
├── requirements.txt
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── utils/
│   ├── preprocess.py
│   └── language.py
│
└── data/
    ├── imdb.csv
    ├── b2w.csv
    └── dataset_final.csv

frontend/
│
└── src/
    ├── app/
    └── assets/
```

---

## ⚙️ Como Executar o Projeto

### 🔧 Backend

```bash
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m spacy download en_core_web_sm
python -m spacy download pt_core_news_sm

python app.py
```

API disponível em:

```
http://localhost:5000
```

---

### 🎨 Frontend

```bash
cd frontend/src

npm install
npm start
```

Acesse:

```
http://localhost:4200
```

---

## 🔗 Endpoint da API

### POST `/predict`

```json
{
  "text": "I love this product!"
}
```

### 📤 Resposta

```json
{
  "text": "I love this product!",
  "language": "en",
  "sentiment": "positive",
  "confidence": 0.92,
  "probabilities": {
    "negative": 0.02,
    "neutral": 0.06,
    "positive": 0.92
  }
}
```

---

## ✨ Funcionalidades

* 🌍 Detecção automática de idioma
* 🧠 NLP com spaCy (lemmatization)
* 📊 Probabilidades por classe
* 🎨 Interface moderna com feedback visual
* ⚡ API rápida com Flask
* 🔄 Integração completa Front + Back

---

## 🧪 Melhorias Futuras

* 📈 Melhorar detecção da classe neutra (balanceamento / tuning)
* 🤖 Testar modelos mais avançados (BERT / Transformers)
* 📊 Dashboard com gráficos (Chart.js)
* 💾 Histórico de análises
* 🌐 Deploy em produção (Render / AWS / Vercel)

---

## 👨‍💻 Autor

Lucas Alves Martins

---

## 📌 Observações

Este projeto foi desenvolvido com foco em:

* Portfólio profissional
* Demonstração de habilidades em Machine Learning
* Integração Full Stack (Angular + Flask)

---

## ⭐ Se gostou do projeto

Deixe uma estrela no repositório e contribua! 🚀
