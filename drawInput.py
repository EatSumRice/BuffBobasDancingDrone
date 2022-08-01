import pygame
import sys
import cv2
import os

class UserStrokeInput:
    def __init__(self):
        self.img = None
        self.testimg2 = None
    
    def input_image(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Insert Dance Move (Single Straight Line)")
        clickedlist = []
        white_color = pygame.Color(255, 255, 255)
        blue_color = pygame.Color(0, 0, 255)
        screen.fill(white_color)
        loop = True
        while(loop):
            pos = None
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    loop = False
                if loop == True and pygame.mouse.get_pressed()[0]:
                    try:
                        pos = pygame.mouse.get_pos()
                        clickedlist.append(pos)
                        pygame.draw.rect(screen, blue_color, (pos[0], pos[1], 10, 10))
                    except AttributeError:
                        pass
            pygame.display.update()
            if(loop == False):
                pygame.image.save(screen,"screenshot.jpg")
                self.img = cv2.imread('screenshot.jpg', 0)
                pygame.quit()
                break
            

    def getImage(self):
        return self.img

    def printImage(self):
        cv2.imshow('grayscale image', self.img)
        cv2.waitKey(1000)



inp = UserStrokeInput()
inp.input_image()
inp.printImage()


# blueColor = (0, 0, 255)
# pygame.display.update() #call everytime