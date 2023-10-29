![pygame](https://www.pygame.org/docs/_images/pygame_logo.png)
# flappy Bird with pygame

![flappybird](https://media.wired.co.uk/photos/606db3bf938ecee6e930f3be/1:1/w_1280,h_1280,c_limit/flappybird-1.jpg)
This game is one of the most popular games in which you control a bird and try not to hit the loops on the screen.

## project overview
![animation](https://media.tenor.com/8sBZQO2ZALwAAAAd/flappy-bird-game.gif)








The bird can move up by pressing the space button or the right mouse button, and if no button is pressed, it will be pulled to the ground under the influence of gravity.
When the bird passes through the loops without hitting, it gets a point, but when it hits the obstacles, the game ends.


![gameover](https://masliamohammad.files.wordpress.com/2014/06/flappy-bird-1.gif?w=223)




**This project needs pygame to run**
## Insallation Dependencies
- paython 2.5.2
- pygame 

## construction processes

**first stage**: 
Importing the libraries and constants of the locals module

```
import pygame,sys
```
As we already know, to use an external library in Python, we must import it into the program. For example, if we want to use the math module, we must import it into the program with the command import math. So, to use pygame and sys, we must import them.

The above line is present in every pygame program. This line is a simple import that imports the pygame and sys modules into the program so that our program can use the functions in them. All pygame functions that deal with graphics, sound, etc. are in the pygame module. All you need to know about the sys module is that it contains variables and functions related to the Python interpreter.
----
**The second stage**:Initialize pygame

With the following line, we actually want to tell Python that we intend to use pygame. For this, we need to initialize pygame. If we don't do this, pygame will not work. The pygame.init code should always come after the pygame module and before any other functions. You don't need to know what this function does, just know that in order for pygame functions to work properly, this function must be called before them. So we have
```python
()pygame.init
```






-----
**Third stage**: Determine the size of the window and its name


The next line is a call to the display.set_mode function, which returns an object called pygame.Surface for the window. In fact, set_mode initializes a Screen object to display the window. We send a double tuple of two integers to the function

```python
DISPLAYSURF=pygame.display.set_mode((x,y))



```

**the fourth stage**:Ring and game state

```python
while True: # main game loop
    for event in pygame.event.get()

```
The above line is a while loop whose condition is True. This loop never stops unless its condition is False. The only way to exit the loop is to execute a break or sys.exit(). All the games in this training series have this while loop. We call this loop the main loop of the game. Its job is to run the game until the window is closed. Inside the main loop, there is another loop, which we call the event management loop. This loop is the most important part of a reactive program like games. The event handler loop does three things:

- Handles events such as clicking the mouse or pressing a button on the click screen and...
- Updates or edits the game state.
- Shows the game status on the screen.
**the fifth stage**:pygame.event.Event objects (checking events and managing them)

Every time the user performs several actions together, such as pressing the keyboard or moving the mouse over the application window, a pygame.event.Event object is created by the pygame library to record these events. (The Event object is in the event module, and the event module itself is in the pygame module.) We can find out which events have occurred by calling the

 pygame.event.get()

  function. This function returns an array of pygame.event.Event objects.

**the sixth stage**:QUIT event and pygame.quit function
```python
if event.type==QUIT:
    pygame.quit()
    sys.exit()
```

Event objects have an attribute called type that specifies the type of event. The above line of code checks whether the event type is equal to the constant value QUIT or not. If we have a quit event, then the pygame.quit and sys.exit functions are called. The pygame.quit function is kind of the opposite of the pygame.init function. This function executes the code that disables the pygame library.

The pygame.quit function must always precede sys.exit. Here we don't have any conditions for the rest of the events like mouse movement and... so if you click on the window or press one of the buttons, nothing happens.


**the seventh stage**:update function (updating game status)

```python
pygame.display.update()

```
The last line calls the pygame.display.update function. This function displays the object returned by pygame.display.set_mode (remember that we stored this object in the DISPLAYSURF variable). Since the DISPLAYSURF object does not change in the game, every time the

 pygame.display.update
 
  function is called, the same black image is displayed again. After the last line is executed, the while loop repeats its task of displaying the black window. To close the window, we must click on the X button from the corner of the window.

