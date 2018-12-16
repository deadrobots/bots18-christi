import os, sys
from wallaby import *
import constants as c
import actions as a

# great start on the camera code, Christi. You've got a robot that stops when it
# sees red. Now add a few more conditional statements (if-statements) to tell it
# to move left, right, or straight, depending on where the largest red object is
# use get_object_center_x(c.red)   -LMB

#tells you wether it sees red untill you press the right button
def checkForRed():
    while not right_button():
        camera_update()
        print(get_object_count(c.red), get_object_area(c.red, 0))
        msleep(500)




# turns untill it sees red can and then drives to it and grabs it
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
    get_object_count(c.red)
    if get_object_count(c.red)> 0:
        mav(c.motorRight, -300)
        mav(c.motorLeft, 300)
        while get_object_center(c.red, 0).x < 60:
            camera_update()
            print(get_object_center(c.red, 0).x)
        ao()
        msleep(500)
    else:
        pass
    set_servo_position(c.servoClaw, 1064)
    mav(c.motorRight, -300)
    mav(c.motorLeft, -300)
    while get_object_center(c.red, 0).y > 5:
        camera_update()
        print(get_object_center(c.red, 0).y)
    ao()
    msleep(500)
    set_servo_position(c.servoClaw, 1519)

def twistToRed():
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
    get_object_count(c.red)
    if get_object_count(c.red)> 0:
        mav(c.motorRight, -300)
        mav(c.motorLeft, 300)
        while get_object_center(c.red, 0).x < 60:
            camera_update()
            print(get_object_center(c.red, 0).x)
        ao()
        msleep(500)
    else:
        pass


