import time
import board
import digitalio
led = digitalio.DigitalInOut(board.LED)

while True:


    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)