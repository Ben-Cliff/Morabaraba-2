import _DataStructures
import _PlayerData

import time

# Place a cow
def place(self, i_got):
    # First check if the choice was correct
    boardPos = _DataStructures.allPositions.index(i_got)
    then_got = boardPos
    
    # Error handling - check the move to make sure we can use it (empty and an actual position)

    if self.game_board[boardPos]!=_PlayerData.PlayerType.NOT:           #occupiedcheck
        while self.game_board[then_got]!=_PlayerData.PlayerType.NOT:    #while user input incorrct, ask again
            then_got = input(" ~ Oops, the tile needs to be empty please pick again:\n\t\t")
            if then_got in _DataStructures.allPositions:                #Correct input co-ordinate
                then_got = _DataStructures.allPositions.index(then_got) #exit case
    self.game_board[then_got] = self.whosTurn                           #edit board

    # Let the player know with a certain amount of time
    print('\nNeat, you placed one!\n')
    time.sleep(2)
    
    return self.game_board