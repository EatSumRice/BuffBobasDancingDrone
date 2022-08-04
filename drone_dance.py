import queue
import cv2
import pygame
from djitellopy import Tello
from control_center import ControlCenter
from draw_input import UserStrokeInput

import librosa
import librosa.display
from pygame import mixer

import sys
import time
import numpy as np
import matplotlib.pyplot as plt

### Music Input Processing ###

class MusicInput(object):

    def __init__(self):

        print('Enter .wav file:')
        file = input('data/')

        time_sig = int(input('Enter beats per measure: '))
        while time_sig < 0:
            time_sig = int(input('Invalid input, please re-enter (above 0): '))

        pickup = input('Pickup beat (y or n): ')
        while (pickup != 'y') and (pickup != 'n'):
            pickup = input('Invalid input, please re-enter (y or n): ')
        if pickup == 'y':
            pickup = True
        elif pickup == 'n':
            pickup = False
            

        if ".wav" in file:
            filename = 'data/' + file
        else:
            filename = 'data/' + file + '.wav'
        print("\nRunning: ",filename)

        y, sr = librosa.load(filename)

        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
        self.round_tempo = int(round(tempo, 0))

        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        self.beat_durations = np.ediff1d(beat_times)     # create array of differences between beat frames to get durations
    
    def song_init(self):
        self.filename = str(self.filename)
        self.tempo = self.tempo
        self.time_sig = self.time_sig
        self.pickup = self.pickup

### Dance Execution

class Driver(object):
    
    def get_draw_input(self, number):       # get moves list from drawing input
        x = ControlCenter(number)
        self.movesList = x.getMoves()
        print(self.movesList)

    def execute_dance(self):
        mixer.init()        # initialize audio player
        mixer.music.load(self.filename)
        mixer.music.set_volume(0.1)

        print('Rounded tempo:',self.round_tempo,'beats per minute')
        print('\nStarting playback:\n')     # countdown so user can try manually syncing the music with the beats

        mixer.music.play()

        x = 1       # beat counter for whole song
        y = 1       # beat counter for measure
        m = 1       # measure counter
        # time.sleep(beat_durations[0])   # buffer in order to improve synchronicity 

        if self.pickup == True:       # adds pickup beat per user input (extra preceding beat before first measure)
            y = self.beats_per_measure
            print('pickup measure')
        elif self.pickup == False:
            pass

        for i in self.beat_durations:        # records every measure change and every beat on time (can be subbed with real events)
            if y == 1:
                print('measure',m)

            if self.beats_per_measure == 0:
                if self.round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                elif self.round_tempo <= 120:
                    if y % 2 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

                elif self.round_tempo > 120:
                    if y % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

            elif self.beats_per_measure == 1:
                if self.round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                elif self.round_tempo <= 120:
                    if x % 2 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

                elif self.round_tempo > 120:
                    if x % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

            elif self.beats_per_measure >= 2:
                if self.round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                
                elif self.ound_tempo <= 120:
                    if y % 2 == 1:
                        if self.beats_per_measure % 2 == 1:
                            if y == self.beats_per_measure:
                                print('beat',y,'(',x,')')

                            else:
                                print('beat',y,'(',x,') | dance move')
                                #dance move:
                                self.performMove(self.nodeMovesList[self.moveIndex])
                                self.progressIndex()
                        else:
                            print('beat',y,'(',x,') | dance move')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')
                
                elif self.round_tempo > 120:
                    if self.beats_per_measure % 3 == 0:
                        if y % 3 == 1:
                            print('beat',y,'(',x,') | dance move')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                        else:
                            print('beat',y,'(',x,')')

                    elif self.beats_per_measure < 6:
                        if y == 1:
                            print('beat',y,'(',x,') | dance move')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                        else:
                            print('beat',y,'(',x,')')

                    elif self.beats_per_measure > 6:
                        num = self.beats_per_measure // 3     # number of dance moves
                        if y % 3 == 1:
                            if y == ((3 * num) + 1):
                                print('beat',y,'(',x,')')
                            else:
                                print('beat',y,'(',x,') | dance move')
                                #dance move:
                                self.performMove(self.nodeMovesList[self.moveIndex])
                                self.progressIndex()
                        else:
                            print('beat',y,'(',x,')')

            x += 1
            if y == self.beats_per_measure:
                y = 1
                m += 1
            else:
                y += 1
            time.sleep(i)       # wait for the beat to pass before printing the next beat to test synchronization with 

    def performMove(self, move):

        move_type = move[-1]
        if(move_type == "line"):
            self.drone.go_xyz_speed(0, move[0], move[1], move[2])
        elif(move_type == "flip"):
            direction = move[0]
            if(direction == "right"):
                self.drone.flip_right()
            elif(direction == "left"):
                self.drone.flip_left()
            elif(direction == "backward"):
                self.drone.flip_back()
            else:
                self.drone.flip_forward()
        elif(move_type == "curve"):
            pos1 = move[0]
            pos2 = move[1]
            self.drone.curve_xyz_speed(pos1[0], pos1[1], pos1[2], pos2[0], pos2[1], pos2[2], move[2])
        elif(move_type == "3d"):
            self.drone.go_xyz_speed(0,move[0], 0, move[1])

    def progressIndex(self):
        self.moveIndex += 1
        if(self.moveIndex >= len(self.nodeMovesList)):
            self.moveIndex = 0

    
if __name__ == '__main__':
    dr = Driver()
    # driver.execute_dance()
    # print("1 here")
    # musicInput = MusicInput()
    # musicInput.song_pub()
    count = 0
    dr.get_draw_input(5)