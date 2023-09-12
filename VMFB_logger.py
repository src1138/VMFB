#!/usr/bin/python

# interrupt-based GPIO example using LEDs and pushbuttons

import RPi.GPIO as GPIO
from datetime import datetime
import time
import threading
import re
#import requests

# Initialize RPi GPIO
GPIO.setmode(GPIO.BOARD)

# Set pin numbers (not the same as the GPIO Pin number)
PIR = 13 # G27
SIR = 11 # G17
DEP = 37 # G26
DIS = 38 # G20
TMR = 15 # G22
EMT = 16 # G23

# Configure input pins
GPIO.setup([PIR, SIR, DEP, DIS, TMR, EMT], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# log routines
def logPIR(pin=None):
	PIRtext = "-"
	PIRcount = 0
	monitorText=""
	if (GPIO.input(PIR) == False):
		PIRtext = "+"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	PIR	" + str(GPIO.input(PIR))	+ " " + PIRtext + "\n")

        # Count the lines with PIR and +
 	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "r") as file:
		# Count the lines with PIR and +
		dailyLog = file.read()
		PIRcount = len(re.findall('PIR.*\+',dailyLog))

	# Update motioneye monitor file
	with open("/data/log/VMFB_monitor_text", "r") as file:
		monitorText = file.read()
		monitorText = re.sub('PIR.[0-9]*',"PIR" + PIRtext + str(PIRcount),monitorText)
	with open("/data/log/VMFB_monitor_text", "w") as file:
		file.write(monitorText)

def logSIR(pin=None):
	SIRtext = "-"
	monitorText = ""
	if (GPIO.input(SIR) == False):
		SIRtext = "+"
		# End event and disable motion detection
#		requests.get("http://localhost:7999/1/action/eventend")
#		requests.get("http://localhost:7999/1/detection/pause")
#	else:
		# Enable motion detection and start an event
#		requests.get("http://localhost:7999/1/detection/start")
#		requests.get("http://localhost:7999/1/action/eventstart")
		
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	SIR	" + str(GPIO.input(SIR))	+ " " + SIRtext + "\n")

	# Update motioneye monitor file
	with open("/data/log/VMFB_monitor_text", "r") as file:
		monitorText = file.read()
		monitorText = re.sub('SIR.',"SIR" + SIRtext,monitorText)
	with open("/data/log/VMFB_monitor_text", "w") as file:		
		file.write(monitorText)

def logDEP(pin=None):
	DEPtext = "-"
	DEPcount = 0
	monitorText = ""
	if (GPIO.input(DEP) == False):
		DEPtext = "+"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	DEP	" + str(GPIO.input(DEP))	+ "	" + DEPtext + "\n")

	# Count the lines with DEP and +
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "r") as file:
		dailyLog = file.read()
		DEPcount = len(re.findall('DEP.*\+',dailyLog))

	# Update motioneye monitor file
	with open("/data/log/VMFB_monitor_text", "r") as file:
		monitorText = file.read()
		monitorText = re.sub('DEP.[0-9]*',"DEP" + DEPtext + str(DEPcount),monitorText)
	with open("/data/log/VMFB_monitor_text", "w") as file:
		file.write(monitorText)
        
def logDIS(pin=None):
    	DIStext = "-"
	DIScount = 0
	monitorText = ""
	if (GPIO.input(DIS) == False):
		DIStext = "+"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	DIS " + str(GPIO.input(DIS))	+ " " + DIStext + "\n")

	# Count the lines with DIS and +
        with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "r") as file:
		dailyLog = file.read()
		DIScount = len(re.findall('DIS.*\+',dailyLog))

	# Update motioneye monitor file
	with open("/data/log/VMFB_monitor_text", "r") as file:
		monitorText = file.read()
		monitorText = re.sub('DIS.[0-9]*',"DIS" + DIStext + str(DIScount),monitorText)
	with open("/data/log/VMFB_monitor_text", "w") as file:	
		file.write(monitorText)

def logTMR(pin=None):
	TMRtext = "+"
	if (GPIO.input(TMR) == False):
		TMRtext = "-"
	with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
		file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	TMR " + str(GPIO.input(TMR))	+ " " + TMRtext + "\n")

	# Update motioneye monitor file
	with open("/data/log/VMFB_monitor_text", "r") as file:
		monitorText = file.read()
		monitorText = re.sub('TMR.',"TMR" + TMRtext,monitorText)
	with open("/data/log/VMFB_monitor_text", "w") as file:		
		file.write(monitorText)
		        
def logEMT(pin=None):
	# if the sensors are not on, don't do anything
	if (GPIO.input(SIR) == False):
		EMTtext = "-"
		if (GPIO.input(EMT) == False):
			EMTtext = "+"
		with open("/data/log/VMFB_"+str(datetime.now().strftime("%Y-%m-%d"))+".log", "a+") as file:
			file.write(str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "	EMT " + str(GPIO.input(EMT))	+ " " + EMTtext + "\n")

		# Update motioneye monitor file
		with open("/data/log/VMFB_monitor_text", "r+") as file:
			monitorText = file.read()
			monitorText = re.sub('FEED.',"FEED" + EMTtext,monitorText)
		with open("/data/log/VMFB_monitor_text", "w") as file:
			file.write(monitorText)

# Initialize monitor file
monitorInitialText = "PIR-0000|SIR-|TMR-|FEED-|DEP-0000|DIS-0000"
with open("/data/log/VMFB_monitor_text", "w") as file:
		file.write(monitorInitialText)
logPIR()
logSIR()
logDEP()
logDIS()
logTMR()
logEMT()

# We want to know about falling and rising edges for all sensors and events
GPIO.add_event_detect(PIR, GPIO.BOTH, logPIR)
GPIO.add_event_detect(SIR, GPIO.BOTH, logSIR)
GPIO.add_event_detect(TMR, GPIO.BOTH, logTMR)
GPIO.add_event_detect(EMT, GPIO.BOTH, logEMT)
GPIO.add_event_detect(DEP, GPIO.BOTH, logDEP)
GPIO.add_event_detect(DIS, GPIO.BOTH, logDIS)

while True:
	time.sleep(1e6)
