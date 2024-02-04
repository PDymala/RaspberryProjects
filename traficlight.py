import time

greenLed = machine.Pin(16,machine.Pin.OUT)
yellowLed = machine.Pin(17,machine.Pin.OUT)
redLed = machine.Pin(18,machine.Pin.OUT)
    
def redLight():
    greenLed.value(0)
    yellowLed.value(0)
    redLed.value(1)
def yellowLight():
    greenLed.value(0)
    yellowLed.value(1)
    redLed.value(0)
def redAndYellowLight():
    greenLed.value(0)
    yellowLed.value(1)
    redLed.value(1)      
    
    
def greenLight():
    greenLed.value(1)
    yellowLed.value(0)
    redLed.value(0)    

while(True):
    
    #RED
    redLight()
    time.sleep(5)
        
    #RED + YELLOW
    redAndYellowLight()
    time.sleep(2)   

    # GREEN
    greenLight()
    time.sleep(5)

    # YELLOW
    yellowLight()
    time.sleep(1)
