from graph_features.degree_centrality import calculation


def feature_extraction(movies):

    for movie in movies:
        feature_values = list()

        # actors degree centrality
        actors_degree_centrality = calculation(movie["actors"], movie["year"])
        feature_values.append(actors_degree_centrality)

