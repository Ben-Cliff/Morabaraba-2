import _DrawBoard
import _PlaceCow
import _MoveCow
import _ShootCow
import _IsMillFor

class game(object):
    # Replace item at position in list
    # def board_replace(whre,wht):
    #     game_board[where] = wht

    def draw_board(self, game_board):
        # Assigned: Ernest
        # draw the board
        return _DrawBoard.draw_board(game_board)

    def place(self, game_board):
        # Assigned: 
        # get input and place
        game_board = _PlaceCow.place(self, game_board)
        return game_board

    def move(self, can_it_fly):
        # Assigned: 
        # pick a spot then move it
        return _MoveCow.move(self.game_board, False)

    def shoot(self):
        # Assigned: 
        # kill a cow
        return _ShootCow.shoot(self.game_board)

    def is_there_a_mill_for(self):
        # Assigned: 
        # Check the mills for this player
        return _IsMillFor.is_there_a_mill_for(self.game_board)

    def main(self, game_board):
        # Assigned: 
        # Main Life of Game : interaction
        self.draw_board(self, game_board)
        i_got = input("Tell me to do something? ")
        # use input to choose what the game plays
        game_board = self.place(self, game_board)
        return game_board

g = game
game_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    game_board = g.main(g, game_board)