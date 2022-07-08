from Game import Game

# TODO: Create data validations
print("STARTING GAME...")
numPlayers = int(input("Enter the number of Players: "))
# TODO: Set max to 6 players
newGame = Game(numPlayers)

for i in range(0, numPlayers):
    playerName = input(f"Enter name Player{i+1}: ")
    newGame.addPlayer(i, playerName)

newGame.printPlayerStats()
newGame.startGame()