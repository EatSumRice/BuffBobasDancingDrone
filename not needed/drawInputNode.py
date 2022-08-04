import queue
from djitellopy import Tello
import numpy as np
import cv2
import pygame
import sys
import time
from controlCenter import ControlCenter
import rospy



class drawInput:

    def __init__(self):

        rospy.init_node("drawInput", anonymous = True) 
        #anonymous prevents the error of two nodes same name
        self.number_moves_sub = rospy.Subscriber("tello/numbermoves", int, 
                                                self.publish_moves)
        self.moves_pub = rospy.Publisher('tello/moves', ControlCenter, 
                                            queue_size = 10)

    def publish_moves(self, data):
        
        temp = ControlCenter(data)
        self.moves_pub.publish(temp)