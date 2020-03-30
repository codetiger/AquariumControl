#!/usr/bin/env python3.7
import helper

# Use Mock pins while running in Mac OS or Windows
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
                controls[setting["port"]] = gpiozero.DigitalOutputDevice(setting["port"], active_high=setting["activeHigh"], initial_value=False)


import time 
from repeatedtimer import RepeatedTimer

controlStates = dict()
forcesControlStates = dict()

def updateCurrentStates():
        global data
        global controlStates
        for port, obj in controlStates.items():
                controlStates[port]["status"] = False

        for setting in data["controls"]:
                port = setting["port"]
                if port not in controlStates:
                        controlStates[port] = {"name":setting["name"], "status":False}
                        
                controlStates[port]["name"] = setting["name"]
                controlStates[port]["status"] = controlStates[port]["status"] or helper.isTimeBetween(setting["startTime"], setting["endTime"])

def resetForcedControlStates():
        global controlStates
        global forcesControlStates
        for port, obj in controlStates.items():
                forcesControlStates[port] = controlStates[port]["status"]

updateCurrentStates()
resetForcedControlStates()

def setControlStates():
        global forcesControlStates
        global controlStates
        global controls
        for port, value in controlStates.items():
                control = controls[port]
                status = False
                if value["status"] == forcesControlStates[port]:
                        status = value["status"]
                else:
                        status = forcesControlStates[port]

                if status:
                        print("Switching ON the control " + value["name"])
                        control.on()
                else:
                        print("Switching OFF the control " + value["name"])
                        control.off()

def checkControls():
        print("\nResetting Controls...")
        setControlStates()
        print("\n")

def codeUpdate():
        print("\nUpdating code...")
        helper.checkUpdates()
        print("\n")

print("\nstarting...\n")
updateTimer = RepeatedTimer(5, updateCurrentStates)
controlTimer = RepeatedTimer(5, checkControls)
resetTimer = RepeatedTimer(60, resetForcedControlStates)
updateCodeTimer = RepeatedTimer(60 * 60 * 3, codeUpdate)

import flask
from flask import request, jsonify, abort

app = flask.Flask(__name__, static_folder='frontend/webapp/')
app.config["DEBUG"] = False

@app.route('/api/controls', methods=['GET'])
def get_control_status():
        states = dict()
        for port, value in controlStates.items():
                status = False
                if value["status"] == forcesControlStates[port]:
                        status = value["status"]
                else:
                        status = forcesControlStates[port]
                states[port] = {"name":value["name"], "status":status}

        return jsonify(states)

@app.route('/api/controls/<int:port>', methods=['PUT'])
def update_task(port):
        global forcesControlStates
        status = request.json['status']
        if port not in forcesControlStates:
                abort(404)
        if not request.json:
                abort(400)
        if 'status' in request.json and type(request.json['status']) is not bool:
                abort(401)
        
        forcesControlStates[port] = status
        return jsonify({'done': True, 'obj':forcesControlStates[port]})

app.run(host='0.0.0.0', port=5000, debug=False)

# Stop timers
updateTimer.stop()
controlTimer.stop()
resetTimer.stop()
updateCodeTimer.stop()