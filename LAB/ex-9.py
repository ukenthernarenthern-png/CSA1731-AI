def dfs(graph, start):
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
        "D": [], "E": [], "F": [],
    }
    print("DFS traversal:", " -> ".join(dfs(graph, "A")))
