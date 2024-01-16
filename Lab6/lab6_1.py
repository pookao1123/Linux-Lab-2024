import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)


while True :
  GPIO.output (LED, True)
  time.sleep(0.1)
  GPIO.output(LED, False)
  time.sleep(1) 
