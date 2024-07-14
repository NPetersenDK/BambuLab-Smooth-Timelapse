import RPi.GPIO as GPIO
import time
import subprocess

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number to which the sensor is connected
DOOR_SENSOR_PIN = 26

# Setup the GPIO pin as an input
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lastvalue = "Runtime"

try:
    while True:
        # Read the state of the door sensor (HIGH when open, LOW when closed)
        door_state = GPIO.input(DOOR_SENSOR_PIN)

        if door_state == GPIO.HIGH:
            if lastvalue == "closed" or lastvalue == "Runtime":
                print("Printer is out in the OPEN again")
                lastvalue = "open"
        else:
            if lastvalue == "open" or lastvalue == "Runtime":
                print("Printer is at timelapse spot. Taking picture")
                print("- Calling picture script")
                subprocess.call(['sh', './run.sh'])
                print("- Picture taken waiting 3 seconds")
                time.sleep(3)
                print("- Done waiting")
                lastvalue = "closed"

        time.sleep(0.1)  # Add a small delay to avoid excessive reads

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()