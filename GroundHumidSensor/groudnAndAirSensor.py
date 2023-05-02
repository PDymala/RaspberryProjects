from machine import Pin, ADC
from time import sleep
import dht
 
airSensor = dht.DHT11(Pin(16)) 
 # https://microcontrollerslab.com/dht11-dht22-raspberry-pi-pico-micropython-tutorial/
groundSensor = Pin(27,Pin.IN)
groundSensorAdc = ADC(groundSensor)



sleep(2)
 
 
def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    airSensor.measure()
    temp = airSensor.temperature()
    hum = airSensor.humidity()
    print("Air Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))       
    groundSensor_raw = groundSensorAdc.read_u16()
    #checked manualny by puting sensor into water
    # does not work in air, slightely in hands, not in books etc. In ground works fine
    groundSensorFinal = remap(groundSensor_raw,65535,19000,0,100)
    print("Ground humidity: ",groundSensorFinal, "%", sep=" ")
    sleep(2)
