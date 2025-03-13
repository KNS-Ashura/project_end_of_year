def rotate_right(board):
    board_turn_right = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            board_turn_right[j][3 - i] = board[i][j] 
    return board_turn_right

def rotate_left(board):
    board_turn_left = [[0 for i in range(4)] for k in range(4)]
    for i in range(4):
        for j in range(4):
            board_turn_left[3 - j][i] = board[i][j] 
    return board_turn_left

def rotate_side(board):
    board_turn_side = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            board_turn_side[3 - i][3 - j] = board[i][j]
    return board_turn_side

def board_fusion(board1, board2, board3, board4):
    board_join = [[0 for i in range(8)] for j in range(8)]
    for i in range(4):
        for j in range(4):
            board_join[i][j] = board1[i][j]
            board_join[i][j + 4] = board2[i][j]
            board_join[i + 4][j] = board3[i][j]
            board_join[i + 4][j + 4] = board4[i][j]
    return board_join

def get_board_fusion(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()
