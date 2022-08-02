import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import time

filename = 'data/waltz_in_a.wav'
print(filename)

y, sr = librosa.load(filename)
print('\nsampling rate')
print(sr)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Actual tempo: 115 beats per minute')
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print('Beat frames: ')
print(beat_times)

beat_durations = np.ediff1d(beat_times)     # create array of differences between beat frames to get durations

print('Starting in...')     # countdown so user can try manually syncing the music with the beats
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('GO:')

x = 1       # beat counter
for i in beat_durations:
    print('beat',x)
    time.sleep(i)       # wait for the beat to pass before printing the next beat to test synchronization with music
    x += 1