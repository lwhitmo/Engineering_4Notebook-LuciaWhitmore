#type: ignore

import time
import board # Provides access to hardware pins on microcontrollers
import digitalio 
import adafruit_mpu6050
import busio


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
   
   x = round(mpu.acceleration[0],3)
   y = round(mpu.acceleration[1],3)
   z = round(mpu.acceleration[2],3)

   print(f" x Acceleration:{x} \n y Acceleration:{y} \n z Acceleration:{z}")
   print("")
   
   time.sleep(1)

