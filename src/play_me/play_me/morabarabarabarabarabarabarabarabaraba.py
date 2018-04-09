import _PlayerData
import _DrawBoard
import _PlaceCow
import _MoveCow
import _ShootCow
import _IsMillFor

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
B  = '\033[34m' # blue

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

        # swap turns
        if self.whosTurn==_PlayerData.PlayerType.RED:
            self.whosTurn = _PlayerData.PlayerType.BLUE
        else:
            self.whosTurn = _PlayerData.PlayerType.RED

        if self.whosTurn==_PlayerData.PlayerType.RED:
            # Red
            print(R + "\n" +
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
                  "\n" + W)
        else:
            # Blue
            print(B + "\n" +
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
                  "\n" + W)
        
        self.draw_board(self)
        
        # Ernest do the code working out which options are available
        print("\nCurrently every option is available for a " + _PlayerData.whatName(self.whosTurn) + " :\n" + 
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
        while not then_got in ["a1", "a4", "a7", "b2", "b4", "b6", "c3", "c4", "c5", "d1", "d2", "d3", "d5", "d6", "d7", "e5", "e6", "e7", "f2", "f4", "f6", "g1", "g4", "g7"]:
            then_got  = input(" ~ Woops! That isnt possible for that move currently, sorry\n" +
                              "    (currently every board option is available)" + 
                              "    Please tell me, which row and column do you want to do this? (remember format note)");
        # Ernest do the handling for whats available, etc
        
        # use input to choose what the game plays
        if i_got == "1":
            game_board = self.place(self, then_got)
            if self.whosTurn==_PlayerData.PlayerType.RED:
                g.player1.cows = g.player1.cows - 1
            else:
                g.player2.cows = g.player2.cows - 1
        if i_got == "2":
            game_board = self.move(self, False, then_got)
        if i_got == "3":
            game_board = self.shoot(self, then_got)
        if i_got == "4":
            game_board = self.is_there_a_mill_for(self, then_got)
        self.game_board = game_board

g = game
g.game_board = [_PlayerData.PlayerType.NOT] * 27

g.player1 = _PlayerData.PlayerClass(20, _PlayerData.PlayerType.RED)
g.player2 = _PlayerData.PlayerClass(20, _PlayerData.PlayerType.BLUE)
g.whosTurn = _PlayerData.PlayerType.RED

while True:
    print("\n\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n\n") # Only added to see all "code" play together
    g.main(g)