#!/usr/bin/python3

# Relay control based on Dusk/Dawn times 
# Gathered automaticaly via ephem module
# by TJK @ 28/05/2019
# Modified personal version 
# Required Python3 and gpiozero + ephem pip packages
# -- sudo apt install pip 
# -- pip install gpiozero 
# -- pip install ephem --user
# Consider running this as cron job or as a service

# Enjoy

from gpiozero import OutputDevice
import datetime, time
import ephem

K2 = OutputDevice(27, active_high=False)    # Relay 1 connected to GPIO 27

# latitude and longtitude for location could be obtained from google maps 
# (right click in google maps and select 'What's here?')
home_lat  = '52.072628'
home_long = '-1.298129'

# sleep time when between checks
sleepT = 60

# daytime function 
def daytime():
    K2.off()
    # other stuff to be run at daytime
# nighttime function 
def nighttime():
    K2.on()
    # other stuff to be run at night
# sunrise check function 
def sunrise_check():
    o = ephem.Observer()
    o.lat = home_lat
    o.long = home_long
    s = ephem.Sun()
    sunrise = o.next_rising(s)
    sunset = o.next_setting(s)
    # sr_next = ephem.localtime(sunrise) # sunrise time (uncomment for real time control)
    # ss_next = ephem.localtime(sunset) # sunset time (uncomment for real time control)
    # delay added below to keep relay on with 1h longer after sunrise and turn it on 1.5h before sunset
    # mainly used for external light control 
    sr_next = ephem.localtime(sunrise)+datetime.timedelta(hours=1) # 1 hour delay after sunrise (adjust as required)
    ss_next = ephem.localtime(sunset)+datetime.timedelta(hours=-1.5) # 1.5 hour before sunset (adjust as required)

    if sr_next > ss_next:
        day = 1
        return 1
        # print ('day = 1')
    else:
        day = 0
        return 0
        # print ('day = 0')
# return day
    print ('sunrise - ', sr_next)
    print ('sunset  - ', ss_next)
    print ('day value = ', day)

# main 
if __name__ == '__main__':
    try:
        while True:
            print (sunrise_check())
            x = sunrise_check()
            if x == 1:
                daytime()
            else:
                nighttime()
            time.sleep(sleepT)

    except KeyboardInterrupt:
        print ("\n CTRL-C \n --- QUIT --- \n")
        
