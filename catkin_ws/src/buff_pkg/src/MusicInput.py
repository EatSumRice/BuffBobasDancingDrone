#!/usr/bin/python3

import rospy
import librosa
import librosa.display
import numpy as np
from pygame import mixer
import time
from pathlib import Path
from buff_pkg.msg import Song

class MusicInput(object):

    def __init__(self):
        rospy.init_node("MusicInput", anonymous=True, disable_signals=True)
        self.pub_song = rospy.Publisher('music/song', Song, queue_size = 10)
        print('Enter .wav file:')
        self.file = input()
        self.time_sig = int(input('Enter beats per measure: '))
        self.pickup = input('Pickup beat (y or n): ')

        path = Path().absolute().parent / "FinalProject" / "catkin_ws" / "src" / "buff_pkg" / "data"
        print(path)

        if ".wav" in self.file:
            self.filename = path / self.file
        else:
            self.filename = path / (self.file + '.wav')
        print("running: ",self.filename)

        self.y, self.sr = librosa.load(self.filename)
        print('\nsampling rate')
        print(self.sr)

        self.tempo, self.beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)
        print('Estimated tempo: {:.2f} beats per minute'.format(self.tempo))
        self.round_tempo = int(round(self.tempo, 0))

        self.beat_times = librosa.frames_to_time(self.beat_frames, sr=self.sr)
        print('Beat frames: ')
        print(self.beat_times)

        #TODO publish below 
        self.beat_durations = np.ediff1d(self.beat_times)     # create array of differences between beat frames to get durations

def __main__():
    musicInput = MusicInput()
            
if __name__ == '__main__':
    __main__()


