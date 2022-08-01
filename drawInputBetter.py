import pygame
import sys
import cv2
import os
import time
from djitellopy import Tello
import math

class UserStrokeInput:
    def __init__(self):
        self.img = None
        self.testimg2 = None
        self.pos1 = None
        self.pos2 = None
        self.distscalar = .056
        self.timeConst = .4

    def input_image(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Insert Dance Move (Single Straight Line)")
        white_color = pygame.Color(255, 255, 255)
        blue_color = pygame.Color(0, 0, 255)
        black_color = pygame.Color(0, 0, 0)
        screen.fill(white_color)
        loop = True
        self.pos1 = None
        self.pos2 = None
        while(loop):
            pos = None
            for event in pygame.event.get():
                if loop == True and event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos1 = pygame.mouse.get_pos()
                if loop == True and event.type == pygame.MOUSEBUTTONUP:
                    self.pos2 = pygame.mouse.get_pos()
                    pygame.draw.line(screen, black_color, self.pos1, self.pos2, 10)
                    loop = False     
                if loop == True and pygame.mouse.get_pressed()[0]:
                    try:
                        pos = pygame.mouse.get_pos()
                        pygame.draw.rect(screen, blue_color, (pos[0], pos[1], 5, 5))
                    except AttributeError:
                        pass
            pygame.display.update()
            if(loop == False):
                # pygame.image.save(screen,"screenshot.jpg")
                # self.img = cv2.imread('screenshot.jpg', 0)
                # time.sleep(3)
                pygame.quit()
                break
            

    def getImage(self):
        return self.img

    def getCoords(self):
        return (self.pos1, self.pos2)

    def printImage(self):
        cv2.imshow('grayscale image', self.img)
        cv2.waitKey(1000)

    def convertInpToMove(self):
        x1 = self.pos1[0]
        y1 = 500 - self.pos1[1]
        x2 = self.pos2[0]
        y2 = 500 - self.pos2[1]
        x_movement = self.distscalar * (x2 - x1)
        y_movement = self.distscalar * (y2 - y1)
        #cm/s
        dist = math.sqrt(x_movement**2 + y_movement**2)
        speed = dist/self.timeConst
        # velx = x_movement/self.timeConst
        # vely = y_movement/self.timeConst
        
        x_dir = -1 if x_movement < 0 else 1
        y_dir = -1 if y_movement < 0 else 1

        if(abs(x_movement) < 20):
            x_movement = 20
        if(abs(y_movement) < 20):
            y_movement = 20
    
        return (x_dir * int(x_movement), y_dir * int(y_movement), int(speed))


    def setScalar(self, input):
        self.scalar = input

    def setTime(self, input):
        self.timeConst = input


# inp = UserStrokeInput()
# inp.input_image()
# print(inp.getCoords())
# vals = inp.convertInpToMove()
# print(vals)
# drone = Tello()
# drone.connect()
# drone.takeoff()
# # drone.send_rc_control(vals[0], 0, vals[1], 0)
# # time.sleep(inp.timeConst)
# # drone.send_rc_control(0, 0, 0, 0)
# drone.go_xyz_speed(0, vals[0], vals[1], vals[2])
# drone.land()
