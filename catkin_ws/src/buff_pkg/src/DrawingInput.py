#!/usr/bin/python3

from controlCenter import ControlCenter
import rospy

class DrawingInput(object):

    def __init__(self):

        rospy.init_node("DrawingInput", anonymous = True) 
        #anonymous prevents the error of two nodes same name
        self.number_moves_sub = rospy.Subscriber("tello/numbermoves", int, 
                                                self.publish_moves)
        self.moves_pub = rospy.Publisher('tello/moves', ControlCenter, 
                                            queue_size = 10)

    def publish_moves(self, data):
        
        temp = ControlCenter(data)
        self.moves_pub.publish(temp)

def __main__():
    drawingInput = DrawingInput()
    while not rospy.is_shutdown:


if __name__ == "__main__":
    __main__()