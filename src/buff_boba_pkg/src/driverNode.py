#!/usr/bin/python3
import rospy
from djitellopy import Tello
import time
import numpy as np
from pygame import mixer
from controlCenter import ControlCenter
from buff_boba_pkg.msg import Song
from buff_boba_pkg.msg import moves
from buff_boba_pkg.msg import numbermoves
from std_msgs.msg import Int32
import pygame

class Driver(object):

    def __init__(self):
        rospy.init_node('driver', anonymous=True, disable_signals=True)

        rospy.Subscriber('/music/song', Song, self.data_callback)
        self.received_song = False
        

        ### we need to incorporate moves/state somehow, i'm not too sure how those work ###

    def data_callback(self, msg):
        self.filename = msg.filename
        self.tempo = msg.tempo
        self.beats_per_measure = msg.time_sig
        self.pickup = msg.pickup
        self.beat_durations = msg.beat_durations
        print("Received song info.")
        self.received_song = True

    def getDrawInput(self, number):
        x = ControlCenter(number)
        self.movesList = x.getMoves()
        print(self.movesList)
    

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

        if self.pickup == True:       # adds pickup beat per user input (extra preceding beat before first measure)
            y = self.beats_per_measure
            print('pickup measure')
        elif self.pickup == False:
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

                elif round_tempo > 120:
                    if y % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

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

                elif round_tempo > 120:
                    if x % 3 == 1:
                        print('beat',y,'(',x,') | dance move')
                        #dance move:
                        self.performMove(self.nodeMovesList[self.moveIndex])
                        self.progressIndex()
                    else:
                        print('beat',y,'(',x,')')

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
                
                elif round_tempo > 120:
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
    count = 0
    dr.getDrawInput(5)

    # while not rospy.is_shutdown():
    #     # if(count < 1):
    #     # dr.publish_getMoves(1)
    #         # count+=1
    #     rospy.spin()
            
    # try:
    #     pygame.init()
    #     pygame.display.set_mode((600, 600))

    #     while(True):
    #         for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN:
    #                 #start/end
    #                 if(event.key == pygame.K_1):
    #                     print('1')
    #                     dr.publish_getMoves(1)
                    


    # except rospy.ROSInterruptException:
    #     pass