from machine import Pin, ADC
import time

sensor = Pin(28,Pin.IN)
myLed = Pin('LED',Pin.OUT)
conversion_factor = 3.3 / (65535)



myLed.value(1)
sensor_temp = ADC(sensor)



while True:
  #  if myButton.value() == 1:
       
    temp_voltage_raw = sensor_temp.read_u16()
    convert_voltage = temp_voltage_raw*conversion_factor
    tempC = convert_voltage/(10.0 / 1000)
    print("Temperature: ",tempC, "°C", sep=" ")
    time.sleep(2)
   
