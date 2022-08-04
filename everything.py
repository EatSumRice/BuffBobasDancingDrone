import librosa
import librosa.display
import numpy as np
from pygame import mixer
import time
from pathlib import Path
from controlCenter import ControlCenter
from drawInputBetter import UserStrokeInput

class MusicInput(object):

    def __init__(self):

            print('Enter .wav file:')
            self.file = input()
            self.time_sig = int(input('Enter beats per measure: '))
            self.pickup_str = input('Pickup beat (y or n): ')
            if self.pickup_str == "y":
                self.pickup = True
            else:
                self.pickup = False


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

    def song_init(self):
        self.filename = str(self.filename)
        self.tempo = self.tempo
        self.time_sig = self.time_sig
        self.pickup = self.pickup
        print("published")

class Driver(object):

    def __init__(self):
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
    # musicInput = MusicInput()
    # musicInput.song_pub()
    count = 0
    dr.getDrawInput(5)