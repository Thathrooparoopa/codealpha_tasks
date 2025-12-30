from music21 import converter, instrument, note, chord
import os

def process_midi_files(folder_path):
    notes = []

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".mid"):
            file_path = os.path.join(folder_path, file_name)
            midi = converter.parse(file_path)

            parts = instrument.partitionByInstrument(midi)
            elements = parts.parts[0].recurse() if parts else midi.flat.notes

            for element in elements:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append(".".join(str(n) for n in element.normalOrder))

    return notes
