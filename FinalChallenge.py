from djitellopy import Tello
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
from pydub import AudioSegment
import pydub.scipy_effects
from Music_notes_detection import music_notes_detection as md
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import time 

audio_file = AudioSegment.from_file("data/babyShark.wav", "wav")
print(audio_file)
filtered_version = audio_file.low_pass_filter(800, order=4)
filtered_version.export("data/babySharkBass.wav", format='wav')

filename = 'data/babySharkBass.wav'
print(filename)

y, sr = librosa.load(filename)
print('\nsampling rate')
print(sr)
print("\ny")
print(y.shape)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Actual tempo: 115 beats per minute')
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print('Beat frames: ')
print(beat_times)

beat_durations = np.ediff1d(beat_times)


x = 1       # beat counter
for i in beat_durations:
    md.note_detect(y)
    print('beat',x)
    time.sleep(i)       # wait for the beat to pass before printing the next beat to test synchronization with music
    x += 1



