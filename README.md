Overview
========
This is a pong game using redis as a data server.
All game variables (e.g., co-ordinates of the ball and the players) are treated as redis key-value pairs.

The server (server.py) runs a `while 1` loop that updates the position of the ball and does colliosion detection.

The client (client_x.py) renders the game objects based on the values of the values stored in the keys. It also takes player input (using pygame's event handler) and updates the values
of the players' positions in the redis dictionary.

Therefore, both the server and client operate on the redis dictionary - the server changes the position of the ball and the client changes
the position of the player. The server also uses the value of the players' position to do collision detection. But at no point do the client and server
try to change the same variable and so there can be no conflicts there.

server.py
=========
The server has just one function apart from main(), one that moves the ball. The entire logic of the ball's movement & collision detection has been implemented using simple if-else statements.
I have used the sleep function in line 48 because the speed at which redis data updates is just too fast for decent gameplay.
It also prints the game variables to the console, just for fun.

The game loop runs in the main function. D-uh.

client_x.py
===========
The client used pygame library to create and render game objects, all the pygame code is standard boilerplate. 
The client picks up the location data from the redis server. We can simply specify the `host` parameter in line 53 to connect to any machine that is runnning the server code.
The client also uses a `while 1` loop to continuosly render the game on the client machine and also handle keyboard inputs.
Based on the keyboard inputs, it updates the redis dictionary.

