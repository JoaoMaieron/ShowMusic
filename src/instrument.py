
class Instrument:
    """
    Class of Instruments, that have an name, sound
    and other instrument properties
    """
    def __init__(self, name, midi_number, note_stream = []):
        self.name = name """ Name of the instrument """
        self.midi_number = midi_number """ Number of the midi correspondent to that instrument """
        self.note_stream = note_stream """ Channel of the instrument """
