import _PlayerData
import _IsMillFor
import _DataStructures

def move(game_board, can_it_fly, playertype, self):
    #can_it_fly  boolean check if player has 3 cows
    # pick a spot then move it
    num_cows=game_board.count(playertype)
    if num_cows==3:
        #fly
        # -> we can pick any empty
        frm = pick_valid_spot(game_board, 2, playertype, _PlayerData.whatName(playertype) + " player's turn to FLY! Enter a coordinate to warp into space from (where your cow is)", _PlayerData.whatName(playertype) + " player, that was not one of your cows, sorry. Please enter another co ordinate ")
        to = pick_valid_spot(game_board, 3, playertype, "Now where does your cow land: ", _PlayerData.whatName(playertype) + " player, woops, thats not somewhere you should land, where else should I try: ")
        game_board[frm] = _PlayerData.PlayerType.NOT
        game_board[to] = playertype
        is_there_mill = _IsMillFor.is_there_a_mill_for(playertype, game_board, _DataStructures.allPositions[to])
        if is_there_mill:
            self.shoot(playertype, game_board)
    else:
        #move
        # -> we can only pick positions empty that are NEXT TO the position we choose
        unitbool = False
        while unitbool == False:
            frm = pick_valid_spot(game_board, 2, playertype, _PlayerData.whatName(playertype) + " player's turn to move. Enter a coordinate to move a cow from", _PlayerData.whatName(playertype) + " player, you do not have a cow in that position. Please enter another co ordinate ")
            to = pick_valid_spot(game_board, 3, playertype, "Now enter a coordinate to move the cow to. (Must be empty and must be one unit away)", _PlayerData.whatName(playertype) + " player, you do not have a cow in that position. Please enter another co ordinate ")
            if _DataStructures.one_away[_DataStructures.allPositions.index(frm)].count(_DataStructures.allPositions.index(to)) > 0 :        #Tests that player is moving by one unit
                unitbool = True
        game_board[frm] = _PlayerData.PlayerType.NOT
        game_board[to] = playertype
        is_there_mill = _IsMillFor.is_there_a_mill_for(playertype, game_board, _DataStructures.allPositions[to])
        if is_there_mill:
            self.shoot(playertype, game_board)
    return game_board