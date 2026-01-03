# 🎵 AI Music Generator (Flask + LSTM)

An AI-powered music generation web application using **Flask**, **TensorFlow (LSTM)**, and **music21**.

---

## 🚀 Features
- Upload MIDI files
- Train LSTM-based music model
- Generate new music
- Download generated MIDI
- Auto-play generated music
- Dark / Light mode
- Clean, beginner-friendly UI

# Techstack
- Python 3.10+
- Flask
- TensorFlow 2.13
- NumPy 1.24.3
- music21
- HTML, CSS, JavaScript, Bootstrap

---

# Project Structure

ai_music_generator_web/
│
├── app.py
├── model.py
├── trainer.py
├── generator.py
├── midi_processor.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── css/style.css
│ └── js/script.js
│
├── data/midi_files/
├── models/
└── outputs/

# HOW TO RUN THE PROJECT

# 1) Create Virtual Environment
python -m venv venv
venv\Scripts\activate
# 2)Install dependencies
pip install -r requirements.txt
# 3)Run application
python app.py
# 4)Open browser
http://127.0.0.1:5000

---

## 📸 Screenshots

### Home Page
![Home](screenshots/home.png)

### MIDI Upload
![Upload](screenshots/upload.png)

### Model Training
![Training](screenshots/training.png)

### Music Generation
![Generated](screenshots/generated.png)

---

## 🎓 Internship Highlights
- End-to-end AI music generation pipeline
- LSTM-based sequence modeling
- MIDI processing using music21
- Clean Flask backend architecture
- Professional UI/UX with Dark/Light mode
- Proper project documentation
# 📌 Note
Model training may take a few minutes depending on system performance.

👤 Author

Name: THATHROOPA V
Domain: Artificial Intelligence
Internship: CodeAlpha AI Internship Program