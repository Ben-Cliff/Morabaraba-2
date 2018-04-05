def draw_board(game_board):
    # Draw the board
    get_player_o = {0 : " ",
    				1 : "X",
    				2 : "0"}
    print("\n")
    print("\t  \t1,2,3    4    5,6,7")
    print("\t[A]\t" + get_player_o[game_board[0]] + "........" + get_player_o[game_board[1]] + "........" + get_player_o[game_board[2]] + "")
    print("\t   \t|\       |       /|")
    print("\t[B]\t| " + get_player_o[game_board[8]] + "......" + get_player_o[game_board[9]] + "......" + get_player_o[game_board[10]] + " |")
    print("\t   \t| |\     |     /| |")
    print("\t[C]\t| | " + get_player_o[game_board[16]] + "...." + get_player_o[game_board[17]] + "...." + get_player_o[game_board[18]] + " | |")
    print("\t   \t| | |         | | |")
    print("\t[D]\t" + get_player_o[game_board[7]] + "." + get_player_o[game_board[15]] + "." + get_player_o[game_board[23]] + "         " + get_player_o[game_board[19]] + "." + get_player_o[game_board[11]] + "." + get_player_o[game_board[3]] + " ")
    print("\t   \t| | |         | | |")
    print("\t[E]\t| | " + get_player_o[game_board[22]] + "...." + get_player_o[game_board[21]] + "...." + get_player_o[game_board[20]] + " | |")
    print("\t   \t| |/     |     \| |")
    print("\t[F]\t| " + get_player_o[game_board[14]] + "......" + get_player_o[game_board[13]] + "......" + get_player_o[game_board[12]] + " |")
    print("\t   \t|/       |       \|")
    print("\t[G]\t" + get_player_o[game_board[6]] + "........" + get_player_o[game_board[5]] + "........" + get_player_o[game_board[4]] + "\n\n")

# Drawing in colours isnt important for this project, also it added difficulty
#/// <summary>
#/// Write a full string with colours converted for the game (so we can have red/blue/gray/white/etc)
#/// </summary>
#/// <param name="msg">The string we need to convert and write on console</param>
#let rec consColorWrite =
#    fun (msg : string) ->
#        let head = msg.Chars 0
#        let newMsg = msg.Substring(1)
#        match head with
#        | 'X' ->
#            System.Console.ForegroundColor<-System.ConsoleColor.Red
#            System.Console.Write(head);
#        | '0' ->
#            System.Console.ForegroundColor<-System.ConsoleColor.Blue
#            System.Console.Write(head);
#        | '[' | ']' | '-' | '|' | '\\' | '/' | ',' ->
#            System.Console.ForegroundColor<-System.ConsoleColor.DarkGray
#            System.Console.Write(head);
#        | a ->
#            System.Console.ForegroundColor<-System.ConsoleColor.White
#            System.Console.Write(head);
#        match newMsg with
#        | "" -> System.Console.WriteLine() // End line
#        | _ -> consColorWrite newMsg