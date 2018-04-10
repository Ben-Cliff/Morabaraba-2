import _DataStructures
import _PlayerData
import _IsMillFor
def pick_valid_spot(game_board, option, player, msg, err):      #Options: 1-Empty 2-PlayerType you expect, passed in as player
    if option==1:   #Expecting Empty Spot
        avail = []
        for x in [0, 24]:
            if game_board[x]==_PlayerData.PlayerType.NOT:
                avail.insert(0, _DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)


    if option==2:   #Expecting Player's cow in spot
        avail = []
        for x in [0, 24]:
            if game_board[x]==player.PlayerType:
                avail.insert(0, _DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)

    if option==3:    #Expecting Enemy's cow in spot

        avail = []
        otherplayer = player
        
        for x in [0, 24]:

            if game_board[x]==player.PlayerType & (_IsMillFor.is_there_a_mill_for(game_board[x],game_board, _DataStructures.allPositions[x]) == False):
                avail.insert(0, _DataStructures.allPositions[x])
        then_got = input("\t" + msg + "\n\t\t")
        while (not then_got in avail):
            
            then_got  = input(" ~ " + err);
        
        return _DataStructures.allPositions.index(then_got)




