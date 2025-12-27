from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route("/translate", methods=["POST"])
def translate_text():
    try:
        data = request.get_json()

        text = data.get("text")
        source = data.get("source")
        target = data.get("target")

        if not text:
            return jsonify({"error": "Text is empty"}), 400

        # Use googletrans (open-source Google Translate)
        result = translator.translate(
            text,
            src=source,
            dest=target
        )

        return jsonify({"translatedText": result.text})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Translation failed"}), 500


@app.route("/")
def home():
    return "Open-Source Google Translate Backend Running"


if __name__ == "__main__":
    app.run(debug=True)
