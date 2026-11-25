from heapq import heappop, heappush
from itertools import count

GRAPH = {
    "S": {"A": 1, "B": 4},
    "A": {"C": 2, "G": 7},
    "B": {"G": 3},
    "C": {"G": 3},
    "G": {},
}
HEURISTIC = {"S": 5, "A": 4, "B": 3, "C": 3, "G": 0}


def a_star(start, goal):
    sequence = count()
    frontier = [(HEURISTIC[start], next(sequence), start)]
    cost_so_far = {start: 0}
    parent = {start: None}
    while frontier:
        _, _, current = heappop(frontier)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path)), cost_so_far[goal]
        for neighbor, edge_cost in GRAPH[current].items():
            new_cost = cost_so_far[current] + edge_cost
            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current
                priority = new_cost + HEURISTIC[neighbor]
                heappush(frontier, (priority, next(sequence), neighbor))
    return None, float("inf")


if __name__ == "__main__":
    path, cost = a_star("S", "G")
    print("Shortest path:", " -> ".join(path))
    print("Total cost:", cost)
