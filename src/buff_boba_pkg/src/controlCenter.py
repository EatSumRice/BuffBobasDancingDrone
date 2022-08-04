#!/usr/bin/python3
import pygame
import sys
import cv2
import os
import time
from djitellopy import Tello
import math
from drawInputClass import UserStrokeInput

class ControlCenter:

    def __init__(self, m):
        self.moves = m
        self.movesList = []
    
    def getMoves(self):
        for i in range(self.moves):
            temp = UserStrokeInput()
            temp.input_image()
            move = temp.convertInpToMove() #(y movement, z movement, speed)
            self.movesList.append(move)

    def printMoves(self):
        print(self.movesList)

    # def performMoves(self):
    #     self.drone.takeoff()
    #     for i in self.movesList:
    #         move_type = i[-1]
    #         if(move_type == "line"):
    #             self.drone.go_xyz_speed(0, i[0], i[1], i[2])
    #         elif(move_type == "flip"):
    #             direction = i[0]
    #             if(direction == "right"):
    #                 self.drone.flip_right()
    #             elif(direction == "left"):
    #                 self.drone.flip_left()
    #             elif(direction == "backward"):
    #                 self.drone.flip_back()
    #             else:
    #                 self.drone.flip_forward()

    #         elif(move_type == "curve"):
    #             pos1 = i[0]
    #             pos2 = i[1]
    #             self.drone.curve_xyz_speed(pos1[0], pos1[1], pos1[2], pos2[0], pos2[1], pos2[2], i[2])
    #         elif(move_type == "3d"):
    #             self.drone.go_xyz_speed(0,i[0], 0, i[1])

    #     self.drone.land()


# cc = ControlCenter(1)
# cc.getMoves()
# cc.printMoves()
# cc.performMoves()


