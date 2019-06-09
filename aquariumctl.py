import gpiozero
from datetime import datetime
import json
import time 

def isTimeBetween(startTime, endTime):
        timeNow = datetime.now().time()
        if timeNow >= datetime.strptime(startTime, '%H:%M:%S').time() and timeNow <= datetime.strptime(endTime, '%H:%M:%S').time():
                return True
        else:
                return False

print("Loading & Initialising GPIO controls from config file...")
with open('config.json') as f:
  data = json.load(f)

controls = dict()
controlNames = dict()
for setting in data:
        if setting["port"] not in controls:
                controls[setting["port"]] = gpiozero.DigitalOutputDevice(setting["port"], active_high=setting["activeHigh"], initial_value=False)
                controlNames[setting["port"]] = setting["name"]

while True:
        controlStates = dict()
        for setting in data:
                if setting["port"] not in controlStates:
                        controlStates[setting["port"]] = False
                controlStates[setting["port"]] = controlStates[setting["port"]] or isTimeBetween(setting["startTime"], setting["endTime"])

        for port, value in controlStates.iteritems():
                if value:
                        print("Switching ON the control " + controlNames[port])
                        controls[setting["port"]].on()
                else:
                        print("Switching OFF the control " + controlNames[port])
                        controls[setting["port"]].off()

        print("Sleeping for few seconds...\n")
        time.sleep(10)
