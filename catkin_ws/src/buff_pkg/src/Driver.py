#!/usr/bin/python3

import rospy
from djitellopy import Tello
import time
import numpy as np
from pygame import mixer

class Driver(object):

    def __init__(self):
        rospy.init_node('driver', anonymous=True, disable_signals=True)

        # sorry im terrible at ros so i definitely wrote these subscribers
        # wrong, pretend they work properly
        self.filename_sub = rospy.Subscriber('music/filename', notsure, self.filename_callback)
        # subscribe to the file path of the song
        self.pickup_sub = rospy.Subscriber('music/pickup', notsure, self.pickup_callback)
        # subscribe to whether or not there is a pickup beat
        self.tempo_sub = rospy.Subscriber('music/tempo', notsure, self.tempo_callback)
        # subscribe to the tempo of the song
        self.beatsPerMeasure = rospy.Subscriber('music/beatsPerMeasure', notsure, self.beatsPerMeasure_callback)
        # subscribe to the number of beats per measure
        self.beatTimes_sub = rospy.Subscriber('music/beatTime', notsure, self.beatTimes_callback)
        # subscribe to the timestamps of each beat
        self.beatDurations_sub = rospy.Subscriber('music/beatDuration', notsure, self.beatDuration_callback)
        # subscribe to the durations of each beat
        

        # alex, make sure u subscribe to stuff from draw input so it can 
        # receive the list of moves

    def filename_callback(self, data):
        self.filename = data        # listen to music input node, store file path of song
    
    def pickup_callback(self, data):
        self.pickup = data          # listen to music input node, store whether or not there is pickup
    
    def tempo_callback(self, data):
        self.tempo = data           # listen to music input node, store tempo

    def beatsPerMeasure_callback(self, data):
        self.beats_per_measure = data # listen to music input node, store number of beats per measure
    
    def beatTimes_callback(self, data):
        self.beat_times = data        # listen to music input node, store beat times array
    
    def beatDurations_callback(self, data):
        self.beat_durations = data    # listen to music input node, store beat durations array

    

    def execute_dance(self):
    
        mixer.init()        # initialize audio player
        mixer.music.load()
        mixer.music.set_volume(0.1)
        round_tempo = int(round(self.tempo, 0))

        print('Rounded tempo:',round_tempo,'beats per minute')
        print('Starting playback:')     # countdown so user can try manually syncing the music with the beats

        mixer.music.play()

        x = 1       # beat counter for whole song
        y = 1       # beat counter for measure
        m = 1       # measure counter
        # time.sleep(beat_durations[0])   # buffer in order to improve synchronicity 

        if self.pickup == 'y':       # adds pickup beat per user input (extra preceding beat before first measure)
            y = self.beats_per_measure
            print('pickup measure')
        elif self.pickup == 'n':
            pass

        for i in self.beat_durations:        # records every measure change and every beat on time (can be subbed with real events)
            if y == 1:
                print('measure',m)

            if self.beats_per_measure == 0:
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

            elif self.beats_per_measure == 1:
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

            elif self.beats_per_measure >= 2:
                if round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                
                elif round_tempo <= 120:
                    if y % 2 == 1:
                        if self.beats_per_measure % 2 == 1:
                            if y == self.beats_per_measure:
                                print('beat',y,'(',x,')')
                            else:
                                print('beat',y,'(',x,') | dance move')
                        else:
                            print('beat',y,'(',x,') | dance move')
                    else:
                        print('beat',y,'(',x,')')
                
                elif round_tempo > 120:
                    if self.beats_per_measure % 3 == 0:
                        if y % 3 == 1:
                            print('beat',y,'(',x,') | dance move')
                        else:
                            print('beat',y,'(',x,')')

                    elif self.beats_per_measure < 6:
                        if y == 1:
                            print('beat',y,'(',x,') | dance move')
                        else:
                            print('beat',y,'(',x,')')
                    
                    elif self.beats_per_measure > 6:
                        num = self.beats_per_measure // 3     # number of dance moves
                        if y % 3 == 1:
                            if y == ((3 * num) + 1):
                                print('beat',y,'(',x,')')
                            else:
                                print('beat',y,'(',x,') | dance move')
                        else:
                            print('beat',y,'(',x,')')

            x += 1
            if y == self.beats_per_measure:
                y = 1
                m += 1
            else:
                y += 1
            time.sleep(i)       # wait for the beat to pass before printing the next beat to test synchronization with 

def __main__():
    driver = Driver()
    driver.execute_dance()
            
if __name__ == '__main__':
    __main__()