import _DrawBoard
import _PlaceCow
import _MoveCow
import _ShootCow
import _IsMillFor

class game(object):
    # Replace item at position in list
    # def board_replace(whre,wht):
    #     game_board[where] = wht

    def draw_board(self):
        # Assigned: Ernest
        # draw the board
        _DrawBoard.draw_board(self.game_board)

    def place(self, i_got):
        # Assigned: 
        # get input and place
        game_board = _PlaceCow.place(self, i_got)
        return game_board

    def move(self, can_it_fly, i_got):
        # Assigned: 
        # pick a spot then move it
        return _MoveCow.move(self.game_board, False, i_got)

    def shoot(self, i_got):
        # Assigned: 
        # kill a cow
        return _ShootCow.shoot(self.game_board, i_got)

    def is_there_a_mill_for(self, i_got):
        # Assigned: 
        # Check the mills for this player
        return _IsMillFor.is_there_a_mill_for(self.game_board, i_got)

    def main(self):
        # Assigned: 
        # Main Life of Game : interaction
        self.draw_board(self)
        
        print("\nCurrently every option is available for a player:\n" + 
              "1 = place, 2 = move, 3 = shoot, 4 = is mill\n" +
              "Essentially this allows us to test and debug by changing any values we need to test code\n")
        # get which play option
        i_got = input(" So what would you like to do?\n\n")
        while not i_got in ["1", "2", "3", "4"]:
            i_got = input(" ~ Woops, that isnt an option.\n" + 
                          "So what would you like to do?\n\n")
        # get where to play
        then_got = input("\n\nNow please tell me, which row and column do you want to do this?\n" +
                         "  (Note: format being <row><column> e.g. 'e4' is accepted as the input, dont leave spaces)\n")
        while not then_got in ["a1"]:
            then_got  = input(" ~ Woops! That isnt possible for that move currently, sorry\n" +
                              "Please tell me, which row and column do you want to do this? (remember format note)");
        
        # use input to choose what the game plays
        if i_got == "1":
            game_board = self.place(self, then_got)
        if i_got == "2":
            game_board = self.move(self, False, then_got)
        if i_got == "3":
            game_board = self.shoot(self, then_got)
        if i_got == "4":
            game_board = self.is_there_a_mill_for(self, then_got)
        self.game_board = game_board

g = game
g.game_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    print("\n\n ~ ~ ~ ~ ~  ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ \n\n") # Only added to see all "code" play together
    g.main(g)