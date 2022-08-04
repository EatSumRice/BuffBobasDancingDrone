import queue
from djitellopy import Tello
import numpy as np
import cv2
import pygame
import sys
import time
from drawInputClass import UserStrokeInput
from controlCenter import ControlCenter
from packageName.msg import moves
import rospy


class drawInput:

    def __init__(self):

        rospy.init_node("drawInput", anonymous = True) 
        #anonymous prevents the error of two nodes same name
        self.number_moves_sub = rospy.Subscriber("tello/numbermoves", int, 
                                                self.publish_moves)
        self.moves_pub = rospy.Publisher('tello/moves', moves, 
                                            queue_size = 10)

    def publish_moves(self, data):
        
        temp = moves()
        x = ControlCenter(data)
        overall = ""
        for i in x.movesList:
            val = ""
            for component in i:
                val = val + component + ","
            overall = overall + val + " "
        temp.moveString = overall
        self.moves_pub.publish(temp)