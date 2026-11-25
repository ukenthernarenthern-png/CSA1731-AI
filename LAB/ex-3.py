"""Find and display one solution to the 8-queens problem."""


def solve_queens(size=8):
    """Return a list where result[row] is the queen's column in that row."""
    placement = [-1] * size
    columns = set()
    descending_diagonals = set()  # row - column
    ascending_diagonals = set()   # row + column

    def place(row):
        if row == size:
            return True
        for col in range(size):
            if (col in columns or row - col in descending_diagonals
                    or row + col in ascending_diagonals):
                continue
            placement[row] = col
            columns.add(col)
            descending_diagonals.add(row - col)
            ascending_diagonals.add(row + col)
            if place(row + 1):
                return True
            columns.remove(col)
            descending_diagonals.remove(row - col)
            ascending_diagonals.remove(row + col)
        return False

    return placement if place(0) else None


def display(board):
    for queen_col in board:
        print(" ".join("Q" if col == queen_col else "."
                      for col in range(len(board))))


if __name__ == "__main__":
    solution = solve_queens()
    if solution is None:
        print("No solution found.")
    else:
        print("One 8-queens solution (Q = queen):")
        display(solution)
