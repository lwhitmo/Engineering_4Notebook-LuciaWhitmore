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
   y = (mpu.acceleration[1])
   z = (mpu.accelertaion[2])

   print()

   time.sleep(1)

