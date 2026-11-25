"""Recommend unrated items using user-based collaborative filtering."""
from math import sqrt

RATINGS = {
    "Alice": {"Book A": 5, "Book B": 3},
    "Bob": {"Book A": 4, "Book B": 2, "Book C": 5},
    "Cara": {"Book A": 1, "Book B": 5, "Book C": 4},
    "Dan": {"Book B": 4, "Book C": 3},
}

def similarity(ratings_a, ratings_b):
    common = set(ratings_a) & set(ratings_b)
    numerator = sum(ratings_a[item] * ratings_b[item] for item in common)
    norm_a = sqrt(sum(ratings_a[item] ** 2 for item in common))
    norm_b = sqrt(sum(ratings_b[item] ** 2 for item in common))
    return numerator / (norm_a * norm_b) if norm_a and norm_b else 0.0

def recommend(user):
    known = RATINGS[user]
    candidates = {item for ratings in RATINGS.values() for item in ratings} - set(known)
    scores = {}
    for item in candidates:
        weighted_sum = total_weight = 0.0
        for other, ratings in RATINGS.items():
            if other != user and item in ratings:
                weight = similarity(known, ratings)
                weighted_sum += weight * ratings[item]
                total_weight += weight
        if total_weight:
            scores[item] = weighted_sum / total_weight
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)

if __name__ == "__main__":
    print("Recommendations for Alice:")
    for item, score in recommend("Alice"):
        print(f"{item}: predicted rating {score:.2f}")
