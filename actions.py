#!/usr/bin/python
#Try threshold value for gyroLoop absolute value of 200
import os, sys
from wallaby import *
import constants as c
import camera as m
# added servo arm. continue makeing code for grabbing can.
def waitForButton():
    print("wait for button.")
    while left_button() == 0:
        pass


# right angles use time 1550
# max speed is 1400
def tickDrive(time, speed1, speed2):
    if speed1 > 1400:
        print("speed too fast. please pick a number under 1401.")
        speed1 = 1400
    if (speed1 > 1400): # You are checking for "edge-cases" here. This is solid coding. Well done! - LMB
        print("speed too fast. please pick a number under 1401.")
        speed2 = 1400
    mav(c.motorLeft, speed1)
    mav(c.motorRight, speed2)
    msleep(time)

#drives in a square
def square():
    x = 1
    while x < 5:
        tickDrive(500, 1000, 1000)
        msleep(500)
        tickDrive(1700, -500, 500)
        x = x + 1

# makes the robot line follow
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

# drives untill the can is a certain distance away
def etDrive (distance):
    while analog(c.et) < distance:
       mav(c.motorLeft, -500)
       mav(c.motorRight, -500)
       print(analog(c.et))


#drives to can then grabs it
def canGrab():
    set_servo_position(c.servoArm, 1064) #lowers arm to good grabbing position
    msleep(500)
    set_servo_position(c.servoClaw, 591) # opens claw to good grabbing position
    msleep(500)
    tickDrive(2000, -1000, -1000)
    set_servo_position(c.servoClaw, 1519) # good position for hoding the can

#if youput the robot in a corner it will drive into the wall then
# turn and drive into the other wall and keep on going back and forth
def gyroLoop():
    gy = 0
    while gy < 3 :
        while gyro_y() < 200:
            print(gyro_y())
            mav(c.motorRight,-1300)
            mav(c.motorLeft,-1300)
        if gy == 1:
           tickDrive(1000,1300,1300)
           tickDrive(1600,-500,500) 
        else:
            tickDrive(1000,1300,1300)
            tickDrive(1600,500,-500)
        gy = gy + 1

def swatCan():
    set_servo_position(c.servoClaw, 600)
    m.twistToRed()
    etDrive(2100)
    msleep(500)
    set_servo_position(c.servoClaw, 1650)
