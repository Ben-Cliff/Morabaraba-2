import _PlayerData

from enum import Enum

#Data structures
flatboard = [_PlayerData.PlayerType.NOT] * 27

mills = [[0,8,16], [1,9,17], [2,10,18], [3,11,19], [4,12,20], [5,13,21], [6,14,22], [7,15,23], [0,1,2], [2,3,4], [4,5,6], [6,7,0], [8,9,10] ,[10,11,12] ,[12,13,14], [14,15,8], [16,17,18], [18,19,20], [20,21,22], [22,23,24]]

WHITE  = '\033[0m'  # White (normal)
RED    = '\033[31m' # Red
BLUE   = '\033[36m' # Blue
GRAY   = '\033[90m' # Grey

allPositions = ["a1", "a4", "a7", "d7", "g7", "g4", "g1", "d1", "b2", "b4", "b6", "d6", "f6", "f4", "f2", "d2", "c3", "c4", "c5", "d5", "e5", "e4", "e3", "d3"]

get_player_icon = {_PlayerData.PlayerType.NOT : " ",
	_PlayerData.PlayerType.RED : RED + "X" + GRAY,
	_PlayerData.PlayerType.BLUE : BLUE + "0" + GRAY}