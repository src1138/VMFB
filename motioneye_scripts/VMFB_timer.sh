#!/bin/bash

# Assign pins
SIRCON=25
DISCON=11

# Assumes you want to enable the camera early and disable it late
# To do the opposite, you can swap the $ontime and $offtime variables below

# Set the time you want to enable and disable the camera
ontime="0600" #6:00am
offtime="1800" #6:00pm

# Set pins 11 and 25 to be outputs driving low to avoid them going high on start up.
# Add the following line to your /boot/config.txt
# gpio=11,25=op,dl
 
# Verify they are set up, else initialize them
test -e /sys/class/gpio/gpio$SIRCON ||
  (echo $SIRCON > /sys/class/gpio/export \
   && echo out > /sys/class/gpio/gpio$SIRCON/direction)
test -e /sys/class/gpio/gpio$DISCON ||
  (echo $DISCON > /sys/class/gpio/export \
   && echo out > /sys/class/gpio/gpio$DISCON/direction)

while true
do
# Get the current time's hours and minutes (ex. 1430 for 2:30pm)
nowtime=$(date +%H%M)

# Get the target on/off state
targetState="0"
# Swap $ontime and $offtime to disable early and enable late
if [[ "$nowtime" > "$ontime" ]]; then
    if [[ "$nowtime" < "$offtime" ]]; then
        targetState="1"
    fi
fi
echo "$(date +%F_%X)	$nowtime	$ontime	$offtime"

# Log any values that changed since the last execution
VMFB_logfile="/data/log/VMFB_$(date +%F).log"
touch "$VMFB_logfile"

if [ "$targetState"=="1" ]; then
	echo "$(date +%F_%X)	TMR	1	START">> "$VMFB_logfile"
	# Set the pin to high, wait 1s, then set it back to low
	echo "1">/sys/class/gpio/gpio$SIRCON/value
	echo "1">/sys/class/gpio/gpio$DISCON/value
	sleep 1
	echo "0">/sys/class/gpio/gpio$SIRCON/value
	echo "0">/sys/class/gpio/gpio$DISCON/value
	echo "$(date +%F_%X)	TMR	0	END">> "$VMFB_logfile"
fi

# Trigger timer every hour
sleep 3600

done
