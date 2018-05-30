from mido import MidiFile, Message, MidiTrack

TUNINGS = {
    'EADGBE': [('E', 4), ('B', 3), ('G', 3), ('D', 3), ('A', 2), ('E', 2)]
}

NOTE_MAP = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
}


def note2midi(note, octave):
    '''C_{-1} = 0'''
    return (octave + 1) * 12 + NOTE_MAP[note]


def tuning_to_notes(tuning):
    return [note2midi(*t) for t in tuning]


def tab2midi(string, fret, tuning='EADGBE'):
    '''get midinote from fretboard guitar

    Watch out: string is base-1'''
    if type(tuning) == str:
        tuning = TUNINGS[tuning]
    return note2midi(*tuning[string - 1]) + fret

