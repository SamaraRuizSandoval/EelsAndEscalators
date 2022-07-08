import random

class Dice:
    _output = None

    def rollDice(self) -> int:
        self._output = random.randint(1, 6)
        return self._output