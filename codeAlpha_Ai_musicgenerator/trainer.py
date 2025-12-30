import numpy as np
from tensorflow.keras.utils import to_categorical
from model import create_model

def train_model(notes, model_path):
    sequence_length = 50

    unique_notes = sorted(set(notes))
    note_to_int = {note: number for number, note in enumerate(unique_notes)}

    network_input = []
    network_output = []

    for i in range(len(notes) - sequence_length):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]

        network_input.append([note_to_int[n] for n in sequence_in])
        network_output.append(note_to_int[sequence_out])

    X = np.reshape(
        network_input,
        (len(network_input), sequence_length, 1)
    )
    X = X / float(len(unique_notes))

    y = to_categorical(network_output)

    model = create_model(
        input_shape=(X.shape[1], X.shape[2]),
        output_units=y.shape[1]
    )

    model.fit(X, y, epochs=30, batch_size=64)
    model.save(model_path)
