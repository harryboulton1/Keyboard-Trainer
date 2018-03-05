import random
from keys import *

chord_types = ["Sus2", "Sus4",
               "Minor Triad", "Major Triad",
               "Diminished Triad", "Augmented Triad",
               "Sixth Chord",
               "Diminished 7th", "Half-Diminished 7th",
               "Minor 7th", "Major 7th",
               "Dominant 7th"]

chord_patterns = {chord_types[0] : (0, 2, 7),
                  chord_types[1] : (0, 5, 7),
                  chord_types[2] : (0, 3, 7),
                  chord_types[3] : (0, 4, 7),
                  chord_types[4] : (0, 3, 6),
                  chord_types[5] : (0, 4, 8),
                  chord_types[6] : (0, 4, 7, 9),
                  chord_types[7] : (0, 3, 6, 9),
                  chord_types[8] : (0, 3, 6, 10),
                  chord_types[9] : (0, 3, 7, 10),
                  chord_types[10]: (0, 4, 7, 11),
                  chord_types[11]: (0, 4, 7, 10)}

class Chord:
    def __init__(self):
        self.type = random.choice(chord_types)
        self.chord_pattern = chord_patterns[self.type]
        self.notes = []
        self.tonic = random.choice(all_notes[:14])
        self.tonic_index = all_notes.index(self.tonic)
        for interval in self.chord_pattern:
            self.notes.append(all_notes[self.tonic_index+interval])
        self.tonicname = self.tonic.name[:len(self.tonic.name)-1]
