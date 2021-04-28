import numpy as np
import matplotlib.pyplot as pl
import wave
import struct
import pyaudio
import GUI

DEFAULT_NOTE = 44100
# interval_list
G3 = 196    # Sor(3)
C4 = 261    # Do
C4_2 = 277  # Do#
D4 = 293    # Re
D4_2 = 311  # Re#
E4 = 330    # Mi
F4 = 349    # Fa
F4_2 = 370  # Fa#
G4 = 392    # Sor
G4_2 = 415  # Sor#
A4 = 440    # Ra
A4_2 = 466  # Ra#
B4 = 494    # Si
C5 = 523    # Do


def whole_note(interval) :
    sec = 2
    note_hz = interval
    sample_hz = DEFAULT_NOTE
    t = np.arange(0, sample_hz * sec)
    wv = np.sin(2 * np.pi * note_hz * t/sample_hz)
    return wv

def half_note(interval) :
    sec = 1
    note_hz = interval
    sample_hz = DEFAULT_NOTE
    t = np.arange(0, sample_hz * sec)
    wv = np.sin(2 * np.pi * note_hz * t/sample_hz)
    return wv

def quarter_note(interval) :
    sec = 0.5
    note_hz = interval
    sample_hz = DEFAULT_NOTE
    t = np.arange(0, sample_hz * sec)
    wv = np.sin(2 * np.pi * note_hz * t/sample_hz)
    return wv

def eighth_note(interval) :
    sec = 0.25
    note_hz = interval
    sample_hz = DEFAULT_NOTE
    t = np.arange(0, sample_hz * sec)
    wv = np.sin(2 * np.pi * note_hz * t/sample_hz)
    return wv

def sixteenth_note(interval) :
    sec = 0.125
    note_hz = interval
    sample_hz = DEFAULT_NOTE
    t = np.arange(0, sample_hz * sec)
    wv = np.sin(2 * np.pi * note_hz * t/sample_hz)
    return wv

def make_binary(wv) :
    max_num = 32767.0 / max(wv)
    wv16 = [int(x * max_num) for x in wv]
    bi_wv = struct.pack("h" * len(wv16), *wv16)
    return bi_wv


def main() :
    wv1 = quarter_note(C4)
    wv2 = quarter_note(G3)
    wv3 = half_note(D4)
    wv4 = eighth_note(G4)
    wv5 = half_note(E4)
    wv6 = half_note(C4)
    wv7 = eighth_note(G4)
    wv8 = whole_note(F4_2)

    bi_wv1 = make_binary(wv1)
    bi_wv2 = make_binary(wv2)
    bi_wv3 = make_binary(wv3)
    bi_wv4 = make_binary(wv4)
    bi_wv5 = make_binary(wv5)
    bi_wv6 = make_binary(wv6)
    bi_wv7 = make_binary(wv7)
    bi_wv8 = make_binary(wv8)

    bi_wv = bi_wv1 + bi_wv2 + bi_wv3 + bi_wv4 + bi_wv5 + bi_wv6 + bi_wv7 + bi_wv8
    file = wave.open("./sample.wav", mode = "wb")
    param = (1, 2, DEFAULT_NOTE, len(bi_wv), "NONE", "not compressed")
    file.setparams(param)
    file.writeframes(bi_wv)
    file.close

if __name__ == "__main__" :
    main()