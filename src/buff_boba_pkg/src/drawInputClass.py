#!/usr/bin/python3
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
        self.mode = "line"
    def input_image(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 600))
        pygame.display.set_caption("Insert Dance Move (Single Straight Line)")
        white_color = pygame.Color(255, 255, 255)
        blue_color = pygame.Color(0, 0, 255)
        black_color = pygame.Color(0, 0, 0)
        
        screen.fill(white_color)
        self.initButtons(screen)
    
        pygame.display.update()
        loop = True
        temppos1 = None
        temppos2 = None
        while(loop):
            pos = None
            for event in pygame.event.get():   
                if loop == True and event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if(pos[0] > 15 and pos[0] < 65 and pos[1] > 540 and pos[1] < 590):
                            self.mode = "line"
                            print(self.mode)
                        elif(pos[0] > 75 and pos[0] < 125 and pos[1] > 540 and pos[1] < 590):
                            self.mode = "flip"
                            print(self.mode)                            
                        elif(pos[0] > 135 and pos[0] < 215 and pos[1] > 540 and pos[1] < 590):
                            self.mode = "3d"
                            print(self.mode)
                        elif(pos[0] > 225 and pos[0] < 300 and pos[1] > 540 and pos[1] < 590):
                            self.mode = "curve"
                            print(self.mode)
                        elif(pos[0] > 310 and pos[0] < 385 and pos[1] > 540 and pos[1] < 590):
                            screen.fill(white_color)
                            self.initButtons(screen)
                        elif(pos[0] > 415 and pos[0] < 490 and pos[1] > 540 and pos[1] < 590):
                            loop = False
                        else:
                            self.pos1 = pos

                if loop == True and event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if(pos[1] < 540):
                        self.pos2 = pos 

                if loop == True and pygame.mouse.get_pressed()[0]:
                    try:
                        pos = pygame.mouse.get_pos()
                        pygame.draw.rect(screen, black_color, (pos[0], pos[1], 10, 10))
                    except AttributeError:
                        pass
                        
                        

            pygame.display.update()
            if(loop == False):
                # pygame.image.save(screen,"screenshot.jpg")
                # self.img = cv2.imread('screenshot.jpg', 0)
                # time.sleep(3)
                pygame.quit()
                break

    def initButtons(self, screen):

        font = pygame.font.Font('freesansbold.ttf', 16)
        white_color = pygame.Color(255, 255, 255)
        blue_color = pygame.Color(0, 0, 255)
        black_color = pygame.Color(0, 0, 0)
        pygame.draw.line(screen, black_color, (0, 530), (500, 530), 3)
        pygame.draw.rect(screen, (100, 255, 0),(15,540,50,50))
        text = font.render('Linear', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (40, 565)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, (150, 255, 0),(75,540,50,50))
        text = font.render('Flip', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (100, 565)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, (200, 255, 0),(135,540,80,50))
        text = font.render('3D Move', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (175, 565)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, (250, 255, 0),(225,540,75,50))
        text = font.render('Curve', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (260, 565)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, (0, 255, 100),(310,540,75,50))
        text = font.render('Clear', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (340, 565)
        screen.blit(text, textRect)
        pygame.draw.rect(screen, (255, 0, 0),(415,540,75,50))
        text = font.render('Submit', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (450, 565)
        screen.blit(text, textRect)

    def getImage(self):
        return self.img

    def getCoords(self):
        return (self.pos1, self.pos2, self.mode)

    def printImage(self):
        cv2.imshow('grayscale image', self.img)
        cv2.waitKey(1000)

    def convertInpToMove(self):
        if(self.mode == "line"):
            x1 = self.pos1[0]
            y1 = 600 - self.pos1[1]
            x2 = self.pos2[0]
            y2 = 600 - self.pos2[1]
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
        
            return (x_dir * int(abs(x_movement)), y_dir * int(abs(y_movement)), int(speed), self.mode)
        elif(self.mode == "flip"):
            x1 = self.pos1[0]
            y1 = 600 - self.pos1[1]
            x2 = self.pos2[0]
            y2 = 600 - self.pos2[1]
            x_movement = self.distscalar * (x2 - x1)
            y_movement = self.distscalar * (y2 - y1)
            #cm/s

            direction = ""
            if(abs(y_movement) > abs(x_movement)):
                if(y_movement > 0):
                    direction = "backward"
                else:
                    direction = "forward"
            else:
                if(x_movement > 0):
                    direction = "right"
                else:
                    direction = "left"

            return (direction, self.mode)
        elif(self.mode == "3d"):
            y1 = 600 - self.pos1[1]
            y2 = 600 - self.pos2[1]
            y_movement = self.distscalar * (y2 - y1)

            dist = abs(y_movement)
            if(y_movement > 0):
                val = -1 * abs(y_movement)
                speed = dist/self.timeConst
            else:
                val = abs(y_movement)
                speed = dist/self.timeConst
            
            return (int(val), int(speed), self.mode)
        else:
            x1 = self.pos1[0]
            y1 = 600 - self.pos1[1]
            x2 = self.pos2[0]
            y2 = 600 - self.pos2[1]
            x_movement = self.distscalar * (x2 - x1)
            y_movement = self.distscalar * (y2 - y1)

            x_dir = -1 if x_movement < 0 else 1
            y_dir = -1 if y_movement < 0 else 1

            if(abs(x_movement) < 50):
                x_movement = 50
            if(abs(y_movement) < 50):
                y_movement = 50

            radiusx = x_movement/2
            radiusy = y_movement/2
            #cm/s
            dist = math.sqrt((x_movement-20)**2 + (y_movement-20)**2)
            speed = 60
            # velx = x_movement/self.timeConst
            # vely = y_movement/self.timeConst
            

            peakCurve = math.sqrt(radiusx**2 + radiusy**2)

        
            return (((x_dir * 50), y_dir * 50, 0), (x_dir * 50 * 2, 0, 0), int(speed), self.mode)



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
