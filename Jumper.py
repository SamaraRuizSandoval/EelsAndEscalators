import EelsEscalatorsEnum

class Jumper:
    def __init__(self, start:int, end:int, type:str):
        self.__start = start
        self.__end = end
        if(type == 'eel'):
            self.__type = EelsEscalatorsEnum.JumperType.Eel
        elif(type == 'escalator'):
            self.__type = EelsEscalatorsEnum.JumperType.Escalator

    def getEnd(self) -> int:
        return self.__end

    def getType(self) -> str:
        return self.__type.name

    def printJumper(self):
        return f"{self.__type} [{self.__start}] = start: {self.__start} end: {self.__end}"