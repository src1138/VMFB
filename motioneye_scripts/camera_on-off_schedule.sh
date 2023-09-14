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
if [$nowtime >= $ontime]; then
    if [$nowtime <= $offtime]; then
        targetState="1"
    fi
fi

# Get the camera's status
# "0" means it's not active, anything else means it is active
camStatus=$(curl  http://localhost:7999/1/detection/connection | grep -c "Connection OK")

# If the current time is greater than ontime and less than offtime
# the camera should be enabled, else it should be disabled
if [ "$camStatus" == "0" ]; then
    if [ "$targetState" == "1" ]; then
        #enable the camera
        /bin/bash /data/etc/light_on_1
    fi
fi

if [ "$camStatus" != "0" ]; then
    if [ "$targetState" == "0" ]; then
        #disable the camera
        /bin/bash /data/etc/light_off_1
    fi
fi

# Run every 30 minutes
sleep 1800

done
