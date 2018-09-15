from mido import (
    Message,
    MidiFile,
    MidiTrack,
)


def generate_note_on(**kwargs):
    '''yield note event'''
    return Message('note_on', **kwargs)


def generate_note_off(**kwargs):
    '''yield note off event'''
    return Message('note_off', **kwargs)

