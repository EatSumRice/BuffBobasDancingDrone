#!/usr/bin/python3

import rospy
from djitellopy import Tello
import time
import numpy as np
from pygame import mixer
from controlCenter import ControlCenter
from challenges.msg import moves
from challenges.msg import state


class Driver(object):

    def __init__(self):
        rospy.init_node('driver', anonymous=True, disable_signals=True)

        # sorry im terrible at ros so i definitely wrote these subscribers
        # wrong, pretend they work properly
        self.filename_sub = rospy.Subscriber('music/filename', state, self.filename_callback)
        # subscribe to the file path of the song
        self.pickup_sub = rospy.Subscriber('music/pickup', state, self.pickup_callback)
        # subscribe to whether or not there is a pickup beat
        self.tempo_sub = rospy.Subscriber('music/tempo', state, self.tempo_callback)
        # subscribe to the tempo of the song
        self.beatsPerMeasure = rospy.Subscriber('music/beatsPerMeasure', state, self.beatsPerMeasure_callback)
        # subscribe to the number of beats per measure
        self.beatTimes_sub = rospy.Subscriber('music/beatTime', state, self.beatTimes_callback)
        # subscribe to the timestamps of each beat
        self.beatDurations_sub = rospy.Subscriber('music/beatDuration', state, self.beatDuration_callback)
        # subscribe to the durations of each beat
        self.moves_sub = rospy.Subscriber('tello/moves', moves, self.moves_callback())
        

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

    def moves_callback(self, data):
        tempMoveList = data.split(" ")
        self.nodeMovesList = []
        for i in tempMoveList:
            temp = i.split(",")
            self.nodeMovesList.append(temp)


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
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                elif round_tempo <= 120:
                    if y % 2 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                elif round_tempo > 120:
                    if y % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()

            elif self.beats_per_measure == 1:
                if round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                elif round_tempo <= 120:
                    if x % 2 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                elif round_tempo > 120:
                    if x % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()

            elif self.beats_per_measure >= 2:
                if round_tempo <= 60:
                    print('beat',y,'(',x,') | dance move')
                    #dance move:
                    self.performMove(self.nodeMovesList[self.moveIndex])
                    self.progressIndex()
                
                elif round_tempo <= 120:
                    if y % 2 == 1:
                        if self.beats_per_measure % 2 == 1:
                            if y == self.beats_per_measure:
                                print('beat',y,'(',x,')')
                                #dance move:
                                self.performMove(self.nodeMovesList[self.moveIndex])
                                self.progressIndex()
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
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                
                elif round_tempo > 120:
                    if self.beats_per_measure % 3 == 0:
                        if y % 3 == 1:
                            print('beat',y,'(',x,') | dance move')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                        else:
                            print('beat',y,'(',x,')')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                                    

                    elif self.beats_per_measure < 6:
                        if y == 1:
                            print('beat',y,'(',x,') | dance move')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                        else:
                            print('beat',y,'(',x,')')
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()
                    
                    elif self.beats_per_measure > 6:
                        num = self.beats_per_measure // 3     # number of dance moves
                        if y % 3 == 1:
                            if y == ((3 * num) + 1):
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
                            #dance move:
                            self.performMove(self.nodeMovesList[self.moveIndex])
                            self.progressIndex()

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

def __main__():
    driver = Driver()
    driver.execute_dance()
            
if __name__ == '__main__':
    __main__()