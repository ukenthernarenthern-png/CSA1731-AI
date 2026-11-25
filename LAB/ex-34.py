"""Classify a point with the k-nearest neighbors algorithm."""
from math import sqrt
from collections import Counter


def predict(train_points, train_labels, query, k=3):
    distances = []
    for point, label in zip(train_points, train_labels):
        distance = sqrt(sum((a - b) ** 2 for a, b in zip(point, query)))
        distances.append((distance, label))
    nearest = sorted(distances)[:k]
    return Counter(label for _, label in nearest).most_common(1)[0][0]

if __name__ == "__main__":
    points = [(1, 1), (1.5, 2), (3, 3), (5, 4)]
    labels = ["Red", "Blue", "Blue", "Red"]
    print("Predicted class:", predict(points, labels, (2, 2), k=3))
