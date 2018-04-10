import _DataStructures
import _PickMove
import _PlayerData

#interaction ie PickMove
        # check ismill
            #destroy dat moo

def shoot(player, game_board, i_got):
    # pick a spot then move it
    #valid spot given
    if player == _PlayerData.PlayerType.BLUE:
        enemy = _PlayerData.PlayerType.RED
    else: enemy = _PlayerData.PlayerType.BLUE
    coord = pick_valid_spot(game_board,3,enemy, "PEWPEW Shoot mode Activated \nChose a target co-ordinate. No friendly fire \n " , "Sorry, incorrect tile, chose a slice of beef that doesn't belong to you" )       #option 3 = opposite player chosen
    while (is_there_a_mill_for(enemy,game_board, i_got) == False):
        print("Mill Detected. Try again")
        coord = pick_valid_spot(game_board,3,enemy, "PEWPEW Shoot mode Activated \nChose a target co-ordinate. No friendly fire \n " , "Sorry, incorrect tile, chose a slice of beef that doesn't belong to you" )       
         
    game_board[coord] = _PlayerData.PlayerType.NOT
    
    return game_board

