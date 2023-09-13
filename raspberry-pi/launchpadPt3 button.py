#type: ignore

import time
import board
import digitalio 
button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
redled = digitalio.DigitalInOut(board.GP12)
redled.direction = digitalio.Direction.OUTPUT 
greenLED =digitalio.DigitalInOut(board.GP19)
greenLED.direction = digitalio.Direction.OUTPUT 

while button.value == False:
   
   if button.value == True:

      for x in range(10,0,-1):
         print(x)
         redled.value = True
         time.sleep(.5)
         redled.value = False
         time.sleep(.5)
      
      print("Liftoff!") 
      greenLED.value = True
      time.sleep(3)





