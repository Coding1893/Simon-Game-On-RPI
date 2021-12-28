import RPi.GPIO as GPIO

#SETTING UP BOARD
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)

#VARIABLES
red = 18
yellow = 22
green = 24
blue = 26

#SETTING UP LED'S
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, GPIO.LOW)
GPIO.output(yellow, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
GPIO.output(yellow, GPIO.LOW)