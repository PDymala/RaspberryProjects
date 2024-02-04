from lcd1602 import LCD
import utime as time

myLed = machine.Pin('LED',machine.Pin.OUT)
myLed.value(1)

lcd=LCD()
while True:
    
    myName=input('What is Your Name? ')
    lcd.clear()
    greeting1='Hello '+myName
    greeting2='Welcome to My Pi'
    lcd.write(0,0,greeting1)
    lcd.write(0,1,greeting2)
    