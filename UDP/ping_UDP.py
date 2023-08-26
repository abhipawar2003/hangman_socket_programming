import socket
# import threading
import random

# List of words for the game
words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]


def get_word():
    return random.choice(words)


def start_game(data, client_address):
    word = get_word()

    blanks = ["_" for letter in word]
    server_socket.sendto(" ".join(blanks).encode(), client_address)  
    while True:
        guess, client_address = server_socket.recvfrom(1024) 
        guess = guess.decode()
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
            if "_" not in blanks:
                server_socket.sendto(("You win! The word was " + word).encode(), client_address)
                break
            else:
                server_socket.sendto((" ".join(blanks)).encode(), client_address)
        else:
            server_socket.sendto("Incorrect guess. Try again.".encode(), client_address)




server_address = ('localhost', 8000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

print("Hangman server started on port 8000")
            

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("new connection established",client_address)
    start_game(data, client_address)
    print("client disconnected",client_address)   
