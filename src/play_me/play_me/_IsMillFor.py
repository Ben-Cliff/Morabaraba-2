import _DataStructures


def is_there_a_mill_for(player,game_board, i_got):

    ''' 
    LOGIC:
    -> get input    (called when input is corredct)
    -> check corresponding mills it is involved in
    -> shorten array to suit specific instance of input
    -> sort through each instance lookin at game_baord
    -> true
        -> INTERACTION : shoot co-ordinate
                            -> check valid
        -> shoot opposite cow (edit board)
    -> false return game_board unedited
    '''

    # Check the mills for this player
    _DataStructures.mills   #list of mills
    #while loop looking for input compared to ,mills list
    translated_input = _DataStructures.allPositions.index(i_got)                    #translates co-ordinates
    fine_tuned = []
    for x in range(_DataStructures.mills.count) :
        look_mill = _DataStructures.mills[x]
        for y in range(look_mill):
            if translated_input == y :
                fine_tuned.append(look_mill)                                        #Potential mill found, added to list
    

    #inspect fine_tuned for other tiles
    left = f
    for x in range(fine_tuned.count):
        mill_filled = fine_tuned[x]
        val = game_board[mill_filled[0]]
        if val == player :
                valb = game_board[mill_filled[1]]
                if valb == player :
                       valc = game_board[mill_filled[2]]                             #mill formed!
                       if valc == player :
                           return true
    

    return false                                                                               

#Note Interactive message needs to be sent to player to state whether a mill has been found or not


         

        





    #if mill formed
    #   return shoot(game_baord, player)
    #return game_board
