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
    action = 1
    while True:
        try:
            row_move = int(input("Enter Row Move (-1 to stop): "))
            while (row_move<0 or row_move>19):
                row_move = int(input("Enter Row Move (-1 to stop): "))
                if (row_move == -1):
                    print("Users have stopped the match")
                    action = 0
                    break;

            col_move = int(input("Enter Column Move: (-1 to stop)"))
            while (col_move<0 or col_move>19):
                col_move = int(input("Enter Column Move (-1 to stop): "))
                if (col_move == -1):
                    print("Users have stopped the match")
                    action = 0
                    break;

            break
        except ValueError:
            print("Still working")
    if (action == 1):
        board[row_move-1][col_move-1] = 1
        print("hi")
    return board

if __name__ == "__main__":
    main()
