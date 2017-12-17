from src.feature_extraction.utils import Feature
from src.feature_extraction.normal_features.features import Normal_Features
import operator
import numpy as np
import math

class Feature_Extraction:

    def __init__(self):
        self.f = Feature()
        self.movies = self.f.movies
        self.sorted_movies = self.sort_by_year()
        self.nf = Normal_Features()

    def feature_extraction(self):
        for year in range(1995, 2016):
            self.movies_per_year(1995)

            # print self.movies[m_id[0]]

    def sort_by_year(self):
        temp = dict()
        for key, value in sorted(self.movies.iteritems(), key=lambda (k, v): (v, k)):
            print "%s: %s" % (movies[key]['name'], value)


        for m_id, movie in self.movies.iteritems():
            if movie["year"] >= 1995:
                temp[m_id] = movie["year"]

        return sorted(temp.items(), key=operator.itemgetter(1))

    def movies_per_year(self, year, feature_type="exact"):

        print self.nf.avg_team_aggregate_value(year, feature_type, "rating")

        for m_id in self.sorted_movies:


    def create_target_vector(self):
        y = []
        for t in self.sorted_movies:
            id = t[0]
            rounded = int(round(self.movies[id]["rating"]))
            y.append(rounded)
        return np.array(y)


k = Feature_Extraction()
k.movies_per_year(1995)
