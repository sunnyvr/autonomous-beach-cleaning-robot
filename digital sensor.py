import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)

while 1:
    if GPIO.input(40)==1:
        print"Detected"
        
        time.sleep(1)
    else:
        print"Not Detected"
        
        time.sleep(1)
