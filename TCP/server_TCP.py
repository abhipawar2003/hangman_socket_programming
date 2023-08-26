import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))


game_state = client_socket.recv(1024).decode()
print(game_state)
guessess=6

while True:
    guess = input("Guess a letter: ")
    
    client_socket.send(guess.encode())
    game_state = client_socket.recv(1024).decode()
    print(game_state)
    if "win"  in game_state.lower():
            break
    if guessess == 0:
        if "win" not in game_state.lower():
            print("you lost the game")
            break
    print("you have only",guessess,"guessess left") 
    guessess=guessess-1

client_socket.close()
