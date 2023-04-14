import RPi.GPIO as GPIO
import time


def blinkLED():
    LEDPin = 18
    t = 0.3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPin, GPIO.OUT)
    for _ in range(10):
        GPIO.output(LEDPin, GPIO.HIGH)
        time.sleep(t)
        GPIO.output(LEDPin, GPIO.LOW)
        time.sleep(t)
    GPIO.cleanup()
