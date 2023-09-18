#!/bin/bash

# Assumes you want to enable the camera early and disable it late
# To do the opposite, you can swap the $ontime and $offtime variables below

# Set the time you want to enable and disable the camera
ontime="0600" #6:00am
offtime="1800" #6:00pm

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

# Get the camera's status
# "0" means it's not active, anything else means it is active
camStatus=$(curl  http://localhost:7999/1/detection/connection 2>&1 | grep -c "Connection OK")

# If the current time is greater than ontime and less than offtime
# the camera should be enabled, else it should be disabled
if [ "$camStatus" == "0" ]; then
    echo "$(date +%F_%X)	Camera is disabled"	
    if [ "$targetState" == "1" ]; then
        #enable the camera
        # swap the camera config file and restart motion and the motioneye server
	echo "$(date +%F_%X)	Enabling camera"
	cp /data/etc/camera-1.conf.enable_camera /data/etc/camera-1.conf
	cp /data/etc/motion.conf.enable_camera /data/etc/motion.conf
	#curl  http://localhost:7999/1/action/restart
	#curl  http://localhost:7999/1/detection/pause
	meyectl stopserver -b -c /data/etc/motioneye.conf
	meyectl startserver -b -c /data/etc/motioneye.conf
        echo "$(date +%F_%X)	Camera enabled"
    fi
fi

if [ "$camStatus" != "0" ]; then
    echo "$(date +%F_%X)	Camera is enabled"
    if [ "$targetState" == "0" ]; then
        #disable the camera
	# swap the camera config file and restart motion and the motioneye server
	echo "$(date +%F_%X)	Disabling camera"
	cp /data/etc/camera-1.conf.disable_camera /data/etc/camera-1.conf
	cp /data/etc/motion.conf.disable_camera /data/etc/motion.conf
	#curl  http://localhost:7999/1/action/restart
	meyectl stopserver -b -c /data/etc/motioneye.conf
	meyectl startserver -b -c data/etc/motioneye.conf
        echo "$(date +%F_%X)	Camera disabled"
    fi
fi

# Run every 15 minutes
sleep 900

done
