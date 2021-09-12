import string
import numpy as np

def main():
    go_row = 19
    go_col = 19
    board = np.zeros((go_row, go_col), int)
    board = player_input(board)
    print_board(board)   

def print_board(board): 
    print("\n")
    print("      ", end = "")
    for c1 in range (len(board[0])):
        if (c1+1<10):
            print(c1+1, "  ", end= "")
        else:
            print(c1+1, " ", end ="")
    print("\n")
    for y_loc in range(len(board[0])):
        print("----", end = "")
    print("-------\n")
    for row in range(len(board)):
        if (row+1<10):
            print(row+1, " |  ", end = "")
        else:
            print(row+1, "|  ", end = "")
        for col in range(len(board[0])):
            print(board[row][col], "  ", end='')
        print("|", end ='')
        print("\n")
    for y_loc in range(len(board[0])):
        print("----", end = "")
    print("-------")

def player_input(board):
    #player 1 is black and player 2 is white
    action = 1
    player = 1;
    while (action == 1):
        while True:
            try:
                print("-------------------------------------")
                row_move = int(input("Enter Row Move (-1 to forfeit): "))
                while (not valid_move(row_move)):
                    if (row_move == -1):
                        print("Player", player, "has forfeited the match")
                        action = 0
                        break;
                    else:
                        row_move = int(input("Enter Row Move (-1 to stop): "))
                if (action == 0):
                    break
                col_move = int(input("Enter Column Move: (-1 to stop): "))
                while (not valid_move(col_move)):
                    if (col_move == -1):
                        print("Player", player, "has forfeited the match")
                        action = 0
                        break;
                    else:
                        col_move = int(input("Enter Column Move: (-1 to stop): "))
                break
            except ValueError:
                print("Invalid Move, not integer number has been entered")
        if (action == 1):
            print("The player", player, "inserted on [", row_move, ",", col_move, "]")
            board[row_move-1][col_move-1] = player
            if (player == 1):
                player = 2
            else:
                player = 1
    return board

def valid_move(move):
    if (move<1 or move>19):
        if (move != -1):
            print("Invalid Move")
        return False
    else:
        return True



if __name__ == "__main__":
    main()
