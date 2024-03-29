# Turn off HDMI to save ~24mA
/usr/bin/tvservice -o >> /data/log/userinit.log
# Start deposit/dispense logger
nohup /data/etc/VMFB_logger.py >> /data/log/userinit.log &
# Start logger for PIR, Sensor IR, Timer and Empty sensors
nohup /data/etc/VMFB_logger.sh >> /data/log/userinit.log &
# Start the camera on/off scheduler script
nohup /data/etc/camera_on-off_schedule.sh >> /data/log/userinit.log &
# Pause motion detection on startup
curl http://localhost:7999/1/detection/pause >> /data/log/userinit.log
