#!/usr/bin/python
# I grabbed a can and attached an et and tophat. Next I should make the robot line follow.
import os, sys
from wallaby import *

motorLeft = 3
motorRight = 0
servoArm = 0
servoClaw = 3
tophat = 4
et = 5

# added servo arm. continue makeing code for grabbing can.
def waitForButton():
    print("wait for button.")
    while left_button() == 0:
        pass


# right angles use time 1550
# max speed is 1400
def tickDrive(time, speed1, speed2):
    if (speed1 > 1400):
        print("speed too fast. please pick a number under 1401.")
        speed1 = 1400
    if (speed1 > 1400):
        print("speed too fast. please pick a number under 1401.")
        speed2 = 1400
    mav(motorLeft, speed1)
    mav(motorRight, speed2)
    msleep(time)


def square():
    x = 1
    while x < 5:
        tickDrive(500, 1000, 1000)
        msleep(500)
        tickDrive(1700, -500, 500)
        x = x + 1


def canGrab():
    set_servo_position(servoArm, 1064)
    msleep(500)
    set_servo_position(servoClaw, 591)
    msleep(500)
    tickDrive(2000, -1000, -1000)
    set_servo_position(servoClaw, 1519)


def main():
    enable_servos()
    print("Let's Go")
    waitForButton()
    analog(5)

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
