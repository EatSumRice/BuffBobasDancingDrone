import pygame
import sys
import cv2
import os

class UserStrokeInput:
    def __init__(self):
        self.img = None
        self.testimg2 = None
        self.pos1 = None
        self.pos2 = None
    def input_image(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Insert Dance Move (Single Straight Line)")
        white_color = pygame.Color(255, 255, 255)
        blue_color = pygame.Color(0, 0, 255)
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
                    pygame.draw.line(screen, blue_color, self.pos1, self.pos2, 10)
                    loop = False     
                if loop == True and pygame.mouse.get_pressed()[0]:
                    try:
                        pos = pygame.mouse.get_pos()
                        pygame.draw.rect(screen, blue_color, (pos[0], pos[1], 5, 5))
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

    def getCoords(self):
        return (self.pos1, self.pos2)

    def printImage(self):
        cv2.imshow('grayscale image', self.img)
        cv2.waitKey(1000)



inp = UserStrokeInput()
inp.input_image()
inp.printImage()
print(inp.getCoords())


# blueColor = (0, 0, 255)
# pygame.display.update() #call everytime