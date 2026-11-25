"""Solve the Australia map-coloring CSP with backtracking."""
REGIONS = ("WA", "NT", "SA", "Q", "NSW", "V")
COLORS = ("Red", "Green", "Blue")
NEIGHBORS = {
    "WA": ("NT", "SA"), "NT": ("WA", "SA", "Q"),
    "SA": ("WA", "NT", "Q", "NSW", "V"),
    "Q": ("NT", "SA", "NSW"), "NSW": ("Q", "SA", "V"),
    "V": ("SA", "NSW"),
}


def consistent(region, color, assignment):
    return all(assignment.get(other) != color for other in NEIGHBORS[region])


def backtrack(assignment):
    if len(assignment) == len(REGIONS):
        return assignment
    region = next(r for r in REGIONS if r not in assignment)
    for color in COLORS:
        if consistent(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[region]
    return None


if __name__ == "__main__":
    solution = backtrack({})
    if solution:
        for region in REGIONS:
            print(f"{region}: {solution[region]}")
    else:
        print("No coloring exists")
