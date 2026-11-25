from collections import deque

CAPACITY_A = 4
CAPACITY_B = 3
TARGET = 2
START = (0, 0)

def successors(state):
    a, b = state
    candidates = [
        (CAPACITY_A, b), (a, CAPACITY_B), (0, b), (a, 0),
        (a - min(a, CAPACITY_B - b), b + min(a, CAPACITY_B - b)),
        (a + min(b, CAPACITY_A - a), b - min(b, CAPACITY_A - a)),
    ]
    return [s for s in candidates if s != state]

def solve():
    queue = deque([START])
    parent = {START: None}
    while queue:
        state = queue.popleft()
        if TARGET in state:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path))
        for next_state in successors(state):
            if next_state not in parent:
                parent[next_state] = state
                queue.append(next_state)
    return None

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Water jug states (A, B):")
        for state in solution:
            print(state)
        print("Goal reached: 2 liters")
    else:
        print("No solution")
