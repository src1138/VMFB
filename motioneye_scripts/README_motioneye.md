GPIO Pins Used
You can use whatever pins you want, but I chose the following as they all default as inputs at boot.
Sensor IR Cntrol (SIRCON)=25 
Dispenser Control (DISCON)=11
PIR Monitor=27
Sensor IR Monitor=17
Timer Monitor=22
Feed Level Monitor=23
Deposit Monitor=24 
Dispense Monitor=10 

/boot/config.txt
Add the following to make your control outputs drive low
gpio=11,25=op,dl

All the scripts go in /data/etc/
- userinit.sh: turns off HDMI and starts logging and camera enable/disable scripts
- VMFB_logger.py: logs the deposit and dispense events
- VMFB_logger.sh: logs PIR, Sensor IR, Timer and Feed Level status and trigger counts
- camera_on-off_schedule: sets the time for the camera to be enabled and disabled to save power
- monitor_1: displays logging and monitoring information on the video overlay
- alarm_on_1 and alarm_off_1: show as action buttons on the web interface to manually start and stop recording
- down_1: show as action buttons on the web interface to manually dispense feed

Config files also go in /data/etc/
- camera-1.conf (camera-1.conf.enable_camera/camera-1.conf.disable_camera): configuration files are overwritten to enable/disable the camera before restarting the motioneye server
- motion.conf (motion.conf.enable_camera/motion.conf.disable_camera): configuration files are overwritten to enable/disable the camera before restarting the motioneye server

Logs will be generated in /data/log/
- VMFB_YYY-MM-DD.log: daily log of events
- userinit.log: logs output from scripts called from userinit.sh
- prev_valPIR, prev_valSIR, prev_valTMR, prev_valEMT: logs the state of the previous execution of the VMFB_logger.sh so only changes will be logged
- 

If you want to specify timed dispense in a script instead of using the 555-based timer, you can try out VMFB_timer.sh.
