import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(24,gpio.OUT)
gpio.setup(23,gpio.OUT)
while True:
    gpio.output(24,1)
    print("led1 is on")
    gpio.output(23,1)
    print("led2 is on")
    time.sleep(1)
    gpio.output(24,0)
    print("led1 is off")
    gpio.output(23,0)
    print("led2 is off")
    time.sleep(1)
