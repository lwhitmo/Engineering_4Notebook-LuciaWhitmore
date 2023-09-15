# The following line is a comment that indicates the type checking tool to ignore this file.
# This can be useful when using tools like mypy for static type checking.

# Import necessary modules
import time  # Provides time-related functions
import board  # Provides access to hardware pins on microcontrollers
import digitalio  # Provides digital input/output capabilities

# Initialize the red LED
redled = digitalio.DigitalInOut(board.GP12)  # Create a DigitalInOut object for the GP12 pin
redled.direction = digitalio.Direction.OUTPUT  # Set the direction of the GP12 pin to OUTPUT

# Initialize the green LED
greenLED = digitalio.DigitalInOut(board.GP19)  # Create a DigitalInOut object for the GP19 pin
greenLED.direction = digitalio.Direction.OUTPUT  # Set the direction of the GP19 pin to OUTPUT

# Countdown loop from 10 to 1
for x in range(10, 0, -1):
    print(x)  # Print the current value of x
    redled.value = True  # Turn on the red LED
    time.sleep(0.5)  # Pause for 0.5 seconds
    redled.value = False  # Turn off the red LED
    time.sleep(0.5)  # Pause for another 0.5 seconds

# After the countdown, print "Liftoff!" and turn on the green LED
print("Liftoff!")
greenLED.value = True  # Turn on the green LED
time.sleep(3)  # Pause for 3 seconds
