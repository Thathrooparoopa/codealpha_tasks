🏥 Hospital / Healthcare FAQ Chatbot

A full-screen, interactive Hospital FAQ Chatbot Web Application built using Python (Flask) and Natural Language Processing (NLP) techniques.
The chatbot answers common hospital-related questions using TF-IDF Vectorization and Cosine Similarity, providing fast and accurate responses through a modern ChatGPT-style interface.

📌 Project Overview

This project is developed as part of an internship Task-2 (FAQ Chatbot).
It allows users to ask general hospital and healthcare-related questions, such as OPD timings, emergency services, insurance details, appointments, ICU availability, and hospital facilities.

⚠️ Disclaimer:
This chatbot provides general hospital information only and does not offer medical advice or diagnosis.

🔹 Backend (NLP + Flask)

FAQ-based chatbot using TF-IDF + Cosine Similarity
Text preprocessing with NLTK:
    Lowercasing
    Tokenization
    Stopword removal
    Lemmatization
Trained model reused using Pickle
Graceful fallback for low-confidence matches

🔹 Frontend (UI / UX)

* Full-screen web application (100vw × 100vh)
* Unique medical-themed background
* Modern ChatGPT-style interface
* Emoji support 😊
* Typing indicator (Bot is typing…)
* Auto-suggestions while typing 💡
* Quick-reply FAQ buttons
* Emoji picker 😄
* Dark mode 🌙
 * Mobile-responsive design 📱

| Layer         | Technology                               |
| ------------- | ---------------------------------------- |
| Backend       | Python, Flask                            |
| NLP           | NLTK                                     |
| ML            | Scikit-learn (TF-IDF, Cosine Similarity) |
| Frontend      | HTML, CSS, JavaScript                    |
| Model Storage | Pickle                                   |


📂 Project Structure
hospital_faq_chatbot/
│
├── app.py                  # Flask backend
├── train.py                # Model training script
├── requirements.txt        # Python dependencies
│
├── data/
│   └── hospital_faqs.json  # FAQ dataset (JSON)
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   └── faq_matrix.pkl
│
├── templates/
│   └── index.html          # Frontend HTML
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── README.md
|
|___ screenshots
|

FAQ Dataset

The chatbot is trained on hospital-related FAQs grouped into:
OPD & hospital timings
Emergency services 🚑
Doctor & department availability
Appointment booking & cancellation
Insurance & billing 💳
ICU & facilities 🏥
Pharmacy & diagnostics 🧪
Patient support services

⚙️ Installation & Setup

1️⃣ Clone or Download Project
git clone <repository-url>
cd codeAlpha_hospitalfaqchatbot
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
📥 Download NLTK Data 
Run the following once:
bash:
   python

python:
 import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
exit()

🧠 Train the Model
python train.py

After training, the models/ folder will contain:
tfidf_vectorizer.pkl
faq_matrix.pkl

▶️ Run the Application
python app.py

Open browser and go to:
http://127.0.0.1:5000


screenshots

autosuggestions.png
darkmode.png
faqchatbot.png
homepage.png


🧪 Sample Questions
What are OPD timings?
Is emergency service available 24/7?
How can I book an appointment?
Do you accept insurance?
Is ICU available?
Is pharmacy open 24 hours?

🔮 Future Enhancements

Voice input & text-to-speech
Admin panel to manage FAQs
Database integration
AI-powered intent detection

👤 Author

Name: THATHROOPA V
Domain: Artificial Intelligence
Internship: CodeAlpha AI Internship Program