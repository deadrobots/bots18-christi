#!/usr/bin/python
# I grabbed a can and attached an et and tophat. Next I should make the robot line follow.
import os, sys
from wallaby import *
import constants as c
import actions as a

# Great code overall! -LMB
# Looks like you made some progress with your hardware this week. Looking forward to seeing more code, too! -LMB


def main():
    enable_servos()
    a.waitForButton()
    print("hello!")
    a.gyroLoop()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
