#!/usr/bin/python
# I grabbed a can and attached an et and tophat. Next I should make the robot line follow.
import os, sys
from wallaby import *
import constants as c
# added servo arm. continue makeing code for grabbing can.
def waitForButton():
    print("wait for button.")
    while left_button() == 0:
        pass


# right angles use time 1550
# max speed is 1400
def tickDrive(time, speed1, speed2):
    if (speed1 > 1400): # My printed documentation is incorrect (my bad). But IF-statements don't need parentheses. Please remove unnecessary parentheses -LMB
        print("speed too fast. please pick a number under 1401.")
        speed1 = 1400
    if (speed1 > 1400): # You are checking for "edge-cases" here. This is solid coding. Well done! - LMB
        print("speed too fast. please pick a number under 1401.")
        speed2 = 1400
    mav(c.motorLeft, speed1)
    mav(c.motorRight, speed2)
    msleep(time)


def square():
    x = 1
    while x < 5:
        tickDrive(500, 1000, 1000)
        msleep(500)
        tickDrive(1700, -500, 500)
        x = x + 1

def lineFollow():
   set_servo_position(c.servoClaw, 512)
   while analog(c.et) < 2300:
        if (analog(c.tophat) > 2000):
            mav(c.motorLeft, -1400)
            mav(c.motorRight, 0)
        else:
            mav(c.motorLeft, 0)
            mav(c.motorRight, -1400)
   tickDrive(300,-800,-100)
   tickDrive(800,-900,-900)
   set_servo_position(c.servoClaw, 1519)


def etDrive ():
   while analog(c.et) < 2900:
       print(analog(c.et))
       mav(c.motorLeft, -500)
       mav(c.motorRight, -500)



def canGrab():
    set_servo_position(c.servoArm, 1064) # Unless you are using named constants for the servo positions, please put a comment explaining whether the arm is moving up, or down, or where... -LMB
    msleep(500)
    set_servo_position(c.servoClaw, 591)
    msleep(500)
    tickDrive(2000, -1000, -1000)
    set_servo_position(c.servoClaw, 1519)
