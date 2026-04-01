import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from utils.preprocess import preprocess

print("Carregando dataset...")
df = pd.read_csv("data/dataset_final.csv")

print("Pré-processando textos...")
processed = []

for i, row in df.iterrows():
    processed_text = preprocess(str(row["text"]), row["lang"])
    processed.append(processed_text)

print("Vetorizando...")
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=10000)
X = vectorizer.fit_transform(processed)

y = df["sentiment"]

print("Dividindo treino/teste...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Treinando modelo...")
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

print("Avaliando modelo...")
y_pred = model.predict(X_test)

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

print("Salvando modelo...")
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Treinamento finalizado com sucesso!")