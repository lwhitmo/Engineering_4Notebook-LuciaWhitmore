# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad](#Launchpad)
    * [Countdown](#Countdown_Part_1)
    * [Lights](#Lights(LaunchpadPt.2))
    * [Button](#Button)
    * [Servo](#Servo)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

# Launchpad 
## Countdown_Part_1

### Assignment Description

Print on the serial monitor a countdown from 10 seconds to 0. When the countdown reaches 0, print "Liftoff."


### Evidence

![countdowngif](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/ezgif.com-crop.gif)



### Code
Link to my [code](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/launchpad.py). 


### Reflection

When making the range loop, make sure that everything you want to have in that loop is "tabbed." Also making sure that you have imported all the necessary boards for the assignment or else it will not function. Lastly, if you want something to get all the way down to one on your serial monitor, make sure to include zero in your range.

&nbsp;

## Lights (LaunchpadPt.2)

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

## Lights + Button (LaunchpadPt.3)

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

## Lights + Button +Servo (LaunchpadPt.4)

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

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyperlink woo](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/raspberry-pi/test.py)
### Test Image
![random test image](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/unnamed.png)
### Test GIF
![random test gif](https://github.com/lwhitmo/Engineering_4Notebook-LuciaWhitmore/blob/main/images/01-eyes-final.gif)
