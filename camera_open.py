import RPi.GPIO as GPIO
import time,os,serial,cv2
import numpy as np
import cv2 as cv



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)




cap=cv2.VideoCapture(0)
print cap.isOpened()
if cap.isOpened()==False:
    cap=cv2.VideoCapture(1)
    print cap.isOpened()
    

try:
    while(1):

            ret,img_frame =cap.read()
            
            cv2.imshow('output',img_frame)
            

            k=cv2.waitKey(10)
            #cheking for an esc key press
            if k==27:
                break

        
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()

