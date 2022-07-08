from Dice import Dice
from binaryTree import Node
from Board import Board
from Player import Player
from time import sleep 

class Game:
    __turn = 0
    __players = {}
    __gameOn = True    #Will be false once the game is over
    _newDice = Dice()

    def __init__(self, numPlayers:int):
        self.__numPlayers = numPlayers
        # TODO: Extend so that player can set the size of board
        #self.__newBoard = Board(100,8, 8)
        self.__newBoard = Board(20,1, 1)
    
    def addPlayer(self, id:int, name:str):
        newPlayer = Player(id, name)
        self.__players[id] = newPlayer

    def printPlayerStats(self):
        for playerID in self.__players:
            print("Player : [", playerID, "] = " , self.__players[playerID].printStats())

    def checkIfWon(self, playerPosition):
        if(playerPosition >= self.__newBoard.getBoardSize()):
            print("Game Over")
            self.__gameOn = False

    def checkIfSpecialTile(self, playerName:str, position:int) -> int:
        jumperExists = self.__newBoard.checkIfSpecialTile(position)
        if jumperExists:
            jumperData = self.__newBoard.getJumperData(position)
            jumperType = jumperData[0]
            jumperEnd = jumperData[1]
            print(playerName, " fell on a ", jumperType)
            print(playerName, " is now in position ", jumperEnd)
            return jumperEnd
        else:
            return position
            

    def updatePlayerPosition(self, currentPlayer:Player, diceOutput:int):
        player = currentPlayer
        currentPosition = player.getBoardPosition()
        newPosition = currentPosition + diceOutput
        print(player.getName(), "moving to tile ", newPosition)
        self.checkIfWon(newPosition)
        newPosition = self.checkIfSpecialTile(player.getName(), newPosition)
        player.setBoardPosition(newPosition)

    def startGame(self):
        self.__newBoard.createRandomBoard()
        while self.__gameOn:
            currentPlayer = self.__players[self.__turn]
            sleep(2)
            print("\n", currentPlayer.getName(), " turn..." )
            self.printPlayerStats()  #! FIX
            print("  1. Roll Dice")
            print("  9. Exit \n")
            selection = input("Enter selection: ")
            if selection == "1":
                diceOutput=self._newDice.rollDice()
                print("\nDice: ", diceOutput)
                self.updatePlayerPosition(currentPlayer, diceOutput)
            elif selection == "9":
                self.__gameOn = False

            # Change turn
            self.__turn+=1
            if(self.__turn == self.__numPlayers):
                self.printPlayerStats()
                self.__turn = 0
