from src.feature_extraction.utils import Feature
from src.feature_extraction.normal_features.features import Normal_Features
import operator
import numpy as np
import collections
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
        sorted_dict = collections.OrderedDict()
        for m_id, movie in self.movies.iteritems():
            if movie["year"] >= 1995:
                temp[m_id] = movie["year"]
        for key in sorted(temp.items(), key=operator.itemgetter(1)):
            sorted_dict[key[0]] = key[1]
        return sorted_dict

    def movies_per_year(self, year, feature_type="exact"):
        feature_dict = dict()
        f1 = self.nf.avg_team_aggregate_value(year, feature_type, "rating")
        for key, y in self.sorted_movies:
            if y == year:
                feature_dict[key] = f1[key]

    def create_target_vector(self):
        y = []
        for key in self.sorted_movies.keys():
            rounded = int(round(self.movies[key]["rating"]))
            y.append(rounded)
        return np.array(y)


k = Feature_Extraction()
k.create_target_vector()
