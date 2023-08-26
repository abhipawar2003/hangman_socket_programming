import socket
import threading
import random

# List of words for the game
words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

def get_word():
    return random.choice(words)

# Function to start the game
def start_game(conn):
    word = get_word()   
    blanks = ["_" for letter in word]
    conn.send((" ".join(blanks)).encode()) 
    while True:
        guess = conn.recv(1024).decode()  
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
            # Check for the win
            if "_" not in blanks:
                conn.send(("You win! The word was " + word).encode())
                break
            else:
                conn.send((" ".join(blanks)).encode())
        else:
            conn.send(("Incorrect guess. Try again.").encode())

def handle_client(conn, addr):
    print("New client connected:", addr)
    start_game(conn)
    conn.close()
    print("Client disconnected:", addr)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

print("Hangman server started on port 5000")

while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
    