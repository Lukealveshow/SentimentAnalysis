from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from utils.preprocess import preprocess
from utils.language import detect_language

app = Flask(__name__)
CORS(app)

print("Carregando modelo...")
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return {"message": "API de Análise de Sentimentos está rodando!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Texto não fornecido"}), 400

    text = data["text"]

    lang = detect_language(text)
    processed = preprocess(text, lang)

    vectorized = vectorizer.transform([processed])

    prediction = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]

    return jsonify({
        "text": text,
        "language": lang,
        "sentiment": prediction,
        "confidence": float(max(probabilities)),
        "probabilities": {
            "negative": float(probabilities[0]),
            "neutral": float(probabilities[1]) if len(probabilities) > 2 else 0,
            "positive": float(probabilities[-1])
        }
    })

if __name__ == "__main__":
    app.run(debug=True)