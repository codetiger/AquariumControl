import gpiozero
from datetime import datetime
import json

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
                controls[setting["port"]] = gpiozero.OutputDevice(setting["port"], active_high=True, initial_value=False)
                controlNames[setting["port"]] = setting["name"]

controlStates = dict()
for setting in data:
        controlStates[setting["port"]] = isTimeBetween(setting["startTime"], setting["endTime"])

for port, value in controlStates.iteritems():
        if value:
                print("Switching ON the control " + controlNames[port])
                controls[setting["port"]].on()
        else:
                print("Switching OFF the control " + controlNames[port])
                controls[setting["port"]].off()
