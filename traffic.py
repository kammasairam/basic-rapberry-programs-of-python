import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)


while True:
    input_state1 = GPIO.input(16)
    print("switch1 state is ",str(input_state1))
    input_state2 = GPIO.input(18)
    print("switch2 state is ",str(input_state2))
    if (input_state1 == 0):  
       GPIO.output(22, 1)
       GPIO.output(24, 0)
       GPIO.output(26, 0)
       print("green led is on") 
       print("red and white leds are off")
       #time.sleep(5)
       
    elif(input_state2 == 0): 
        GPIO.output(22, 0)
        GPIO.output(24, 1)
        GPIO.output(26, 0)
        print("red led is on") 
        print("green and white leds are off")
        #time.sleep(5)

    else:
        GPIO.output(22, 0)
        GPIO.output(24, 0)
        GPIO.output(26, 1)
        print("white led is on")
        print("red and green leds are off")
        #time.sleep(5)
    time.sleep(1)    
