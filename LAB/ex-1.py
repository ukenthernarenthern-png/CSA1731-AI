"""Breadth-first search for an unweighted graph."""
from collections import deque


def bfs(graph, start, goal):
    """Return the shortest path (in number of edges), or None if unreachable."""
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path))

        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None


if __name__ == "__main__":
    # An undirected graph represented by adjacency lists.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    start, goal = "A", "F"
    path = bfs(graph, start, goal)
    print("BFS shortest path:", " -> ".join(path) if path else "No path found")
