import RPi.GPIO as GPIO
import time 

sw = 22 
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try :
    while True :
        if GPIO.wait_for_edge(sw,GPIO.FALLING):
            count += 1
            print(f"Buttom pressed {count}")
except KeyboardInterrupt :
    GPIO.cleanup()
print("\nBye........")
