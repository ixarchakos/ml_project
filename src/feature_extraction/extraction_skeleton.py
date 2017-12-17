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
        self.feature_matrix = []
        self.feature_names = {}

    def feature_extraction(self):
        for year in range(1995, 2016):
            self.movies_per_year(year)
        print len(self.feature_matrix[1])

    def sort_by_year(self):
        temp = dict()
        sorted_dict = collections.OrderedDict()
        for m_id, movie in self.movies.iteritems():
            if movie["year"] >= 1995:
                temp[m_id] = movie["year"]
        for key in sorted(temp.items(), key=operator.itemgetter(1)):
            sorted_dict[key[0]] = key[1]
        return sorted_dict

    def movies_per_year(self, year):
        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[0]
        self.add_to_feature_matrix(feature_dict , year , 0)
        self.feature_names[0] = 'previous exact cast rating'
        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[1]
        self.add_to_feature_matrix(feature_dict,year,1)
        self.feature_names[1] = 'previous exact crew rating'


    def add_to_feature_matrix(self, feature_dict, year , index):
        feature = []
        for key, y in self.sorted_movies.iteritems():
            if y == year:
                
                feature.append(feature_dict[key])
        if year == 1995:
            self.feature_matrix.append(feature)
        else:
            self.feature_matrix[index].append(feature)

    def create_target_vector(self):
        y = []
        for key in self.sorted_movies.keys():
            rounded = int(round(self.movies[key]["rating"]))
            y.append(rounded)
        return np.array(y)


k = Feature_Extraction()
print k.feature_extraction()
