# When we want reference to the other files this is what we add
#   -> reminder we would us the file name followed by the value
#      -> e.g. _PlayerData.PlayerType.NOT     <- correct
#              PlayerType.NOT                 <- incorrect
import _DataStructures
import _PlayerData
import _PickMove

import time

# Place a cow
#  -> i_got is the string input we accepted in main and received in this external function call
#  -> self is the instance of Game we are using/playing with
#    -> you will see that it is where we can reference game_board, either player, etc
def place(self):
    boardPos = _PickMove.pick_valid_spot(self.game_board, 1, self.whosTurn, "So liek piek a place", "woopsidoodle: ")

    # First check if the choice was correct
	#  -> this gets the index in the array for the board
	#    -> note: because we double check the input before we know i_git is in the "allPositions", we only need the index
    #boardPos = _DataStructures.allPositions.index(i_got)
    then_got = boardPos
    
    # Error handling - check the move to make sure we can use it (empty and an actual position)
    if self.game_board[boardPos]!=_PlayerData.PlayerType.NOT:           #occupiedcheck
        while self.game_board[then_got]!=_PlayerData.PlayerType.NOT:    #while user input incorrct, ask again
            then_got = input(" ~ Oops, the tile needs to be empty please pick again:\n\t\t")
            if then_got in _DataStructures.allPositions:                #Correct input co-ordinate
                then_got = _DataStructures.allPositions.index(then_got) #exit case
    self.game_board[then_got] = self.whosTurn                           #edit board

    # Let the player know with a certain amount of time
	#   -> just so it doesnt instantly show the next turn
    print('\nNeat, you placed one!\n')
    time.sleep(2)
    
	# finally like I shared before we currently return the updated board
	#   -> we will remove this later unless we find a need to keep it
	#   -> this is mostly for debugging so you can call "print" for any state of board, etc
    return self.game_board