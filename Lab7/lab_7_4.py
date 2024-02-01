import drivers
import RPi.GPIO as GPIO
import time

dp = drivers.Lcd()

text = [["Patompong","Thanapak"],["1165104620224","1165104002894"]]
text1 = "LAB 7"
showText = list(text1)
SW1  = 27  
SW2  = 17

n = 0 

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING)  # add rising edge detection on a channel
GPIO.add_event_detect(27, GPIO.FALLING)  #for both buttons



try:
    while True:
        if GPIO.event_detected(27):
            dp.lcd_clear()
            n = not n 
        if GPIO.event_detected(17):
            dp.lcd_clear()
            break

        dp.lcd_display_string(text[0][n],1)
        dp.lcd_display_string(text[1][n],2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye..")
