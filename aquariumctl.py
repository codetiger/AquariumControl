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

# Main loop to keep the application alive. 
import time 
from repeatedtimer import RepeatedTimer

controlStates = dict()

def updateCurrentStates():
        global setting
        global controlStates
        for port, obj in controlStates.items():
                controlStates[port]["status"] = False

        for setting in data["controls"]:
                if setting["port"] not in controlStates:
                        controlStates[setting["port"]] = {"name":setting["name"], "status":False}
                controlStates[setting["port"]]["name"] = setting["name"]
                controlStates[setting["port"]]["status"] = controlStates[setting["port"]]["status"] or helper.isTimeBetween(setting["startTime"], setting["endTime"])

updateCurrentStates()

def setControlStates():
        global controlStates
        for port, value in controlStates.items():
                control = controls[port]

                if value["status"]:
                        print("Switching ON the control " + value["name"])
                        control.on()
                else:
                        print("Switching OFF the control " + value["name"])
                        control.off()

def checkControls():
        global controlStates
        print("\nResetting Controls...")
        setControlStates()
        # helper.checkUpdates()
        print("\n")

print("\nstarting...\n")
updateTimer = RepeatedTimer(60, updateCurrentStates)
controlTimer = RepeatedTimer(30, checkControls)

import flask
from flask import request, jsonify, abort, send_from_directory
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__, static_folder='./frontend/webapp/')
app.config["DEBUG"] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/controls', methods=['GET'])
@cross_origin()
def get_control_status():
        return jsonify(controlStates)

@app.route('/api/controls/<int:port>', methods=['PUT'])
@cross_origin()
def update_task(port):
        status = request.json['status']
        if port not in controlStates:
                abort(404)
        if not request.json:
                abort(400)
        if 'status' in request.json and type(request.json['status']) is not bool:
                abort(401)
        
        controlStates[port]["status"] = status
        return jsonify({'done': True, 'obj':controlStates[port]})

app.run(host='0.0.0.0', port=80, debug=False)

# Stop timer
updateTimer.stop()
controlTimer.stop()