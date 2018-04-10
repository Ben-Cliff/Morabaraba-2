import _DataStructures
import _PlayerData
import _DrawBoard
import _PlaceCow
import _MoveCow
import _ShootCow
import _IsMillFor
import _PickMove

'''
	This is the main game class, we use a loop around main where
	we do the following:
		-> draw the board
		-> work out which moves we have available
		-> get the user input
			-> we make sure the input is the available input
				-> doing this makes it a way lower possibility they do (or try do) an incorrect move
		-> this launches the "external" function
			-> this is the split file system we are using for the functions
		-> after the "external" function finishes we check if the end of the game is reached
			-> we assume the current player just finished a move (like shoot)
			   therefore we check if the other player has 2 cows left on the board
			   which means they lose

	Also note in string on console:
		-> "\t" is a tab space
		-> "\n" is a new line
		-> the colours are what we add to the string to make the text we write a different colour

	As an added note:
		-> Currently the default call to an external function doesnt know the player it is this turn
			-> just add to the code after [Spot X] an input of "self.whosTurn"
			-> next add it to the "def" of the function
				-> in the def brackets
				-> also in the input brackets: _<name>.<function name>(<brackets>)
			-> in the external file for that "function" add the input option to the external function
		-> just remember order (I always accidentally add it in the wrong places in all of the spots above)
'''
class game(object):
    def draw_board(self):
        # Assigned: Ernest
        # draw the board
        _DrawBoard.draw_board(self.game_board) 

    def place(self):
        # Assigned: 
        # get input and place
        game_board = _PlaceCow.place(self)
        return game_board

    def move(self, can_it_fly):
        # Assigned: 
        # pick a spot then move it
        return _MoveCow.move(self.game_board, False, self.whosTurn, self)

    def shoot(self, player, game_board):
        # Assigned: 
        # kill a cow
        return _ShootCow.shoot(self.game_board, i_got)

    def is_there_a_mill_for(self, i_got):
        # Assigned: 
        # Check the mills for this player
        return _IsMillFor.is_there_a_mill_for(self.game_board, i_got)



