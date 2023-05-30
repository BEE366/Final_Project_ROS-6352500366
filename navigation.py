#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def go_home(req):
    rospy.loginfo("Going to home.")
    time.sleep(2)
    rospy.loginfo("Arrived home")
    return EmptyResponse()

def go_to_kitchen(req):
    rospy.loginfo("Going to kitchen.")
    time.sleep(2)
    rospy.loginfo("Arrived kitchen")
    return EmptyResponse()

def stop(req):
    rospy.loginfo("stop.")
    return EmptyResponse()

def trigger_server():
    rospy.init_node('trigger_server')

    GH = rospy.Service('/go_home', Empty, go_home)
    GK = rospy.Service('/go_to_kitchen', Empty, go_to_kitchen)
    ST = rospy.Service('/stop', Empty, stop)

    rospy.spin()

if __name__ == "__main__":
    trigger_server()
