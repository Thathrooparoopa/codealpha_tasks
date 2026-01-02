import json
import nltk
import pickle
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# NLTK DOWNLOADS
# -----------------------------
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

# -----------------------------
# PATHS
# -----------------------------
DATA_PATH = os.path.join("data", "hospital_faqs.json")
MODEL_DIR = "models"
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
MATRIX_PATH = os.path.join(MODEL_DIR, "faq_matrix.pkl")

# -----------------------------
# CREATE MODELS FOLDER IF NOT EXISTS
# -----------------------------
os.makedirs(MODEL_DIR, exist_ok=True)

# -----------------------------
# LOAD FAQ DATA
# -----------------------------
with open(DATA_PATH, "r", encoding="utf-8") as f:
    faqs = json.load(f)

questions = [faq["question"] for faq in faqs]

# -----------------------------
# NLP PREPROCESSING
# -----------------------------
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

processed_questions = [preprocess(q) for q in questions]

# -----------------------------
# TRAIN TF-IDF MODEL
# -----------------------------
vectorizer = TfidfVectorizer()
faq_matrix = vectorizer.fit_transform(processed_questions)

# -----------------------------
# SAVE TRAINED MODELS
# -----------------------------
with open(VECTORIZER_PATH, "wb") as f:
    pickle.dump(vectorizer, f)

with open(MATRIX_PATH, "wb") as f:
    pickle.dump(faq_matrix, f)

print("✅ Training completed successfully")
print("📁 Models saved in /models folder")
