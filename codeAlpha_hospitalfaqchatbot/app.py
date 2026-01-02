from flask import Flask, render_template, request, jsonify
import json
import pickle
import nltk
import os
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# -----------------------------
# FORCE NLTK DOWNLOADS
# -----------------------------
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)
print("✅ Flask app initialized")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]
    return " ".join(tokens)

# -----------------------------
# LOAD FAQ DATA (SAFE)
# -----------------------------
FAQ_PATH = os.path.join("data", "hospital_faqs.json")

if not os.path.exists(FAQ_PATH):
    raise FileNotFoundError("❌ hospital_faqs.json not found in data/ folder")

with open(FAQ_PATH, "r", encoding="utf-8") as f:
    content = f.read().strip()
    if not content:
        raise ValueError("❌ hospital_faqs.json is EMPTY")
    faqs = json.loads(content)

print("✅ FAQs loaded")

# -----------------------------
# LOAD TRAINED MODEL
# -----------------------------
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/faq_matrix.pkl", "rb") as f:
    faq_matrix = pickle.load(f)

print("✅ Model loaded")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Please type a question 😊"})

    user_input = data["message"].strip()
    if not user_input:
        return jsonify({"reply": "Please enter a valid question 😊"})

    processed_input = preprocess(user_input)
    user_vector = vectorizer.transform([processed_input])
    similarity = cosine_similarity(user_vector, faq_matrix)

    best_idx = similarity.argmax()
    confidence = similarity[0][best_idx]

    if confidence < 0.2:
        return jsonify({
            "reply": "🤔 Sorry, I couldn't find an exact answer. Please try another hospital-related question."
        })

    return jsonify({
        "reply": faqs[best_idx]["answer"]
    })

# START SERVER
# -----------------------------
if __name__ == "__main__":
    print("🚀 Starting Hospital FAQ Chatbot Server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
