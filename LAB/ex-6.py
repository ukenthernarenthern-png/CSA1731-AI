from collections import deque

TOTAL_M = 3
TOTAL_C = 3
BOAT_CAPACITY = 2
START = (3, 3, 1)  # missionaries left, cannibals left, boat on left
GOAL = (0, 0, 0)


def safe(m, c):
    return 0 <= m <= TOTAL_M and 0 <= c <= TOTAL_C and (m == 0 or m >= c)


def neighbors(state):
    m, c, boat_left = state
    direction = -1 if boat_left else 1
    for move_m in range(BOAT_CAPACITY + 1):
        for move_c in range(BOAT_CAPACITY + 1 - move_m):
            if move_m + move_c == 0:
                continue
            next_m = m + direction * move_m
            next_c = c + direction * move_c
            right_m, right_c = TOTAL_M - next_m, TOTAL_C - next_c
            if safe(next_m, next_c) and safe(right_m, right_c):
                yield (next_m, next_c, 1 - boat_left)


def solve():
    queue = deque([START])
    parent = {START: None}
    while queue:
        state = queue.popleft()
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path))
        for nxt in neighbors(state):
            if nxt not in parent:
                parent[nxt] = state
                queue.append(nxt)
    return None


if __name__ == "__main__":
    path = solve()
    if path:
        print(f"Solution found in {len(path) - 1} crossings")
        print("All missionaries and cannibals reached the right bank")
    else:
        print("No solution")
