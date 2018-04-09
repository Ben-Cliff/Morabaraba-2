from enum import Enum
class PlayerType(Enum):
    RED = 1
    BLUE = 2
    NOT = 0

def whatName(_num):
    if _num==PlayerType.RED:
        return "RED"
    if _num==PlayerType.BLUE:
        return "BLUE"
    return "NONE"

class PlayerClass:
    def __init__(self, _cows, _playerType):
        self.cows = _cows
        self.name = whatName(_playerType)
        self.playerType = _playerType
