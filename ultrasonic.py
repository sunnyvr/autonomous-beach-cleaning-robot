import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
TRIG=11
ECHO=13
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while 1:
    GPIO.output(TRIG,0)
    time.sleep(0.1)
    GPIO.output(TRIG,1)
    time.sleep(0.1)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO)==0:
        start=time.time()
    while GPIO.input(ECHO)==1:
        end=time.time()
    T=end-start
    distance=T*17150
    distance=round(distance,2)
    print"distance: ",distance,"cm"

   
