# Turn off HDMI to save ~24mA
/usr/bin/tvservice -o >> /data/log/userinit.log
# Start deposit/dispense logger
nohup /data/etc/VMFB_logger.py >> /data/log/userinit.log &
