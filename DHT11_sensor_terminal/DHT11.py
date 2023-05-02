from machine import Pin
from time import sleep
import dht
 
sensor = dht.DHT11(Pin(16)) 
 # https://microcontrollerslab.com/dht11-dht22-raspberry-pi-pico-micropython-tutorial/

sleep(5)
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(temp)
    print(hum)
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    sleep(2)