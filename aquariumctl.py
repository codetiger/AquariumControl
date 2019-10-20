#!/usr/bin/env python3.7
import helper

# Use Mock pins while running in Mac OS
helper.checkSimulate()

# Load the configuration data
import json
print("Loading & Initialising GPIO controls from config file...")
with open('config.json') as f:
        data = json.load(f)


# Building all GPIOZero controls using configuration loaded from config file
import gpiozero
controls = dict()
for setting in data["controls"]:
        if setting["port"] not in controls:
                controls[setting["port"]] = gpiozero.DigitalOutputDevice(setting["port"], active_high=setting["activeHigh"], initial_value=False), setting["name"]

# Main loop to keep the application alive. 
import time 
while True:
        controlStates = dict()
        for setting in data["controls"]:
                if setting["port"] not in controlStates:
                        controlStates[setting["port"]] = False
                controlStates[setting["port"]] = controlStates[setting["port"]] or helper.isTimeBetween(setting["startTime"], setting["endTime"])

        for port, value in controlStates.items():
                control, name = controls[port]
                if value:
                        print("Switching ON the control " + name)
                        control.on()
                else:
                        print("Switching OFF the control " + name)
                        control.off()

        helper.checkUpdates()

        print("Sleeping for few seconds...\n")
        time.sleep(30)