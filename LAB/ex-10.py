from itertools import permutations


# Symmetric distances between four cities
CITIES = ("A", "B", "C", "D")
DISTANCE = {
    ("A", "B"): 10, ("A", "C"): 15, ("A", "D"): 20,
    ("B", "C"): 35, ("B", "D"): 25, ("C", "D"): 30,
}


def distance(city1, city2):
    return DISTANCE.get((city1, city2), DISTANCE.get((city2, city1), 0))


def solve_tsp():
    start = CITIES[0]
    best_route = None
    best_cost = float("inf")
    for rest in permutations(CITIES[1:]):
        route = (start,) + rest + (start,)
        cost = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
        if cost < best_cost:
            best_route, best_cost = route, cost
    return best_route, best_cost


if __name__ == "__main__":
    route, cost = solve_tsp()
    print("Best tour:", " -> ".join(route))
    print("Total distance:", cost)
