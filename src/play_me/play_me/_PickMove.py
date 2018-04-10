import _DataStructures
import _PlayerData
import _IsMillFor
def pick_valid_spot(game_board, option, player, msg, err):      #Options: 1-Empty 2-Player's cow 3-Enemy Player's Cow
    
    if option==1:   #Expecting Empty Spot
        avail = []
        for x in range(24):
            if _DataStructures.get_player_icon[game_board[x]] == " ":
                avail.append(_DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)


    if option==2:   #Expecting Player's cow in spot
        avail = []
        for x in range(24):
            if game_board[x]==player:
                avail.append(_DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)

    if option==3:    #Expecting Enemy's cow in spot

        avail = []
        otherplayer = player
        if player==_PlayerData.PlayerType.RED:
            otherplayer = _PlayerData.PlayerType.BLUE
        else:
            otherplayer = _DataStructures.RED
        
        for x in range(24):

            if (game_board[x]==player) and (_IsMillFor.is_there_a_mill_for(game_board[x],game_board, _DataStructures.allPositions[x]) == False):
                avail.append(_DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)




