"""Reduce the Iris dataset to two principal components."""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    features = load_iris().data
    scaled = StandardScaler().fit_transform(features)
    model = PCA(n_components=2)
    reduced = model.fit_transform(scaled)
    print("Original shape:", features.shape)
    print("Reduced shape:", reduced.shape)
    print("Explained variance ratio:", [round(v, 3) for v in model.explained_variance_ratio_])
