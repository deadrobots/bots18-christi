import os, sys
from wallaby import *
import constants as c
import actions as a

def checkForRed():
    while not right_button():
        camera_update()
        print(get_object_count(c.red), get_object_area(c.red, 0))
        msleep(500)


def scanForRed():
    done = 0
    mav(c.motorLeft, 10)
    mav(c.motorRight, -10)
    while not done:
        camera_update()
        print(get_object_count(c.red), get_object_area(c.red, 0))
        if get_object_count(c.red) > 0 and get_object_area(c.red, 0) > 700:
            mav(c.motorLeft, 0)
            mav(c.motorRight, 0)
            done = 1
        msleep(50)