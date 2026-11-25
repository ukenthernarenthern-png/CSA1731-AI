"""Build a small categorical decision tree using ID3 information gain."""
from collections import Counter
from math import log2

DATA = [
    {"Outlook":"Sunny", "Humidity":"High", "Wind":"Weak", "Play":"No"},
    {"Outlook":"Sunny", "Humidity":"High", "Wind":"Strong", "Play":"No"},
    {"Outlook":"Overcast", "Humidity":"High", "Wind":"Weak", "Play":"Yes"},
    {"Outlook":"Rain", "Humidity":"High", "Wind":"Weak", "Play":"Yes"},
    {"Outlook":"Rain", "Humidity":"Normal", "Wind":"Weak", "Play":"Yes"},
    {"Outlook":"Rain", "Humidity":"Normal", "Wind":"Strong", "Play":"No"},
    {"Outlook":"Overcast", "Humidity":"Normal", "Wind":"Strong", "Play":"Yes"},
    {"Outlook":"Sunny", "Humidity":"High", "Wind":"Weak", "Play":"No"},
]
TARGET = "Play"

def entropy(rows):
    counts = Counter(row[TARGET] for row in rows)
    total = len(rows)
    return -sum((n/total) * log2(n/total) for n in counts.values())

def majority(rows):
    return Counter(row[TARGET] for row in rows).most_common(1)[0][0]

def id3(rows, attributes):
    labels = {row[TARGET] for row in rows}
    if len(labels) == 1: return labels.pop()
    if not attributes: return majority(rows)
    base = entropy(rows)
    def gain(attribute):
        groups = {}
        for row in rows: groups.setdefault(row[attribute], []).append(row)
        return base - sum(len(group)/len(rows)*entropy(group) for group in groups.values())
    best = max(attributes, key=gain)
    tree = {best:{}}
    remaining = [a for a in attributes if a != best]
    for value in sorted({row[best] for row in rows}):
        subset = [row for row in rows if row[best] == value]
        tree[best][value] = id3(subset, remaining)
    return tree

def predict(tree, sample):
    while isinstance(tree, dict):
        attribute = next(iter(tree))
        tree = tree[attribute].get(sample.get(attribute), majority(DATA))
    return tree

if __name__ == "__main__":
    tree = id3(DATA, ["Outlook", "Humidity", "Wind"])
    print("Root attribute:", next(iter(tree)))
    print("Prediction for Sunny, High humidity:", predict(tree, {"Outlook":"Sunny", "Humidity":"High", "Wind":"Weak"}))
