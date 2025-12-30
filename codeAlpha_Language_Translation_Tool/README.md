🌍 Language Translation Tool

A modern, beginner-friendly Language Translation Tool built using HTML, CSS, JavaScript, and Python Flask.
This project allows users to translate text between multiple languages with a clean UI, dark mode, and additional usability features.

🚀 Developed as part of an AI / Web Development Internship Project to demonstrate full-stack skills.

✨ Features
🌐 Translate text between multiple languages
🔄 Swap source and target languages
🌙 Dark / Light mode toggle
📋 Copy translated text with one click
🔊 Text-to-Speech (TTS) for translated output
⏳ Loading indicator during translation
✅ Toast notification on successful translation
⚠️ Error handling for empty input & network issues
📱 Responsive and clean UI design

🛠️ Tech Stack
Frontend
HTML5
CSS3
JavaScript
Font Awesome Icons
Google Fonts
Backend
Python 3.x
Flask
Flask-CORS
googletrans (Open-source Google Translate API)

📂 Project Folder Structure
language-translation-tool/
│
├── assets/
│   └── background.jpg        # UI background image
│
├── index.html                # Frontend HTML
├── style.css                 # Styling and themes
├── script.js                 # Frontend logic
│
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
│
├── README.md                 # Project documentation

⚙️ Installation & Setup

1️⃣ Clone the Repository
2️⃣ Create Virtual Environment 
python -m venv venv
Activate it:
Windows
venv\Scripts\activate
3️⃣ Install Backend Dependencies
pip install -r requirements.txt
▶️ Running the Project
## Start Flask Backend
python app.py
Backend will run at:
http://127.0.0.1:5000
▶️ Run Frontend
Simply open index.html in your browser

🔌 API Endpoint Details

Translate Text
# Endpoint:
POST /translate
# Request Body (JSON):
{
  "text": "Hello",
  "source": "en",
  "target": "fr"
}
# Response (JSON):
{
  "translatedText": "Bonjour"
}
📸 Screenshots
/screenshots
* light-mode.png
* dark-mode.png
* translation-example.png

👨‍💻 Author

Name:THATHROOPA V
Internship: Artificial Intelligence internship
Purpose: Internship task submission & learning AI basics