import RPi.GPIO as GPIO
import time 

sw = 22 
R = 18
G = 14
B = 15

RState = False
GState = False
BState = False


State = 0


GPIO.setmode(GPIO.BCM)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)



try :
    while True :
        if GPIO.wait_for_edge(sw,GPIO.FALLING):
            State += 1 
        if (State % 7 == 0) :
            print("Led => off")
            RState = False
            GState = False
            BState = False
        elif (State % 7 == 1):
            print("Led => Blue")
            RState = False
            GState = False
            BState = True
        elif (State % 7 == 2):
            print("Led => Green")
            RState = False
            GState = True
            BState = False
        elif (State % 7 == 3):
            print("Led => Cyan")
            RState = False
            GState = True
            BState = True
        elif (State % 7 == 4):
            print("Led => Red")
            RState = True
            GState = False
            BState = False
        elif (State % 7 == 5):
            print("Led => Magenta")
            RState = True
            GState = False
            BState = True
        elif (State % 7 == 6):
            print("Led => Yellow")
            RState = True
            GState = True
            BState = False
        elif (State % 7 == 7):
            print("Led => White")
            RState = True
            GState = True
            BState = True
        GPIO.output(R,RState)
        GPIO.output(G,GState)
        GPIO.output(B,BState)
        
except KeyboardInterrupt :
    GPIO.cleanup()
print("\nBye........")