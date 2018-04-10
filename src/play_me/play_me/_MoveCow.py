import _PlayerData
def move(game_board, can_it_fly, playertype):
    #can_it_fly  boolean check if player has 3 cows
    # pick a spot then move it
    num_cows=game_board.count(playertype)
    if num_cows==3:
        #fly
        # -> we can pick any empty
        a=1
    else:
        #move
        # -> we can only pick positions empty that are NEXT TO the position we choose
        frm = pick_valid_spot(game_board, 2, playertype, _PlayerData.whatName(playertype) + " player's turn to move. Enter a coordinate to move a cow from", _PlayerData.whatName(playertype) + " player, you do not have a cow in that position. Please enter another co ordinate ")
        to = pick_valid_spot(game_board, 3, playertype, "Now enter a coordinate to move the cow to. (Must be empty and must be one unit away)", _PlayerData.whatName(playertype) + " player, you do not have a cow in that position. Please enter another co ordinate ")
    return game_board