def main():
    go_row = 19
    go_col = 19
    board = [[0]*go_col]*go_row
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
    print("-----\n")
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
    print("-----")


if __name__ == "__main__":
    main()