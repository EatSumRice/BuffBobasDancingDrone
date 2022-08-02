import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = 'data/baby_shark.wav'
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