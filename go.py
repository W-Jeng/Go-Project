import string
import numpy as np

def main():
    go_row = 19
    go_col = 19
    board = np.zeros((go_row, go_col), int)
    board = player_input(board)
    print_board(board)   

def print_board(p_board): 
    print("\n")
    print("      ", end = "")
    for c1 in range (len(p_board[0])):
        if (c1+1<10):
            print(c1+1, "  ", end= "")
        else:
            print(c1+1, " ", end ="")
    print("\n")
    for y_loc in range(len(p_board[0])):
        print("----", end = "")
    print("-------\n")
    for row in range(len(p_board)):
        if (row+1<10):
            print(row+1, " |  ", end = "")
        else:
            print(row+1, "|  ", end = "")
        for col in range(len(p_board[0])):
            print(p_board[row][col], "  ", end='')
        print("|", end ='')
        print("\n")
    for y_loc in range(len(p_board[0])):
        print("----", end = "")
    print("-------")

def player_input(board):
    #player 1 is black and player 2 is white
    action = 1 #action determines whether the player's move is valid, and then added to the board
    player = 1
    turn = 1
    board_prev1 = np.zeros((19,19), int)
    board_prev2 = np.zeros((19,19), int)
    while (action == 1):
        while True:
            try:
                print("-------------------------------------")
                print("Turn " + str(turn)+ ", Player "+str(player)+ "'s turn:")
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
                if (rules_move(board, row_move, col_move, board_prev1, player, turn)):
                    break;

            except ValueError:
                print("Invalid Move, not integer number has been entered")
        if (action == 1):
            print("The player", player, "inserted on [", row_move, ",", col_move, "]")
            board_prev1 = np.array(board)
            board[row_move-1][col_move-1] = player
            turn+=1
            if (player == 1):
                player = 2
            else:
                player = 1
    return board

def valid_move(move):
    #this checks if the player's movement is within normal bound
    if (move<1 or move>19):
        if (move != -1):
            print("Invalid Move")
        return False
    else:
        return True

def rules_move(board_m, row_move, col_move, board_prev1, player, turn):
    #this checks that the step is within rules
    if (board_m[row_move-1][col_move-1] != 0):
        print("The position has been previously occupied")
        return False
    #prevents repeating moves (ko rule)
    #print_board(board_prev2)
    cur_state = board_m[row_move-1][col_move-1]
    board_m[row_move-1][col_move-1] = player
    if (turn == 3 and equal_matrices(board_m, board_prev1)):
        #print_board(board)
        print("turn" + str(turn)) 
        print("The position is repetitive")
        board_m[row_move-1][col_move-1] = cur_state
        return False
    board_m[row_move-1][col_move-1] = cur_state

    return True

def equal_matrices(board1, board2):
    for i in range(len(board1)):
        for j in range(len(board1[0])):
            if (board1[i][j] != board2[i][j]):
                return False
    return True

def flashfood(board):
    #the flashfood algorithm is capable of detecting that if a capture has happened or not


if __name__ == "__main__":
    main()





