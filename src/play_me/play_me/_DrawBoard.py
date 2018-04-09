import _PlayerData
import _DataStructures

def draw_board(game_board):
    # Draw the board
    print(_DataStructures.GRAY)
    print("\t  \t1,2,3    4    5,6,7")
    print("\t[A]\t" + _DataStructures.get_player_icon[game_board[0]] + "........" + _DataStructures.get_player_icon[game_board[1]] + "........" + _DataStructures.get_player_icon[game_board[2]] + "")
    print("\t   \t|\       |       /|")
    print("\t[B]\t| " + _DataStructures.get_player_icon[game_board[8]] + "......" + _DataStructures.get_player_icon[game_board[9]] + "......" + _DataStructures.get_player_icon[game_board[10]] + " |")
    print("\t   \t| |\     |     /| |")
    print("\t[C]\t| | " + _DataStructures.get_player_icon[game_board[16]] + "...." + _DataStructures.get_player_icon[game_board[17]] + "...." + _DataStructures.get_player_icon[game_board[18]] + " | |")
    print("\t   \t| | |         | | |")
    print("\t[D]\t" + _DataStructures.get_player_icon[game_board[7]] + "." + _DataStructures.get_player_icon[game_board[15]] + "." + _DataStructures.get_player_icon[game_board[23]] + "         " + _DataStructures.get_player_icon[game_board[19]] + "." + _DataStructures.get_player_icon[game_board[11]] + "." + _DataStructures.get_player_icon[game_board[3]] + " ")
    print("\t   \t| | |         | | |")
    print("\t[E]\t| | " + _DataStructures.get_player_icon[game_board[22]] + "...." + _DataStructures.get_player_icon[game_board[21]] + "...." + _DataStructures.get_player_icon[game_board[20]] + " | |")
    print("\t   \t| |/     |     \| |")
    print("\t[F]\t| " + _DataStructures.get_player_icon[game_board[14]] + "......" + _DataStructures.get_player_icon[game_board[13]] + "......" + _DataStructures.get_player_icon[game_board[12]] + " |")
    print("\t   \t|/       |       \|")
    print("\t[G]\t" + _DataStructures.get_player_icon[game_board[6]] + "........" + _DataStructures.get_player_icon[game_board[5]] + "........" + _DataStructures.get_player_icon[game_board[4]] + "\n")
    print(_DataStructures.WHITE)