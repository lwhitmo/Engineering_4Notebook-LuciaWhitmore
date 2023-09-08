#type: ignore

import time
import board
import digitalio
redled = digitalio.DigitalInOut(board.LED)
redled.direction = digitalio.Direction.OUTPUT 


for x in range(10,0,-1):
   print(x)
   time.sleep(1)


print("Liftoff!") 
