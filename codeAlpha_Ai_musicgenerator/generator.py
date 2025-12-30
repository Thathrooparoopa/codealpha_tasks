import numpy as np
from tensorflow.keras.models import load_model
from music21 import note, stream


def generate_music(model_path, output_file):
    model = load_model(model_path)
    pattern = np.random.rand(50, 1)
    output_notes = []

    for _ in range(200):
        prediction = model.predict(pattern.reshape(1, 50, 1), verbose=0)
        index = np.argmax(prediction)
        output_notes.append(index)
        pattern = np.append(pattern[1:], [[index / 128]], axis=0)

    midi_stream = stream.Stream()
    for n in output_notes:
        midi_stream.append(note.Note(int(n)))

    midi_stream.write("midi", output_file)
