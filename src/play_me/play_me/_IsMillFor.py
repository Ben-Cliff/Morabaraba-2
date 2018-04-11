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
    #_DataStructures.mills   #list of mills
    #while loop looking for input compared to ,mills list
    translated_input = _DataStructures.allPositions.index(i_got)                    #translates co-ordinates
    fine_tuned = []
    for x in range(len(_DataStructures.mills)) :
        look_mill = _DataStructures.mills[x]
        for y in range(len(look_mill)):
            if translated_input == look_mill[y] :
                fine_tuned.append(look_mill)                                        #Potential mill found, added to list
                
    #inspect fine_tuned for other tiles
    for x in range(len(fine_tuned)):
        mill_filled = fine_tuned[x]
        val = game_board[mill_filled[0]]
        valb = game_board[mill_filled[1]]
        valc = game_board[mill_filled[2]]											#mill formed!
        if (val == player) and (valb == player) and (valc == player) :
             return True

    return False                                                                               