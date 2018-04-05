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
        print(" ~~~ " + str(self.game_board))
        _DrawBoard.draw_board(self.game_board)

    def place(self):
        # Assigned: 
        # get input and place
        self.game_board = _PlaceCow.place(self)

    def move(self, can_it_fly):
        # Assigned: 
        # pick a spot then move it
        self.game_board = _MoveCow.move(self.game_board, False)

    def shoot(self):
        # Assigned: 
        # kill a cow
        self.game_board = _ShootCow.shoot(self.game_board)

    def is_there_a_mill_for(self):
        # Assigned: 
        # Check the mills for this player
        self.game_board = _IsMillFor.is_there_a_mill_for(self.game_board)

    def main(self):
        # Assigned: 
        # Main Life of Game : interaction
        self.draw_board(self)
        i_got = input("Tell me to do something? ")
        # use input to choose what the game plays
        self.game_board = self.place(self)
        print("- 4. game board to: " + str(self.game_board))

    def define_game_board(self):
        self.game_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

g = game
g.define_game_board(g)
while True:
    g.main(g)