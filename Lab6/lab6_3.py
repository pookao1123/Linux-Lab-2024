import RPi.GPIO as GPIO
import time 

sw = 22 
Led = 18
State = False
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Led,GPIO.OUT)

try :
    while True :
        if GPIO.wait_for_edge(sw,GPIO.FALLING):
            State = not State
        if(State):
            print("Led => on")
        else :
            print("Led => off")
        GPIO.output(Led,State)
        
        
except KeyboardInterrupt :
    GPIO.cleanup()
print("\nBye........")