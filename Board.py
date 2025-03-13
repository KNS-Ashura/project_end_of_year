
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
    

board_a = [[1, 2, 3, 4], [4, 3, 1, 1], [3, 4, 2, 2], [2, 1, 4, 3]]
board_b = [[3, 2, 1, 4], [4, 2, 1, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
board_c = [[3, 2, 4, 1], [2, 3, 2, 4], [1, 4, 1, 3], [4, 3, 1, 2]]
board_d = [[1, 2, 3, 4], [4, 2, 1, 1], [2, 3, 4, 3], [3, 4, 1, 2]]

brrr = [[1, 2, 3, 4, 3, 2, 1, 4], [4, 3, 1, 1, 4, 2, 1, 3], [3, 4, 2, 2, 1, 4, 3, 2], [2, 1, 4, 3, 2, 3, 4, 1], [3, 2, 4, 1, 3, 2, 4, 1], [2, 3, 2, 4, 2, 3, 2, 4], [1, 4, 1, 3, 1, 4, 1, 3], [4, 3, 1, 2, 4, 3, 1, 2]]
