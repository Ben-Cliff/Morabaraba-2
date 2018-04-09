import _DataStructures
import _PlayerData
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

        # swap turns
        if self.whosTurn==_PlayerData.PlayerType.RED:
            self.whosTurn = _PlayerData.PlayerType.BLUE
        else:
            self.whosTurn = _PlayerData.PlayerType.RED

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
        
        self.draw_board(self)
        
        move_posibilities = ["1", "2", "3", "4"]

        # Ernest do the code working out which options are available
        # 1 testing - place
        if self.whosTurn==_PlayerData.PlayerType.RED:
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



        print("You currently have the following options: 1 = place, 2 = move, 3 = shoot, 4 = is mill")
        # get which play option
        i_got = input("\tSo which would you like to do?\n\tYour available options are " + str(move_posibilities) + "\n\t\t")
        while not i_got in move_posibilities:
            i_got = input(" ~ Oops, that isn't possible, please try again:\n\t\t")
        # get where to play
        then_got = input("\tWhich row and column would you like to do this on? (format: <row><column> e.g. 'e4', dont leave spaces)\n\t\t")
        while not then_got in _DataStructures.allPositions:
            then_got  = input(" ~ Woops! That isnt possible, please try another option: ");
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

        # Check if game ends here

        self.game_board = game_board

g = game
g.game_board = _DataStructures.flatboard

g.player1 = _PlayerData.PlayerClass(3, _PlayerData.PlayerType.RED)
g.player2 = _PlayerData.PlayerClass(3, _PlayerData.PlayerType.BLUE)
g.whosTurn = _PlayerData.PlayerType.RED

while True:
    print("\n    ~~~~    \n") # Only added to see all "code" play together
    g.main(g)