#type: ignore

 # Import necessary libraries/modules
import time
import board
import digitalio 
import pwmio # servoo
from adafruit_motor import servo #servo

# Initialize a digital input for the button using GP0 pin
button = digitalio.DigitalInOut(board.GP0) 
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Initialize a digital output for the red LED using GP12 pin
redled = digitalio.DigitalInOut(board.GP12)
redled.direction = digitalio.Direction.OUTPUT 

# Initialize a digital output for the green LED using GP19 pin
greenLED =digitalio.DigitalInOut(board.GP19)
greenLED.direction = digitalio.Direction.OUTPUT 

pwm_servo = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

servo1.angle = 0

while button.value == False: # Run the following code in a loop while the button value is False
   

   if button.value == True:   # Check if the button value becomes True

      for x in range(10,0,-1):  # Count down from 10 to 1 and perf-orm some actions           
         print(x)  # Print the current countdown value
         redled.value = True  # Turn on the red LED
         time.sleep(.5)  # Pause for 0.5 seconds
         redled.value = False  # Turn off the red LED
         time.sleep(.5)  # Pause for another 0.5 seconds
      
      print("Liftoff!")   # When the countdown is complete, print "Liftoff!" and turn on the green LED
      greenLED.value = True
       # time.sleep(3)  # Keep the green LED on for 3 seconds
      servo1.angle = 180
      time.sleep(2)
      break







