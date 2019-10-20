import sys
print(len(sys.argv))

if len(sys.argv) > 2:
    port = int(sys.argv[1])
    state = int(sys.argv[2])
    print("Port : " + str(port))

    import gpiozero
    control = gpiozero.DigitalOutputDevice(port, active_high=False, initial_value=False)

    if state:
        control.blink()
        print("Switching on")
    else:
        control.off()
        print("Switching off")
else:
    print("python testport.py [port] [state]")

import time
time.sleep(5)