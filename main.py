import pickle
from src.feature_extraction.extraction_skeleton import feature_extraction


if __name__ == "__main__":
    movies = pickle.load(open('dicts/movies.p', 'rb'))
    # feature extraction
    train, test = feature_extraction(movies)

    # machine learning
