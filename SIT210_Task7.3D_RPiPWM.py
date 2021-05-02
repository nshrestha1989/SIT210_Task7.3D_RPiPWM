
import RPi.GPIO as GPIO
import time
 
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_BUZZ=23

GPIO.setmode(GPIO.BCM)
 

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_BUZZ,GPIO.OUT)

pwm_buzz=GPIO.PWM(GPIO_BUZZ,1000)#set frequency to 1khz

pwm_buzz.start(0)#set dutycyle to 0

def distance():
    
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        timeStarted = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        timeStoped = time.time()
 
    # time difference between start and arrival
    TimeElapsed = timeStoped - timeStarted

    distance = (TimeElapsed * 34300) / 2
 
    return distance
 

try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            
            if (dist < 50):
                pwm_buzz.ChangeFrequency(1000 - dist*10)
                pwm_buzz.ChangeDutyCycle(10)
                
                time.sleep(1)
            else :
                pwm_buzz.ChangeDutyCycle(0)    
                
        time.sleep(1)
 	    
                 
                         # Reset by pressing CTRL + C
except KeyboardInterrupt:
      print("Measurement stopped by User")
      GPIO.cleanup()

