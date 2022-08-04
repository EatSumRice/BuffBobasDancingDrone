#!/usr/bin/python3
import queue
from djitellopy import Tello
import numpy as np
import cv2
import pygame
import sys
import time
from drawInputClass import UserStrokeInput
from controlCenter import ControlCenter
from buff_boba_pkg.msg import moves
import rospy
from buff_boba_pkg.msg import numbermoves
from std_msgs.msg import Int32


class drawinputnode:

    def __init__(self):

        rospy.init_node("draw", anonymous = True) 
        #anonymous prevents the error of two nodes same name
        self.number_moves_sub = rospy.Subscriber('tello/numbermoves', Int32, 
                                                self.move_callback)
        self.moves_pub = rospy.Publisher('tello/moves', moves, 
                                            queue_size = 1)
        print('inited')

    def move_callback(self, msg):
        print("got it")
        temp = moves()
        x = ControlCenter(msg.data)
        x.getMoves()
        overall = ""
        for i in x.movesList:
            val = ""
            for component in i:
                val = val + component + ","
            overall = overall + val + " "
        temp.moveList = overall
        self.publish_moves(temp)
    
    def publish_moves(self, thing):
        self.moves_pub.publish(thing)

if __name__ == '__main__':
    listener = drawinputnode()
    while not rospy.is_shutdown():
        rospy.spin()