#########################################################################################################################


    def main(self):
        # Assigned: 
        # Main Life of Game : interaction

        # swap turns
		#  -> we swap player for every "main"
		#    -> essentially main gets some input and uses it to decide what is happening
		#       -> e.g. you have 4 cows left, you CAN place but CANT move
		#  -> essentially all EXTRA code we will write in the function we write in an external file
		#    -> e.g. In move we will run the "mill check" after we have done the movement code
		#    -> e.g. like above in the "place" code I need to do the "mill check" after it places (in my code, not after)
        if self.whosTurn==_PlayerData.PlayerType.RED:
            self.whosTurn = _PlayerData.PlayerType.BLUE
        else:
            self.whosTurn = _PlayerData.PlayerType.RED

		# Just some text "art" for player, you can also see the colour code
		#   -> to add a colour to what you write just add  "_DataStructures.<colour>"
		#     -> there are only minimal colours added currently but we can add colours in the future if you want
        if self.whosTurn==_PlayerData.PlayerType.RED:
            # Red
            print(_DataStructures.RED + 
                  "\t  ██▀███  ▓█████ ▓█████▄ \n" + 
                  "\t ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌\n" + 
                  "\t ▓██ ░▄█ ▒▒███   ░██   █▌\n" + 
                  "\t ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌\n" + 
                  "\t ░██▓ ▒██▒░▒████▒░▒████▓ \n" + 
                  "\t ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ \n" + 
                  "\t   ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ \n" + 
                  "\t   ░░   ░    ░    ░ ░  ░ \n" + 
                  "\t    ░        ░  ░   ░    \n" + 
                  "\t                  ░      \n" + 
                  _DataStructures.WHITE)
        else:
            # Blue
            print(_DataStructures.BLUE +
                  "\t                                 \n" +
                  "\t  ▄▄▄▄    ██▓     █    ██ ▓█████ \n" +
                  "\t ▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀ \n" +
                  "\t ▒██▒ ▄██▒██░    ▓██  ▒██░▒███   \n" +
                  "\t ▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄ \n" +
                  "\t ░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒\n" +
                  "\t ░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░\n" +
                  "\t ▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░\n" +
                  "\t  ░    ░   ░ ░    ░░░ ░ ░    ░   \n" +
                  "\t  ░          ░  ░   ░        ░  ░\n" +
                  "\t       ░                         \n" +
                  _DataStructures.WHITE)
        
		# Show the board                                                                              {self is the current status of the game. Board information (self.gameboard = at game start, 24 * PlayerType.Not) + player inforamtion (Determined state via cow count) }
        self.draw_board(self)      
        
		# This list is what we will show to the player as the "moves they have available" and "can do"
        move_posibilities = ["1", "2", "3", "4"]

        # We need to add code for the options we add
		#   -> essentially we check the moves available in a simple way
		#      -> e.g. when you dont have cows left to place the option "1" is removed
		#      -> similar e.g. when there are 0 cows left to place you are allowed to move
		#         -> i.e. if a player has no cows to place he has a possibility to move


        # 1 testing - place
        if self.whosTurn==_PlayerData.PlayerType.RED:                                               # {Can we place or not}
            if self.player1.cows==0:
                move_posibilities.remove("1")
        else:
            if self.player2.cows==0:                                
                move_posibilities.remove("1")


        # 2 testing - move
        if self.whosTurn==_PlayerData.PlayerType.RED:
            if not self.player1.cows==0:
                move_posibilities.remove("2")
        else:
            if not self.player2.cows==0:
                move_posibilities.remove("2")
		# we will eventually remove these options, they are currently only here to test our code as we write it





		# 3 testing - shoot



		# 4 testing - mill


		# here is the player input and essentially double checks it is what is available

		#  -> eventually we will swap this to ONLY show which moves are available, it is just showing them all for our debugging
        print("You currently have the following options: 1 = place, 2 = move, 3 = shoot, 4 = is mill")
        # get which play option
        i_got = input("\tSo which would you like to do?\n\tYour available options are " + str(move_posibilities) + "\n\t\t")
        while not i_got in move_posibilities:
            i_got = input(" ~ Oops, that isn't possible, please try again:\n\t\t")
        # get where to play
        #then_got = _PickMove.pick_valid_spot(self.game_board, 1, self.whosTurn, "", "")
        #then_got = input("\tWhich row and column would you like to do this on? (format: <row><column> e.g. 'e4', dont leave spaces)\n\t\t")
        #while not then_got in _DataStructures.allPositions:
        #    then_got  = input(" ~ Woops! That isnt possible, please try another option: ");
        
        # use input to choose what the game plays
		# [spot X]
        if i_got == "1":
            game_board = self.place(self)
            if self.whosTurn==_PlayerData.PlayerType.RED:
                g.player1.cows = g.player1.cows - 1                 #when 0 , placing no longer possible, this is where we check if they still have the "placement" move
            else:
                g.player2.cows = g.player2.cows - 1
        if i_got == "2":
            game_board = self.move(self, False)
        if i_got == "3":
            game_board = self.shoot(self)
        if i_got == "4":
            game_board = self.is_there_a_mill_for(self, i_got)

        # Check if game ends here
		# Is it player RED?
		#   -> yes, then check if player Blue has only 2 cows left on the board
		#   -> 2 cows left on the board might mean they just placed 2, therefore we double check if they still have cows to place
		#   both true for us = blue loses
		# Above is opposite check on Red instead of Blue
        if self.whosTurn==_PlayerData.PlayerType.RED:
            if game_board.count(self.player2.playerType)==2:
                if self.player2.cows==0:
                    input("BLUE LOST")
        else:                   #gameboard.COUNT -> COUNTING ALL ACTIVE INSTANCES OF RED/BLUE HERD
            if game_board.count(self.player1.playerType)==2:                              # Determine Red or Blue indivdual cow herd size with self.player1.playerType
                if self.player1.cows==0:
                	input("RED LOST")

		# Returning the game_board we might remove when simplifying code, we do it currently just in case we need it
        self.game_board = game_board





#############################################################################################################################




# When we start we make an instance of the game with a flat board
g = game    
g.game_board = _DataStructures.flatboard

# we create player 1 and player 2, the number of cows they can place it the "3" currently for our testing
#  -> we can adjust this as much as we want for testing
g.player1 = _PlayerData.PlayerClass(3, _PlayerData.PlayerType.RED) 
g.player2 = _PlayerData.PlayerClass(3, _PlayerData.PlayerType.BLUE)

# The first player ISNT what we set here since the call to Game.main swaps to the other player
#  -> the "swap" doesnt matter, its mostly for choosing who first is and the same either way
    #Whos_turn : who the game deals with individually (Red/Blue)
g.whosTurn = _PlayerData.PlayerType.RED  

# our main loop is simple
#   -> it does what is described at the top
#     -> all the rest of the code must be finished
#       -> e.g. place before it returns must check if that made a mill for us, if it did it will call shoot
while True:
    print("\n    ~~~~    \n") # Only added to see all "code" play together
    g.main(g)