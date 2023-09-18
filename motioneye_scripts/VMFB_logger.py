#!/usr/bin/python

# interrupt-based GPIO logging for deposit and dispense sensors

import RPi.GPIO as GPIO
from datetime import datetime
import time
import threading

# Initialize RPi GPIO
GPIO.setmode(GPIO.BOARD)

# Set pin numbers (not the same as the GPIO Pin number)
DEP = 18 # G24
DIS = 19 # G10

# Configure input pins
GPIO.setup([DEP, DIS], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# logging and monitoring routines
def logDEP(pin=None):
	DEPtext = "-"
	if (GPIO.input(DEP) == False):
		DEPtext = "+"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	DEP	" + str(GPIO.input(DEP))	+ "	" + DEPtext + "\n")
        
def logDIS(pin=None):
    	DIStext = "-"
	if (GPIO.input(DIS) == False):
		DIStext = "+"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	DIS " + str(GPIO.input(DIS))	+ " " + DIStext + "\n")

# We want to know about falling and rising edges for deposit and dispense
GPIO.add_event_detect(DEP, GPIO.BOTH, logDEP)
GPIO.add_event_detect(DIS, GPIO.BOTH, logDIS)

while True:
	time.sleep(1e6)
