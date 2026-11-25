"""Solve an 8-puzzle with breadth-first search (0 represents the blank)."""
from collections import deque
from math import isqrt


def is_solvable(state):
    """For a 3x3 board, a state is solvable when its inversion count is even."""
    values = [tile for tile in state if tile != 0]
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return inversions % 2 == 0


def neighbors(state):
    size = isqrt(len(state))
    blank = state.index(0)
    row, col = divmod(blank, size)
    for dr, dc, move in ((-1, 0, "Up"), (1, 0, "Down"),
                         (0, -1, "Left"), (0, 1, "Right")):
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            other = nr * size + nc
            board = list(state)
            board[blank], board[other] = board[other], board[blank]
            yield tuple(board), move


def solve(start):
    """Return a shortest list of blank moves, or None when unsolvable."""
    start = tuple(start)
    goal = tuple(range(1, len(start))) + (0,)
    if len(start) != 9 or set(start) != set(range(9)):
        raise ValueError("The board must contain each number 0 through 8 once.")
    if not is_solvable(start):
        return None

    queue = deque([start])
    parent = {start: (None, None)}
    while queue:
        state = queue.popleft()
        if state == goal:
            moves = []
            while parent[state][0] is not None:
                previous, move = parent[state]
                moves.append(move)
                state = previous
            return list(reversed(moves))
        for next_state, move in neighbors(state):
            if next_state not in parent:
                parent[next_state] = (state, move)
                queue.append(next_state)
    return None


if __name__ == "__main__":
    initial = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)
    solution = solve(initial)
    if solution is None:
        print("The puzzle is unsolvable.")
    else:
        print("Moves:", solution)
        print("Number of moves:", len(solution))
