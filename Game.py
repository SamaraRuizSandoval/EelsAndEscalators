import random
from Jumper import Jumper
from binaryTree import Node

"""Board class

This class will create the board and the eels and escalators 
objects. 
"""

class Board:
    __specialTiles = dict()

    def __init__(self, boardSize:int, numEels: int, numEscalators:int):
        self.__boardSize = boardSize
        self.__numEels = numEels
        self.__numEscalators = numEscalators

    def getBoardSize(self) -> int:
        return self.__boardSize

    def addEels(self, val1:int, val2: int):
        if (val1 > val2):
            eel = Jumper(val1, val2, 'eel')
            self.__specialTiles[val1] = eel
        else:
            eel = Jumper(val2, val1, 'eel')
            self.__specialTiles[val2] = eel

    def addEscalator(self, val1:int, val2: int):
        if (val1 < val2):
            escalator = Jumper(val1, val2, 'escalator')
            self.__specialTiles[val1] = escalator
        else:
            escalator = Jumper(val2, val1, 'escalator')
            self.__specialTiles[val2] = escalator

    def checkIfSpecialTile(self, tileNum:int) -> bool:
        if (tileNum not in self.__specialTiles.keys()):
            return False
        else:
            return True

    def getJumperData(self, jumperStart:int) -> list:
        jumper = self.__specialTiles[jumperStart]
        jumperType = jumper.getType()
        jumperEnd = jumper.getEnd()
        return [jumperType, jumperEnd]

    def createRandomBoard(self):
        occupiedTiles = None
        minRandomNum = 1                     # Jumpers can start at tile 1
        maxRandomNum = self.__boardSize - 1  # Jumpers can end at max -1 of boardSize

        # Create first element close to the middle
        middle = int(self.__boardSize / 2)
        
        # This is so that the binary tree is balanced
        val1 = random.randint( middle - 10, middle + 10)
        occupiedTiles = Node(val1)    # Creating binary tree to check if tile is in use
        val2 = random.randint(minRandomNum, val1)
        occupiedTiles.insert(val2)
        eel = Jumper(val1, val2, 'eel')
        self.__specialTiles[val1] = eel

        for i in range (0, self.__numEels + self.__numEscalators - 1):
            val1 = random.randint(minRandomNum, maxRandomNum)
            while occupiedTiles.valExists(val1):
                print("Val exists: ", val1)
                val1 = random.randint(minRandomNum, maxRandomNum)
            occupiedTiles.insert(val1)
            
            val2 = random.randint(minRandomNum, maxRandomNum)
            while occupiedTiles.valExists(val2):
                print("Val exists: ", val2)
                val2 = random.randint(minRandomNum, maxRandomNum)
            occupiedTiles.insert(val2)

            if(i < self.__numEels - 1):  # add eels 
                self.addEels(val1, val2)
            else:
                self.addEscalator(val1,val2)

        for tile in self.__specialTiles:
            print(self.__specialTiles[tile].printJumper())

