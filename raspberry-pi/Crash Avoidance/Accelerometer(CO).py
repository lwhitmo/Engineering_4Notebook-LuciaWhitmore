#type: ignore

# Import necessary libraries
import time  # Provides time-related functions
import board  # Provides access to hardware pins on microcontrollers
import digitalio  # Provides digital input/output capabilities
import adafruit_mpu6050  # Provides access to the MPU6050 sensor
import busio  # Provides support for I2C communication

# Define the pins for I2C communication
sda_pin = board.GP14  # Assign the SDA pin for I2C communication
scl_pin = board.GP15  # Assign the SCL pin for I2C communication

# Initialize the I2C bus using the specified pins
i2c = busio.I2C(scl_pin, sda_pin)

# Create an instance of the MPU6050 sensor using the I2C bus
mpu = adafruit_mpu6050.MPU6050(i2c)

# Infinite loop for continuously reading and processing data
while True:
    # Read acceleration data from the MPU6050 sensor and round the values to 3 decimal places
    x = round(mpu.acceleration[0], 3)
    y = round(mpu.acceleration[1], 3)
    z = round(mpu.acceleration[2], 3)

    # Print the accelerometer data
    print(f" x Acceleration:{x} \n y Acceleration:{y} \n z Acceleration:{z}")
    print("")

    # Pause execution for 1 second
    time.sleep(1)