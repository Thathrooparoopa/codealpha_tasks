from flask import Flask, render_template, request, jsonify, send_file
import os
from midi_processor import process_midi_files

from trainer import train_model
from generator import generate_music

app = Flask(__name__)

UPLOAD_FOLDER = "data/midi_files"
MODEL_PATH = "models/music_model.h5"
OUTPUT_FILE = "outputs/generated_music.mid"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_midi():
    files = request.files.getlist("midi_files")
    if not files:
        return jsonify({"error": "No MIDI files uploaded"}), 400

    for file in files:
        if file.filename.endswith(".mid"):
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return jsonify({"message": "MIDI files uploaded successfully"})


@app.route("/train", methods=["POST"])
def train():
    notes = process_midi_files(UPLOAD_FOLDER)
    if not notes:
        return jsonify({"error": "No MIDI data found"}), 400

    train_model(notes, MODEL_PATH)
    return jsonify({"message": "Model trained successfully"})


@app.route("/generate", methods=["POST"])
def generate():
    if not os.path.exists(MODEL_PATH):
        return jsonify({"error": "Model not trained yet"}), 400

    generate_music(MODEL_PATH, OUTPUT_FILE)
    return jsonify({"message": "Music generated successfully"})


@app.route("/download")
def download():
    if not os.path.exists(OUTPUT_FILE):
        return jsonify({"error": "No generated file found"}), 400

    return send_file(OUTPUT_FILE, as_attachment=True)


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
