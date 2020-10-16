#!/usr/bin/env python2

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32MultiArray
from ascend_msgs.msg import BPS_thrust
from mavros_msgs.msg import RCIn



def messageCallback(message):
    thrust = RCIn.channels[6]
    BPS_thrust_msg = BPS_thrust(thrust, 1)

if __name__== '__main__':
    
    rospy.init_node('fifthprop')

    pub = rospy.Publisher('thrust', BPS_thrust, queue_size=1)
    
    subscriber = rospy.Subscriber("chatter", RCIn, messageCallback)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        pub.publish(BPS_thrust_msg)
        rate.sleep()



