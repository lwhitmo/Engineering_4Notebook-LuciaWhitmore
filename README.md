# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad](#Launchpad)
    * [Countdown](#Countdown)
    * [Lights](#Lights)
    * [Button](#Button)
    * [Servo](#Servo)
* [Crash_Avoidance](#Crash_Avoidance)
    * [Accelerometer](#Accelerometer)
    * [Lights+Power](#Lights+Power)
    * [OLED](#OLED)   
* [FEA_Beam_Assignment](#FEA_Beam_Assignment)

&nbsp;

# Launchpad 
## Countdown

### Assignment Description

Print on the serial monitor a countdown from 10 seconds to 0. When the countdown reaches 0, print "Liftoff."


### Evidence

![countdowngif](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/ezgif.com-crop.gif)



### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/launchpad.py). 


### Reflection

When making the range loop, make sure that everything you want to have in that loop is "tabbed." Also making sure that you have imported all the necessary boards for the assignment or else it will not function. Lastly, if you want something to get all the way down to one on your serial monitor, make sure to include zero in your range.

&nbsp;

## Lights

### Assignment Description

10 seconds till the countdown ends at 0 (liftoff). That countdown will be printed on the serial monitor. Turn on a green LED to indicate liftoff and blink a red light every second during the countdown.

### Evidence

![ledcountdown](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/Countdownlaunchpad.gif)

### Wiring

<img src="https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/ezgif.com-resize.jpg" width = 400>

### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/launchpad.py). 


### Reflection

When you are in the loop of range, make sure you order the led's turning on in the order of first on and THEN off. This makes sure that when the loop is over, your led will turn off. Also make sure that you connect your LED's to the right corresponding pins.

&nbsp;

## Button

### Assignment Description
10 seconds till the countdown ends at 0 (liftoff). That countdown will be printed on the serial monitor.
Turn on a green LED to indicate liftoff and blink a red light every second during the countdown.
Include a button on the countdown's physical trigger. 

### Evidence

![ledcountdown/w button](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/buttonvideolaunchpad.gif)

### Wiring

<img src="https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/buttonwiring.jpg" width = 400> 

### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/launchpadPt3%20button.py).


### Reflection

Most importantly, when wiring your button make sure it correctly coresponds with you code. AKA. Pull up or pull down. Pull down --> wire to 3V3 & button pin and base state is False (0V). Pull Up -->  wire to GND & button pin and base staye is True (3V). NEVER WIRE TO 5V!! Will short out pico.

&nbsp;

## Servo

### Assignment Description
10 seconds till the countdown ends at 0 (liftoff). That countdown will be printed on the serial monitor.
Turn on a green LED to indicate liftoff and blink a red light every second during the countdown.
Include a button on the countdown's physical trigger. 
On takeoff, move a servo 180 degrees to represent the launch tower becoming disconnected.


### Evidence

![ledcountdown/w servo](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/Launchpad%20Servo.gif)

### Wiring

<img src="https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/sevowiriirnh.jpg" width = 400>

### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/launchpadPt4%20servo.py). 


### Reflection

When using the servo, connect brown --> gnd, red --> 3V3 and yellow --> pin. Also make sure that you are only using the correct PWM pin, there are mutiple for every pico, meaning you dont want to accidentally put two inputs to one PWM pin.

#### Example 
<img src="https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/Capture.PNG" width = 400>

&nbsp;

## Crash_Avoidance

## Accelerometer

### Assignment Description
Wire up and write some code for an accelerometer that prints the x, y and z axes of acceleration on the serial monitor in real time. 

### Evidence

![accelerometer vid](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/My%20Project.gif)

### Wiring

<img src="" width = 400>

### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/Crash%20Avoidance/Accelerometer(CO).py)


### Reflection
This code incorporates two new concepts, such as rounding and .



&nbsp;

## Lights+Power

### Assignment Description
description


### Evidence

![blank](gif)

### Wiring

<img src="" width = 400>

### Code
Link to my [code](). 


### Reflection
If you need an easy variable to check if something is not at 90 degrees in all idrections, the Z variable is your friend. Instead of putting in a million if statements regarding what you dont want the other variable to be, the Z variable is uniform in the angle of 90 degrees all sides. Else statements are also helpful, "if it is not this then do this"



&nbsp;

## OLED

### Assignment Description
description


### Evidence

![blank](gif)

### Wiring

<img src="" width = 400>

### Code
Link to my [code](). 


### Reflection
Use the multiple I2C code checker to check which devices you should use in your code. Also when adding the screen, you need to update the mpu = adafruit_mpu6050.MPU6050(i2c) line of your code to mpu = adafruit_mpu6050.MPU6050(i2c, address=your-address-here). (swap them out.)



&nbsp;

## Code Template

### Assignment Description
description


### Evidence

![blank](gif)

### Wiring

<img src="" width = 400>

### Code
Link to my [code](). 


### Reflection



&nbsp;

## FEA_Beam_Assignment_1

### Assignment Description

Cyrus and I were tasked with making a 3D-printed beam that could support the most weight. The parameters were that the beam had to hold a weight of 180mm from the start of the beam, it couldn't weigh more than 13g and it couldn't use any support material. We had to use PLA material.

### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/5917476487600a4a1a491ed3).
### Part Image

![cyrus design](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/Beam%20Starter%20%2B%20Holder%20Copy%201.png)
![lucia design](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/Beam%20Starter%20%2B%20Holder%20Copy%202.png)

### Reflection

Cyrus and I made two different designs to optimize time and design energy. The types of beams we made were an upsidedown T beam and a makeshift spoon beam. The logic behind the spoon beam is mostly focused on tension along the Z axis, trying to hold the most weight vertically with a skinny base. 

&nbsp;

# FEABeamAssignmentPart3

### Assignment Description

We were tasked with using onshape simulation tools to test our beams before printing them. By using the force tool we can simulate how our beam would react to having a weight on the end of it. This is useful for picking the best beam and for knowing where we need to make adjustments.


### Part Link 

[FEABEAM](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/bc14fcb1e64d92da7e0746b2?renderMode=0&uiState=651c47ac2c3aec7eb767df86)
### Part Image
#### Stress Image
![PartImage1a](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%201%20Simulation.png)
#### Displacement Image
![PartImage1b](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%201%20Simulation%20Displacement.png)

#### Part 1 Analysis
To improve this design it would be good to remove material from the dark blue areas and add it to the red. This would involve removing parts of the side skirts and adding more to the spine that is close to the holder. There is the most stress there so it will also be good to use filets and chamfers to get rid of weak 90-degree points.

#### Stress Image
![PartImage2a](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%202%20Simulation%20Stress.png)
#### Displacement Image
![PartImage2b](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%202%20Simulation%20Displacement.png)

#### Part 2 Analysis
This design will need more changes than design 1. It would be benfitial to angle the fins to create more rigidity. It would be good to remove some material from the end of it and beef up the part close to the mounting point. If you look at the stress image you can see where it had the weakest point.


### Reflection

# FEABeamAssignmentPart4

### Assignment Description
After completing part 3 we need to take what we learned and put it into our model. We are supposed to run multiple simulations after each change that we make to see if we have any improvement. Our design is pretty good right now but we will have to make small but important changes to the weak points to improve our design.

### Part Link 

[FEABEAM](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/bc14fcb1e64d92da7e0746b2?renderMode=0&uiState=651c47ac2c3aec7eb767df86)
### Part Image

####  Improvements
Because Lucia was out for most of the week we did this the main changes were all done by me but on the last day we decided to divide and conquer to see who could make a better design. As it turns out Lucia's design beat mine by a stress factor of 1 point so we decided to go with hers. Our maxium improvement was improved by a factor of 36.27% which is good considering that our design was already at a stress factor of 11.57.

#### Lucia's Stress Image
![Lucia's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%202%20stress.png)
#### Lucia's Displacement Image
![Lucia's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%202%20displacement.png)

#### Cyrus's Stress Image
![Cyrus's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%201%20stress.png)
#### Cyrus's Displacement Image
![Cyrus's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%201%20displacement.png)

### Reflection

The FEA in ONSHAPE tool unfortunetly took a very long amount of time per every simulation. This was a hiccup in certain plans due to the fact that we needed to account for longer amounts of time per every design. 


## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink woo](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/test.py)
### Test Image
![random test image](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/unnamed.png)
### Test GIF
![random test gif](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/01-eyes-final.gif)
