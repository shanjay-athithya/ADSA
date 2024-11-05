def safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row,-1,-1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row,-1,-1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True
    
def check(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1
            if check(board, row + 1, n):
                return True
            board[row][col] = 0
    return False
    
def nqueen(n):
    board = [[0] *n for i in range(n)]
    if check(board, 0, n):
        print(board)
        
if __name__ == '__main__':
    q = nqueen(4)
    
    
    