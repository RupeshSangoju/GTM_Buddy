from flask import Flask, request, jsonify
import joblib
import numpy as np
from entity_extraction import extract_entities
import nltk
from nltk.tokenize import sent_tokenize

# Load NLTK resources (first-time setup)
nltk.download('punkt')

app = Flask(__name__)

# Load trained model and vectorizer
classifier = joblib.load("models/classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def generate_summary(text, num_sentences=1):
    """ Generate a simple summary by extracting key sentences """
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])  # Return first sentence(s)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "NLP API is running! Use /predict for predictions."})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided!"}), 400

    # Extract entities
    entities = extract_entities(text)

    # Predict labels
    X_input = vectorizer.transform([text]).toarray()
    predicted_labels = classifier.predict(X_input)[0]

    # Convert predicted labels to readable format
    label_names = ["Objection", "Pricing Discussion", "Security", "Competition"]
    final_labels = [label_names[i] for i, val in enumerate(predicted_labels) if val == 1]

    # Generate summary (1-2 sentences)
    summary = generate_summary(text, num_sentences=2)

    response = {
        "predicted_labels": final_labels,
        "extracted_entities": entities,
        "summary": summary
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
