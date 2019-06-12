# TODO Find what RPi returns and change the condition to work on all systems other than RPi
import platform
from gpiozero.pins.mock import MockFactory
from gpiozero import Device
def checkSimulate():
        if platform.system() == "Darwin":
                Device.pin_factory = MockFactory()


# Check if current time is between startTime and endTime
from datetime import datetime
def isTimeBetween(startTime, endTime):
        timeNow = datetime.now().time()
        return (timeNow >= datetime.strptime(startTime, '%H:%M:%S').time() and timeNow <= datetime.strptime(endTime, '%H:%M:%S').time())


# Restarts the current program
import os, sys, psutil, logging
def restartProgram():
        try:
                p = psutil.Process(os.getpid())
                for handler in p.open_files() + p.connections():
                        os.close(handler.fd)
        except Exception, e:
                logging.error(e)

        python = sys.executable
        os.execl(python, python, *sys.argv)


# Check & pull latest code from git
import subprocess
def checkUpdates():
        print("Checking for updated code in git")
        output = subprocess.check_output(["git", "pull"])
        # print("git output: " + output)
        if output != "Already up to date.\n":
                print("Restarting the application...")
                restartProgram()
        print("Completing code update")

