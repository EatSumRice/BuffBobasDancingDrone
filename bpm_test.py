import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = 'data/potc.wav'
print(filename)

y, sr = librosa.load(filename)
# print('waveform')
# print(y)
print('\nsampling rate')
print(sr)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))