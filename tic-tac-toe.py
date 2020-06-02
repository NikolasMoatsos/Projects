board = [" "," "," "," "," "," "," "," "," "]
winner = {1: [[2,3],[4,7],[5,9]] , 2: [[1,3],[5,8]] , 3: [[1,2],[5,7],[6,9]] , 4: [[1,7],[5,6]] , 
5: [[1,9],[2,8],[4,6],[3,7]] , 6: [[3,9],[4,5]] , 7:[[1,4],[3,5],[8,9]] , 8:[[7,9],[2,5]] , 9:[[1,5],[3,6],[7,8]]}
            
def PrintBoard():
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" \n---|---|---\n "+board[3]+" | "+board[4]+" | "+board[5]+
    " \n---|---|---\n "+board[6]+" | "+board[7]+" | "+board[8]+" ")

counter = 1
end = False
while end == False:
    PrintBoard()
    if counter % 2 == 1:
        choice = input("Choose an empty space for X: ")
        choice = int(choice)
        if board[choice - 1] ==" ":
            board[choice - 1] = "X"
        else:
            print("This place is taken choose an other!")
            continue   
    else: 
        choice = input("Choose an empty space for O: ")
        choice = int(choice)
        if board[choice - 1] ==" ":
            board[choice - 1] = "O"
        else:
            print("This place is taken choose an other!")
            continue 
    for i in winner[choice]:
        if board[i[0] - 1] == board[i[1] - 1] and board[choice - 1] == board[i[0] - 1]:
            PrintBoard()
            print("Winner : ",board[choice -1])
            end = True
            break
    if end == False and counter == 9:
        PrintBoard()
        print("Draw !")
        break
    counter += 1
    