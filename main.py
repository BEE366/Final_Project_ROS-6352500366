#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy

def go_home():
    rospy.wait_for_service('go_home')
    try:
        trigger = rospy.ServiceProxy('go_home', Empty)
        print("Ready do go_home .")
        resp1 = trigger()
        print("go_home Done")
    except rospy.ServiceException as e:
        print("Service (go_home) call failed: %s"%e)

def go_to_kitchen():
    rospy.wait_for_service('go_to_kitchen')
    try:
        trigger = rospy.ServiceProxy('go_to_kitchen', Empty)
        print("Ready do go_to_kitchen .")
        resp1 = trigger()
        print("go_to_kitchen Done")
    except rospy.ServiceException as e:
        print("Service (go_to_kitchen) call failed: %s"%e)

def stop():
    rospy.wait_for_service('stop')
    try:
        trigger = rospy.ServiceProxy('stop', Empty)
        print("Ready do stop .")
        resp1 = trigger()
        print("stop Done")
    except rospy.ServiceException as e:
        print("Service (stop) call failed: %s"%e)

if __name__ == "__main__":
    go_to_kitchen()
    stop()
    go_home()
    stop()