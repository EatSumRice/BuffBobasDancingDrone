from re import S
import pygame
import sys
import cv2
import os

class UserStrokeInput:
    def __init__(self, number):
        self.img = None
        self.testimg2 = None
        self.times = number
    def input_image(self):
        for i in range(self.times):
            pygame.init()
            screen = pygame.display.set_mode((100, 100))
            pygame.display.set_caption("Insert Dance Move (Single Straight Line)")
            clickedlist = []
            white_color = pygame.Color(255, 255, 255)
            black_color = pygame.Color(0, 0, 0)
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
                            pygame.draw.rect(screen, black_color, (pos[0], pos[1], 10, 10))
                        except AttributeError:
                            pass
                    if event.type == pygame.MOUSEBUTTONUP:
                        loop = False
                pygame.display.update()
                if(loop == False):
                    pygame.image.save(screen,"line{0}.jpg".format(i))
                    pygame.quit()
                    break
            




inp = UserStrokeInput()
inp.input_image()


# blueColor = (0, 0, 255)
# pygame.display.update() #call everytime