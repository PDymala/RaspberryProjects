from machine import Pin, ADC
import time

myButton = Pin(28,Pin.IN)
myLed = Pin('LED',Pin.OUT)


adc = ADC(myButton)


while True:
    if myButton.value() == 1:
        myLed.value(1)
        print(adc.read_u16())
    else:
        myLed.value(0)
    time.sleep(0.5)
   