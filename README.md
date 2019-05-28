# Relay_control

RPi Relay control python script based on sunset/sunrise times. </br>
Based on ephem python package provided by pyephem - more info https://pypi.org/project/pyephem/ </br>
and gpiozero python package - more info https://pypi.org/project/gpiozero/ </br></br>

### Script uses few python packages:
 - gpiozero -- can be installed via ' pip install gpiozero' (or pip3 dependent on system configuration)
 - ephem -- can be installed via ' pip install ephem ' (or pip3)

After placing the script into permanent location e.g. home folder -
- place relay_control.service into /lib/systemd/system/relay_control.service
and edit 'ExecStart=' to point to correct location 

To enable the service deamon to run:
 - reload systemctrl deamon ' sudo systemctl daemon-reload '
 - enable it to start at boot ' sudo systemctl enable relay_control.service '
 - and start it ' sudo systemctl start relay_control.service '

To check the status of the service run ' sudo systemctl status relay_control.service '
You can also manually start, stop and restart the service via systemctl 
