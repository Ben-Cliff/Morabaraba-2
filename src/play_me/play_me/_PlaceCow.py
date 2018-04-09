import _PlayerData

def place(self, i_got):
    # Place a cow

    possibilitys = ["a1", "a4", "a7", "b2", "b4", "b6", "c3", "c4", "c5", "d1", "d2", "d3", "d5", "d6", "d7", "e5", "e6", "e7", "f2", "f4", "f6", "g1", "g4", "g7"]
    boardPos = possibilitys.index(i_got)
    print("got to C " + i_got + " / " + str(boardPos))
    # TODO: build this into a better structure, its a 50/50 between both not infinite on both
    if self.game_board[boardPos]!=_PlayerData.PlayerType.NOT:
        print("got to A")
        then_got = boardPos
        while self.game_board[then_got]!=_PlayerData.PlayerType.NOT:
            print("got to B")
            # get where to play
            then_got = input("\n    Oops, as a reminder it needs to be an empty tile availabe!\n" +
                             "  We see" + str(self.game_board[boardPos]) +  # debug purposes incase this happens again
                             "  (Note: format being <row><column> e.g. 'e4' is accepted as the input, dont leave spaces)\n")
            while not then_got in ["a1", "a4", "a7", "b2", "b4", "b6", "c3", "c4", "c5", "d1", "d2", "d3", "d5", "d6", "d7", "e5", "e6", "e7", "f2", "f4", "f6", "g1", "g4", "g7"]:
                then_got  = input(" ~ Woops! That isnt possible since there is something there!\n" +
                                  "   We see " + then_got + # debug purposes incase this happens again
                                  "    Please tell me, which row and column do you want to do this? (remember it must be empty)");
            then_got = possibilitys.index(then_got)
    self.game_board[boardPos] = self.whosTurn

    print(self.game_board)

    print('\n\nNeat, you placed one!\n\n')
    return self.game_board