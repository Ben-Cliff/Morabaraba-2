import _DataStructures
import _PickMove
import _PlayerData
import _PickMove
import _IsMillFor
#interaction ie PickMove
        # check ismill
            #destroy dat moo

def shoot(player, game_board):
    # pick a spot then move it
    #valid spot given
    enemy = _PlayerData.PlayerType.NOT
    if player == _PlayerData.PlayerType.BLUE:
        enemy = _PlayerData.PlayerType.RED
    else: enemy = _PlayerData.PlayerType.BLUE
    coord = _PickMove.pick_valid_spot(game_board,3,enemy, "PEWPEW Shoot mode Activated \nChose a target co-ordinate. No friendly fire \n " , "opción inválida! Aprende español gratis en  https://www.duolingo.com/" )       #option 3 = opposite player chosen
    while (_IsMillFor.is_there_a_mill_for(enemy,game_board, _DataStructures.allPositions[coord] ) != False):
        print("Mill Detected. Try again")
        coord = _PickMove.pick_valid_spot(game_board,3,enemy, "PEWPEW Shoot mode Activated \nChose a target co-ordinate. No friendly fire \n " , " 'Still' opción inválida!" )       
         
    game_board[coord] = _PlayerData.PlayerType.NOT
    
    return game_board

