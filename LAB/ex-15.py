"""Tic-Tac-Toe alpha-beta pruning: choose an optimal move for X."""
LINES = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def winner(board):
    for a,b,c in LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def alphabeta(board, maximizing, alpha, beta):
    result = winner(board)
    if result == "X": return 1
    if result == "O": return -1
    if " " not in board: return 0
    if maximizing:
        value = -float("inf")
        for i, cell in enumerate(board):
            if cell == " ":
                board[i] = "X"
                value = max(value, alphabeta(board, False, alpha, beta))
                board[i] = " "
                alpha = max(alpha, value)
                if alpha >= beta: break
        return value
    value = float("inf")
    for i, cell in enumerate(board):
        if cell == " ":
            board[i] = "O"
            value = min(value, alphabeta(board, True, alpha, beta))
            board[i] = " "
            beta = min(beta, value)
            if alpha >= beta: break
    return value

def best_move(board):
    best_score, move = -float("inf"), None
    for i, cell in enumerate(board):
        if cell == " ":
            board[i] = "X"
            score = alphabeta(board, False, -float("inf"), float("inf"))
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    return move, best_score

if __name__ == "__main__":
    board = [" "] * 9
    move, score = best_move(board)
    print("Board: empty")
    print("Alpha-beta chooses square:", move + 1)
    print("Score for X:", score)
