from machine import Pin
from time import sleep

LED = Pin(0, Pin.OUT)
PIR_sensor = Pin(14, Pin.IN, Pin.PULL_UP)
LED.low()
sleep(10)

while True:
   print(PIR_sensor.value())
   if PIR_sensor.value() == 0:
       print("Motion Detected! -> LED is now ON")
       LED.high()
       sleep(5)
   else:
       LED.low()
       sleep(1)