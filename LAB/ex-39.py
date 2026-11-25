"""Binary classification with a linear support vector machine."""
from sklearn.svm import SVC

if __name__ == "__main__":
    features = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 7], [8, 6]]
    labels = [0, 0, 0, 1, 1, 1]
    model = SVC(kernel="linear", C=1.0)
    model.fit(features, labels)
    print("Predicted class:", model.predict([[2.5, 2.5]])[0])
