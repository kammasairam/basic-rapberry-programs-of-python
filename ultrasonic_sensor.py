import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM) #16,28
trigpin = 25
echopin = 1
gpio.setup(trigpin,gpio.OUT)
gpio.setup(echopin,gpio.IN)

print("calculating distance")

while(True):
    gpio.output(trigpin,0)
    time.sleep(2)
    gpio.output(trigpin,1)
    time.sleep(0.00001)
    gpio.output(trigpin,0)

    while(gpio.input(echopin)==0):
        start_time = time.time()
    while(gpio.input(echopin)==1):
        stop_time = time.time()
    duration = stop_time - start_time
    distance = (34000*duration)/2
    if(distance>0) and (distance<400):
        print("obstacle is at a distance : ",str(distance))
    else:
        print("out of range")
