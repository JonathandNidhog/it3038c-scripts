# Lab 7

This document is an introduction for how to run the python script that I creat for lab7.<br>
The plugin I choose is the pygame. By useing pygame you need install it with the follow comand.<br>
`python -m pip install -U pygame==2.2.0 --user`<br>
Then in python, firsrly import the plugin pygame.<br>
```
import pygame, time
from pygame.locals import *
```
Then the first funtion I use from pygame plugin is the command use to define the color, user can according use RGB color value to get the color they want.<br>
the code is 
```
bgColour = pygame.Color(0,0,0)
```
here I set the `bgColor` to (0, 0, 0)<br>
In main function I will use the `bgcolor` to set the background color of my game windows.<br>
Now let start about the main function.<br>
In main function will use `pygame.init()` to initiate the pygame plugin.<br>
Then according the `pygame.display.set_mode((1000,800))` to set my game window size. Use `__ .fill(bgColour)` to set backgroud color<br>
According the ` pygame.display.set_caption('Lab7')` to set the window's name like "Lab7" <br>
Finally use `pygame.quit` to quit the script. <br>
Also I use the `time.sleep(5)` to control my program auto close in 5 second.<br>
After all the code is like this:<br>
```
import pygame, time
from pygame.locals import *

bgColour = pygame.Color(0,0,0)

def main():

    pygame.init()
    playSurface = pygame.display.set_mode((1000,800))
    playSurface.fill(bgColour)
    pygame.display.set_caption('Lab7')
    time.sleep(5) 
    pygame.quit()
if __name__ == "__main__":
    main()
    ```
