"""Two-player console Tic-Tac-Toe."""

def show(board):
    for row in range(3):
        print(" | ".join(board[row * 3:row * 3 + 3]))
        if row < 2:
            print("---------")


def winner(board):
    lines = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def play():
    board = [" "] * 9
    player = "X"
    while not winner(board) and " " in board:
        show(board)
        try:
            position = int(input(f"Player {player}, choose a square (1-9): ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue
        if position not in range(9) or board[position] != " ":
            print("That square is unavailable. Try again.")
            continue
        board[position] = player
        player = "O" if player == "X" else "X"
    show(board)
    result = winner(board)
    print(f"Player {result} wins!" if result else "It is a draw.")


if __name__ == "__main__":
    play()
