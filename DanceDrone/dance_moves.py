import time
import numpy as np
import cv2
from djitellopy import Tello
import pygame
import sys
 
tello = Tello()
tello.connect()
print("Tello Battery is "+str(tello.get_battery()))

 
class DanceMoves:
 
    def move1(self):
        tello.send_rc_control(0, 0, 50, 100)
        tello.send_rc_control(0, 0, -50, -100)
        print("Move 1 complete!")
 
    def move2(self):
        tello.send_rc_control(0, 20, 50, 70)
        tello.send_rc_control(0, -20, -50, -70)
        print("Move 2 complete!")
 
    def move3(self):
        tello.send_rc_control(-25, 0, 25, 0)
        tello.send_rc_control( 38, 0, 0, 0)
        tello.send_rc_control(-25, 0, -25, 0)
        print("Move 3 complete!")

    def move4(self):
        tello.send_rc_control(50, 50, 50, 0)
        tello.flip_back()
        tello.move_down(50)
        print("Move 4 complete!") 
    
    def move5(self):
        tello.move_up(90)
        tello.move_down(90)
        tello.move_up(40)
        tello.rotate_counter_clockwise(360)
        print("Move 5 complete!") 

    def move6(self):
        tello.move_forward(60)
        tello.flip_back()
        tello.move_up(50)
        tello.move_down(50)
        print("Move 6 complete!") 

    def move7(self):
        tello.send_rc_control(-20, 0, -30, -40)
        tello.send_rc_control(20, 0, 30, -40)
        tello.send_rc_control(-30, 0, 0, 50)
        print("Move 7 complete!") 

    def move8(self):
        tello.flip_right()
        tello.send_rc_control(60, 0, 60, 0)
        tello.flip_right()
        tello.send_rc_control(0, 0, -30, 35)
        print("Move 8 complete!") 

    def move9(self):
        tello.move_up(100)
        tello.move_back(20)
        tello.move_forward(20)
        tello.send_rc_control(0, -40, -60, -30)
        print("Move 9 complete!") 

    def move10(self):
        tello.send_rc_control(0, 50, 100, 90)
        print("Move 10 complete!") 

    move_list = ["",move1(),move2(),move3(),move4(),
    move5(),move6(),move7(),move8(),move9(),move0()]


if __name__ == '__main__':

    dances = DanceMoves()

    tello.takeoff()

    #cv2 commands
    tello.streamon()
    tello.get_frame_read()
    frame_read = tello.get_frame_read()
    img = frame_read.frame
    cv2.imshow('Tello Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        tello.streamoff()

    pygame.init()
    pygame.display.set_mode((400, 500))
            
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
    
            #Different Moves
                if event.key == pygame.K_1:
                    dances.move1()
                                
                elif event.key == pygame.K_2:
                    dances.move2()

                elif event.key == pygame.K_3:
                    dances.move3()

                elif event.key == pygame.K_4:
                    dances.move4()()

                elif event.key == pygame.K_5:
                    dances.move5()

                elif event.key == pygame.K_6:
                    dances.move6()

                elif event.key == pygame.K_7:
                    dances.move7()

                elif event.key == pygame.K_8:
                    dances.move8()

                elif event.key == pygame.K_9:
                    dances.move9()

                elif event.key == pygame.K_0:
                    dances.move10()

            elif event.type == pygame.KEYUP:
                pass


                    # Quit if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    cv2.destroyAllWindows
    tello.land()

