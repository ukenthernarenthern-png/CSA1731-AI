from collections import deque


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
        "D": [], "E": [], "F": [],
    }
    print("BFS traversal:", " -> ".join(bfs(graph, "A")))
