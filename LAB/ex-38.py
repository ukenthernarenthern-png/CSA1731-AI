"""Genetic algorithm maximizing f(x) = -(x - 3)^2 + 9."""
import random

BITS = 8
POPULATION_SIZE = 40
GENERATIONS = 60

def decode(chromosome):
    value = int(chromosome, 2)
    return -5 + 10 * value / (2**BITS - 1)

def fitness(chromosome):
    x = decode(chromosome)
    return -(x - 3) ** 2 + 9

def crossover(parent_a, parent_b):
    point = random.randrange(1, BITS)
    return parent_a[:point] + parent_b[point:], parent_b[:point] + parent_a[point:]

def mutate(chromosome, rate=0.02):
    bits = list(chromosome)
    for i in range(BITS):
        if random.random() < rate:
            bits[i] = "1" if bits[i] == "0" else "0"
    return "".join(bits)

def optimize():
    random.seed(7)
    population = [format(random.randrange(2**BITS), f"0{BITS}b")
                  for _ in range(POPULATION_SIZE)]
    for _ in range(GENERATIONS):
        population.sort(key=fitness, reverse=True)
        next_generation = population[:2]  # elitism
        while len(next_generation) < POPULATION_SIZE:
            parent_a, parent_b = random.choices(population[:20], k=2)
            child_a, child_b = crossover(parent_a, parent_b)
            next_generation.extend((mutate(child_a), mutate(child_b)))
        population = next_generation[:POPULATION_SIZE]
    best = max(population, key=fitness)
    return decode(best), fitness(best)

if __name__ == "__main__":
    x, score = optimize()
    print(f"Best x: {x:.3f}")
    print(f"Best fitness: {score:.3f}")
