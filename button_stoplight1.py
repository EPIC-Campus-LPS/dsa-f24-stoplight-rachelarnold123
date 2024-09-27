import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON_PIN = 27
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def start():
	if GPIO.input(BUTTON_PIN) == GPIO.LOW:
		GPIO.setup(24,GPIO.OUT)
		print("Green on")
		GPIO.output(24,GPIO.HIGH)
		time.sleep(5)
		print("Green off")
		GPIO.setup(23,GPIO.OUT)
		print("Yellow on")
		GPIO.output(23,GPIO.HIGH)
		time.sleep(1)
		print("Yellow off")
		GPIO.output(24,GPIO.LOW)
		print("Red On")
		time.sleep(4)
		print("Red Off")
		GPIO.output(23,GPIO.LOW)

		
while 1>0:
	if GPIO.input(BUTTON_PIN) == GPIO.LOW:
		start()
