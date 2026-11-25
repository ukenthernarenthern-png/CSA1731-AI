"""Perform basic sentiment analysis with TF-IDF and Naive Bayes."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

if __name__ == "__main__":
    texts = [
        "wonderful story and excellent acting",
        "I loved this enjoyable movie",
        "terrible story and poor acting",
        "I hated this boring movie",
        "the film was excellent and enjoyable",
        "the film was dull and disappointing",
    ]
    labels = ["Positive", "Positive", "Negative", "Negative", "Positive", "Negative"]
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(texts, labels)
    sample = ["excellent and enjoyable story"]
    print("Sentiment:", model.predict(sample)[0])
