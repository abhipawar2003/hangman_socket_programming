import socket

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receive the initial game state from the server
server_address = ('localhost', 8000)
client_socket.sendto('start'.encode(), server_address)
game_state, _ = client_socket.recvfrom(1024)
game_state = game_state.decode()
print(game_state)
guessess = 6

while True:
    guess = input("Guess a letter: ")

    client_socket.sendto(guess.encode(), server_address)

    game_state, _ = client_socket.recvfrom(1024)
    game_state = game_state.decode()
    print(game_state)

    if "win" in game_state.lower():
        break

    print("you have only", guessess, "guesses left")
    if guessess == 0:
        if "win" not in game_state.lower():
            print("you lost the game")
            break

    guessess -= 1

client_socket.close()