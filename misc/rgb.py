from time import sleep
from machine import Pin, PWM


myLed = Pin('LED',Pin.OUT)
myLed.value(1)
print('gooo')

redPin = Pin(15,Pin.IN)
greenPin = Pin(14,Pin.IN)
bluePin = Pin(13,Pin.IN)

pwmRed = PWM(redPin)
pwmGreen = PWM(greenPin)
pwmBlue = PWM(bluePin)

pwmRed.freq(1000)
pwmGreen.freq(1000)
pwmBlue.freq(1000)


while True:
    for duty in range(0,65000):
        pwmRed.duty_u16(duty)
        pwmGreen.duty_u16(duty)
        pwmBlue.duty_u16(duty)
        
    for duty in range(0,65000,-1):
        pwmRed.duty_u16(duty)
        pwmGreen.duty_u16(duty)
        pwmBlue.duty_u16(duty)
#65550
