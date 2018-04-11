cowsunplaced = 24

red = {cowscount : 12, state : 0, face : "Red"}
blue = {cowscount : 12, state : 0, face : "Blue"}
print("Red player goes first")
turn = "red"
while (red.cowscount > 0 & blue.cowscount > 0):  
    
    if turn == "red":
        player = red
    else:
        player = blue
        
    if (cowsunplaced > 0):
        cowsunplaced -= 1
        go = input(player.face + "'s turn: Enter a co ordinate to place a cow")
        place(player, go)     #call to place function
        
    else if (red.cowscount > 3):
        fro = input(player.face + "'s turn: Enter a co ordinate to move from  \n NOTE: must be one position away ")
        to = input("Enter a co ordinate to move to \n NOTE: must be one position away")
        move(player, to, fro)        #call to move function
    else:
        fro = input(player.face + "'s turn: Enter a co ordinate to fly from")
        to = input("Enter a co ordinate to fly to")
        fly(player)
    
    if turn == "red":
        turn = "blue"
    else:
        turn = "red"    
        
        
        
        

        
done