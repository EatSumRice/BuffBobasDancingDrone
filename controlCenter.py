import pygame
import sys
import cv2
import os
import time
from djitellopy import Tello
import math
from drawInputBetter import UserStrokeInput

class ControlCenter:

    def __init__(self, m):
        self.moves = m
        self.movesList = []
        # self.drone = Tello.connect()
    
    def getMoves(self):
        for i in range(self.moves):
            temp = UserStrokeInput()
            temp.input_image()
            move = temp.convertInpToMove() #(y movement, z movement, speed)
            self.movesList.append(move)

    def printMoves(self):
        print(self.movesList)

    def performMoves(self):
        self.drone.takeoff()
        for i in self.movesList:
            self.drone.go_xyz_speed(0, i[0], i[1], i[2])
        self.drone.land()


cc = ControlCenter(4)
cc.getMoves()
cc.printMoves()


