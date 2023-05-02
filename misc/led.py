from machine import Pin
import time

myLed = Pin(0,Pin.OUT)

while True:
    myLed.value(1)
    time.sleep(1)
    myLed.value(0)
    time.sleep(1)