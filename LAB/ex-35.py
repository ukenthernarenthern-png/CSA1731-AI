"""Classify a simple binary dataset with a decision tree."""
from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":
    features = [[0, 0], [0, 1], [1, 0], [1, 1]]
    labels = [0, 0, 0, 1]  # AND classification
    model = DecisionTreeClassifier(criterion="entropy", random_state=0)
    model.fit(features, labels)
    sample = [[1, 1]]
    print("Predicted class:", model.predict(sample)[0])
