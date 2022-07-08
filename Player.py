"""Player class

This class will keep track of the players by storing data such
as the name and position of the players in the board
"""

class Player:
    
    __positionBoard = 0

    def __init__(self, id:int, name:str):
        self.__name = name
        #TODO: Record of games won

    def  getName(self) -> str:
        return self.__name

    def setBoardPosition(self, newPosition:int):
        self.__positionBoard = newPosition
    
    def  getBoardPosition(self) -> int:
        return self.__positionBoard

    def printStats(self):
        return f"Name: {self.__name}, is in position: {self.__positionBoard}"
        
