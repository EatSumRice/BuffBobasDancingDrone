import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from pygame import mixer
import time

print('Enter .wav file:')
file = input('data/')
time_sig = int(input('Enter beats per measure: '))
pickup = input('Pickup beat (y or n): ')


if ".wav" in file:
    filename = 'data/' + file
else:
    filename = 'data/' + file + '.wav'
print("running: ",filename)

y, sr = librosa.load(filename)
print('\nsampling rate')
print(sr)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
round_tempo = int(round(tempo, 0))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print('Beat frames: ')
print(beat_times)

beat_durations = np.ediff1d(beat_times)     # create array of differences between beat frames to get durations

#### EVEYRTHING ABOVE IS PREPROCESSING



#### EVERYTHING BELOW IS FOR EXECUTION (music player and executing commands to the beat)

mixer.init()        # initialize audio player
mixer.music.load(filename)
mixer.music.set_volume(0.1)


print('Rounded tempo:',round_tempo,'beats per minute')
print('Starting playback:')     # countdown so user can try manually syncing the music with the beats

mixer.music.play()

x = 1       # beat counter for whole song
y = 1       # beat counter for measure
m = 1       # measure counter
# time.sleep(beat_durations[0])   # buffer in order to improve synchronicity 

if pickup == 'y':       # adds pickup beat per user input (extra preceding beat before first measure)
    y = time_sig
    print('pickup measure')
elif pickup == 'n':
    pass

for i in beat_durations:        # records every measure change and every beat on time (can be subbed with real events)
    if y == 1:
        print('measure',m)

    if time_sig == 0:
        if round_tempo <= 60:
            print('beat',y,'(',x,') | dance move')
        elif round_tempo <= 120:
            if y % 2 == 1:
                print('beat',y,'(',x,') | dance move')
            else:
                print('beat',y,'(',x,')')
        elif round_tempo > 120:
            if y % 3 == 1:
                print('beat',y,'(',x,') | dance move')
            else:
                print('beat',y,'(',x,')')

    elif time_sig == 1:
        if round_tempo <= 60:
            print('beat',y,'(',x,') | dance move')
        elif round_tempo <= 120:
            if x % 2 == 1:
                print('beat',y,'(',x,') | dance move')
            else:
                print('beat',y,'(',x,')')
        elif round_tempo > 120:
            if x % 3 == 1:
                print('beat',y,'(',x,') | dance move')
            else:
                print('beat',y,'(',x,')')

    elif time_sig >= 2:
        if round_tempo <= 60:
            print('beat',y,'(',x,') | dance move')
        
        elif round_tempo <= 120:
            if y % 2 == 1:
                if time_sig % 2 == 1:
                    if y == time_sig:
                        print('beat',y,'(',x,')')
                    else:
                        print('beat',y,'(',x,') | dance move')
                else:
                    print('beat',y,'(',x,') | dance move')
            else:
                print('beat',y,'(',x,')')
        
        elif round_tempo > 120:
            if time_sig % 3 == 0:
                if y % 3 == 1:
                    print('beat',y,'(',x,') | dance move')
                else:
                    print('beat',y,'(',x,')')

            elif time_sig < 6:
                if y == 1:
                    print('beat',y,'(',x,') | dance move')
                else:
                    print('beat',y,'(',x,')')
            
            elif time_sig > 6:
                num = time_sig // 3     # number of dance moves
                if y % 3 == 1:
                    if y == ((3 * num) + 1):
                        print('beat',y,'(',x,')')
                    else:
                        print('beat',y,'(',x,') | dance move')
                else:
                    print('beat',y,'(',x,')')

    x += 1
    if y == time_sig:
        y = 1
        m += 1
    else:
        y += 1
    time.sleep(i)       # wait for the beat to pass before printing the next beat to test synchronization with music