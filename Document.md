# Python Game Development-Flappy bird

Flappy Bird is a classic and addictive game that has captured the hearts of millions with its simple yet challenging gameplay. In this tutorial, we will guide you through the process of building your very own Flappy Bird game from scratch, using the Pygame module, a popular Python library for game development.

With just a basic understanding of Python and a dash of creativity, you can harness Pygame's capabilities to create a fun and engaging gaming experience that can be customized to your liking.

## Game Setup
Let's start by making sure Pygame is installed on your computer. Open your terminal and install the pygame module using pip:

To install the pygame module, open your terminal and run the following command:


pip install pygame


Make sure you have pip installed on your computer before running the command.


After that, create a directory for the game and create the following .py files inside it: settings.py, main.py, world.py, game.py, pipe.py, bird.py. Also, create another folder inside the game directory and name it assets, which we'll use to store game media files.

Now we can start coding. Let's define our game variables and functions in settings.py
Next, let's create the main class of our game in main.py which also contains the game's main loop


### Global Variables Declared
In this step, we are declaring various global variables for our game. We first set the value for fps(frames per second), screen_width and screen_height.

We create the screen with screen_width and screen_height as an argument for the pygame.display.set_mode() function. Then, we create a ground-y variable which will give the y-coordinate for our base image, and 2 dictionaries game_images and game_sounds which will contain our various images and sounds used for the game.

### Creating the "main" function
Now let’s create the main function where our game will start and we have to initialize all pygame modules using pygame.init(). We also create fps_clock variable to help us track time at a moment using pygame.tick.Clock() function.

Then we will give a title to our main game window and store all the images in a tuple with first, which we are then assigning to the 'numbers' key in the game_images dictionary. We use pygame.image.load() with paths of the images as arguments along with convert_alpha() to change the pixel format of an image including per pixel alphas.

Similarly, we add the images of the message, base, pipe, background, player, and title, into the dictionary using various keys. For pipe, we also added an inverted pipe image by using pygame.transform.rotate() function and rotating the image by 180 degrees. We then add the sounds to the game_sounds dictionary using various keys.

It is similar to what we did for images but here we use pygame.mixer.Sound() function with the paths for various sounds as the argument for storing the sounds. Then we start a loop calling the welcomeScreen() and mainGame() functions which will be defined in the later sections.

### Creating "welcomeScreen" function
Now, we define our welcomeScreen() function which will display the welcome screen on starting the game. We start by assigning the values of the x-coordinate and y-coordinate for the player, message, and title images.

We have selected the arguments by hit and trial method and you can alter the values that suit you the best. We also give the x-coordinate of base here. Then, we start a while loop which will always be True and thus will start a loop that will not stop unless the control says quit.

Here we make use of a for loop for analyzing all the events taking place throughout the game using pygame.event.get() function. Then we check that whenever a quit type of event is encountered by pressing the escape key, the game window will close.
We will check the next condition i.e. whether we clicked the up key or the space button. If yes, we will return from the function and start the game. And if no key or button is pressed, the welcome screen is displayed. For that, we will place the background, message, player, base, and title images using screen.blit() function.

Finally, we will update our window using pygame.display.update() and will update our clock variable with fps value as argument to show just 32 frames per second.

## Creating the mainGame() function
Now we define our mainGame() function by first initializing the variable score with 0, and also give the coordinates for player image and base again.

Then we create 2 pipes for blitting on the screen using getRandomPipe() which we will be defined later. Then we create a list of upper pipes (inverted ones) and lower pipes with their x and y coordinates.

Again we have chosen values by hit and trial method. Then, we declare variables for velocities in different directions for the bird. We also provide an acceleration variable.

playerFlapVel is the velocity while flapping and playerFlapped is set to false (which is true only if the bird flaps). Then again we check for events.

1. First for exiting the game and exit the game if true.
2. Then we check if the up key or spacebar is pressed. If yes, we check if the player is below the screen top and if yes, we make some updates and play the sound of the wing using .play().
3. After this, we check if we have crashed using the isCollide() function we will define soon. If true, we will return from the function.
Then, we will check and update the scores. Using the player’s mid position, and the positions of the pipes, we increase the score if we cross a pipe and print it in the console.
Also, we play the point sound for crossing each pipe. Then if the player velocity in y-direction has not yet become max, we will provide the acceleration.
Later on, we update the playerFlpped value and then the position of the bird. We move the pipes to the left and add a new pipe when the first one is about to cross the leftmost part of the screen.

We will also see if the pipe is out of the screen and if yes, we remove it and place our pipes and the score on our screen, later on, update the display screen.

For the score, we first access all the digits of the score (if more than 1 digit score) and place the required images. We update our clock again.

## isCollide() and getRandomPipe() functions
In the isCollide() function, first, we check if we have hit the top of the base inline and then we look for collision with upper pipes by comparing the position of the bird with that of the pipe to check for the collision.

We repeat the same for lower pipes. If any of the collision conditions are true, we play the hit sound and return True.

In the getRandomPipe() function, we store the height of the pipe in the pipeHeight variable and use the offset variable to store one-third of screen_width.

We then assign the values of the x and y coordinates for the pipes using random functions at equal distances, but with different sizes of upper and lower pipes. Then we store the coordinates in a list named pipe and return it.

## The Final Output.
