# The following line is a comment that indicates the type checking tool to ignore this file.
#type: ignore
# This can be useful when using tools like mypy for static type checking.

# Import necessary modules
import time  # Provides time-related functions
import board  # Provides access to hardware pins on microcontrollers
import digitalio  # Provides digital input/output capabilities

# Initialize the red LED
redled = digitalio.DigitalInOut(board.LED)  # Create a DigitalInOut object for the built-in LED
redled.direction = digitalio.Direction.OUTPUT  # Set the direction of the LED pin to OUTPUT

# Countdown loop from 10 to 1
for x in range(10, 0, -1):
    print(x)  # Print the current value of x
    time.sleep(1)  # Pause for 1 second

# After the countdown, print "Liftoff!"
print("Liftoff!")
