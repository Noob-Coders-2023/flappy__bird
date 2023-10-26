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
- paygame 

## construction processes

**first stage**: 
Install pygame

```
$ mkdir_awesome_pygame_project
$cd_awesome_pygame_project
```
And after that, along with the capabilities that pygame provides us, we put the background, the ground, the bird, and the loops on the page with the coordinates we got.
![set](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQCaoojR1JgQuMmzZqsOGw59zEljta0a1YKIjIzbeYj0jVPuDezOi_oPGwz5RH8vfamNs&usqp=CAU)
----
**The second stage**: 
In the second stage, to create an illusion in the player and as if the bird is moving, the ground and the background and loops from left to right to move between

**For the bird, only wing movement and vertical movement are considered**

-----
**Third stage**: 
At this point, we will score points for the bird not to hit the birds and if the game is done, the game over the game will end

**Press the r button to start again and keep the previous scores**