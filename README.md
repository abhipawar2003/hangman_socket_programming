# hangman_socket_programming
Multi user gaming server

Abstract

This project involves the design and implementation of a multi-user gaming server using socket programming. The goal is to create a platform that allows multiple players to connect to a server and participate in a real-time game environment. The server will be designed to handle multiple connections simultaneously, enabling players to communicate with each other and share game data in real-time. The implementation will involve the use of socket programming techniques to manage the communication between the server and the clients. The result of this project will be a robust and scalable gaming server that can support multiple users and provide a seamless gaming experience. This implementation will include the both the type of connections UDP and TCP

Description about client server code

The program is built using the socket module in Python, which allows for communication between different processes running on different machines.
The program consists of two parts: the server and the client. The server is responsible for managing the game, keeping track of the secret word, and sending updates to the clients. The clients connect to the server, receive updates about the game, and send guesses for the secret word.


The server code sets up a socket to listen for incoming connections from clients. When a client connects, the server creates a new thread to handle the client's requests. The server then generates a random secret word and sends it to all clients, along with information about the number of letters in the word.
The clients then take turns guessing letters in the word. Each time a client makes a guess, the server checks if the letter is in the word and sends an update to all clients with the new state of the game including the positions of correctly guessed letters. The game continues until either the clients correctly guess the word or the Hangman is fully drawn (representing a wrong guess).


The code for the server and client both use the socket module to establish and manage connections. The server code also uses the threading module to create a new thread for each client. The client code uses a simple user interface (such as a command-line interface) to allow the user to input their guesses
Overall, the multi user Hangman code using socket programming in Python is a fun and educational way to learn about network programming and how to implement multiplayer games.

Outputs:
TCP 

![image](https://github.com/abhipawar2003/hangman_socket_programming/assets/112234264/e4d11c37-82a2-418d-a919-4475c52d71b6)



 
UDP

![image](https://github.com/abhipawar2003/hangman_socket_programming/assets/112234264/29550c22-8adf-45c9-a100-e14d3e2632c9)



