from src.feature_extraction.utils import Feature
from src.feature_extraction.normal_features.features import Normal_Features
from src.feature_extraction.graph_features.centrality import Centrality
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
        self.gf = Centrality()
        self.feature_matrix = []
        self.feature_names = {}
        self.count = 0

    def feature_extraction(self):
        for year in range(1996, 2016):
            self.movies_per_year(year)
        print len(self.feature_matrix[len(self.feature_matrix) - 1])
        print len(self.feature_matrix)
        print self.count


    def sort_by_year(self):
        temp = dict()
        sorted_dict = collections.OrderedDict()
        for m_id, movie in self.movies.iteritems():
            if movie["year"] >= 1996 and movie['year'] <= 2015:
                temp[m_id] = movie["year"]
        for key in sorted(temp.items(), key=operator.itemgetter(1)):
            sorted_dict[key[0]] = key[1]
        return sorted_dict

    def movies_per_year(self, year):
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[0]
        # self.add_to_feature_matrix(feature_dict , year , 0)
        # self.feature_names[0] = 'previous exact cast rating'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[1]
        # self.add_to_feature_matrix(feature_dict,year,1)
        # self.feature_names[1] = 'previous exact crew rating'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "revenue")[0]
        # self.add_to_feature_matrix(feature_dict , year , 2)
        # self.feature_names[2] = 'previous exact cast revenue'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "revenue")[1]
        # self.add_to_feature_matrix(feature_dict, year, 3)
        # self.feature_names[3] = 'previous exact crew revenue'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "rating")[0]
        # self.add_to_feature_matrix(feature_dict, year, 4)
        # self.feature_names[4] = 'previous till cast rating'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "rating")[1]
        # self.add_to_feature_matrix(feature_dict, year, 5)
        # self.feature_names[5] = 'previous till crew rating'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "revenue")[0]
        # self.add_to_feature_matrix(feature_dict, year, 6)
        # self.feature_names[6] = 'previous till cast revenue'
        #
        # feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "revenue")[1]
        # self.add_to_feature_matrix(feature_dict, year, 7)
        # self.feature_names[7] = 'previous till crew revenue'
        #
        #
        # feature_dict = self.nf.avg_previous_team_individual_experience(year, 'exact')[0]
        # self.add_to_feature_matrix(feature_dict, year, 8)
        # self.feature_names[8] = 'previous exact cast individual experience'
        #
        # feature_dict = self.nf.avg_previous_team_individual_experience(year, 'exact')[1]
        # self.add_to_feature_matrix(feature_dict, year, 9)
        # self.feature_names[9] = 'previous exact crew individual experience'
        #
        # feature_dict = self.nf.avg_previous_team_individual_experience(year, 'till')[0]
        # self.add_to_feature_matrix(feature_dict, year, 10)
        # self.feature_names[10] = 'previous till cast individual experience'
        #
        # feature_dict = self.nf.avg_previous_team_individual_experience(year, 'till')[1]
        # self.add_to_feature_matrix(feature_dict, year, 11)
        # self.feature_names[11] = 'previous till crew individual experience'
        #
        # feature_dict = self.nf.team_size(year)[0]
        # self.add_to_feature_matrix(feature_dict, year, 12)
        # self.feature_names[12] = 'cast size'
        #
        # feature_dict = self.nf.team_size(year)[1]
        # self.add_to_feature_matrix(feature_dict, year, 13)
        # self.feature_names[13] = 'crew size'
        #
        # feature_dict = self.nf.team_tenure(year, 'exact')[0]
        # self.add_to_feature_matrix(feature_dict, year, 14)
        # self.feature_names[14] = 'cast exact tenure'
        #
        # feature_dict = self.nf.team_size(year,  'exact')[1]
        # self.add_to_feature_matrix(feature_dict, year, 15)
        # self.feature_names[15] = 'crew exact tenure'
        #
        # feature_dict = self.nf.team_tenure(year, 'till')[0]
        # self.add_to_feature_matrix(feature_dict, year, 16)
        # self.feature_names[16] = 'cast tenure till'
        #
        # feature_dict = self.nf.team_size(year, 'till')[1]
        # self.add_to_feature_matrix(feature_dict, year, 17)
        # self.feature_names[17] = 'crew tenure till'
        #
        # feature_dict = self.nf.average_team_combined_stats(year, 'experience')
        # self.add_to_feature_matrix(feature_dict, year, 18)
        # self.feature_names[18] = 'dyads previous experience'
        #
        # feature_dict = self.nf.average_team_combined_stats(year, 'rating')
        # self.add_to_feature_matrix(feature_dict, year, 19)
        # self.feature_names[19] = 'dyads previous rating'
        #
        # feature_dict = self.nf.average_team_combined_stats(year, 'revenue')
        # self.add_to_feature_matrix(feature_dict, year, 20)
        # self.feature_names[20] = 'dyads previous revenue'
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "degree")
        # self.add_to_feature_matrix(feature_dict, year, 0)
        # self.feature_names[0] = 'previous exact cast degree centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "degree")
        # self.add_to_feature_matrix(feature_dict, year, 1)
        # self.feature_names[1] = 'previous exact crew degree centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "degree")
        # self.add_to_feature_matrix(feature_dict, year, 2)
        # self.feature_names[2] = 'previous till cast degree centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "degree")
        # self.add_to_feature_matrix(feature_dict, year, 3)
        # self.feature_names[3] = 'previous till crew degree centrality'
        #
        # #######################################################
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "pagerank")
        # self.add_to_feature_matrix(feature_dict, year, 4)
        # self.feature_names[4] = 'previous exact cast pagerank'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "pagerank")
        # self.add_to_feature_matrix(feature_dict, year, 5)
        # self.feature_names[5] = 'previous exact crew pagerank'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "pagerank")
        # self.add_to_feature_matrix(feature_dict, year, 6)
        # self.feature_names[6] = 'previous till cast pagerank'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "pagerank")
        # self.add_to_feature_matrix(feature_dict, year, 7)
        # self.feature_names[7] = 'previous till crew pagerank'
        # ####################################################
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "eigentrust")
        # self.add_to_feature_matrix(feature_dict, year, 8)
        # self.feature_names[8] = 'previous exact cast eigentrust'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "eigentrust")
        # self.add_to_feature_matrix(feature_dict, year, 9)
        # self.feature_names[9] = 'previous exact crew eigentrust'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "eigentrust")
        # self.add_to_feature_matrix(feature_dict, year, 10)
        # self.feature_names[10] = 'previous till cast eigentrust'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "eigentrust")
        # self.add_to_feature_matrix(feature_dict, year, 11)
        # self.feature_names[11] = 'previous till crew eigentrust'
        ####################################################
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "cc")
        # self.add_to_feature_matrix(feature_dict, year, 0)
        # self.feature_names[0] = 'previous exact cast clustering coefficient'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "cc")
        # self.add_to_feature_matrix(feature_dict, year, 1)
        # self.feature_names[1] = 'previous exact crew clustering coefficient'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "cc")
        # self.add_to_feature_matrix(feature_dict, year, 2)
        # self.feature_names[2] = 'previous till cast clustering coefficient'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "cc")
        # self.add_to_feature_matrix(feature_dict, year, 3)
        # self.feature_names[3] = 'previous till crew clustering coefficient'
        #######################################################

        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "closeness")
        # self.add_to_feature_matrix(feature_dict, year, 0)
        # self.feature_names[0] = 'previous exact cast closeness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "closeness")
        # self.add_to_feature_matrix(feature_dict, year, 1)
        # self.feature_names[1] = 'previous exact crew closeness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "closeness")
        # self.add_to_feature_matrix(feature_dict, year, 2)
        # self.feature_names[2] = 'previous till cast closeness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "closeness")
        # self.add_to_feature_matrix(feature_dict, year, 3)
        # self.feature_names[3] = 'previous till crew closeness centrality'

        ########################################################
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "betweenness")
        # self.add_to_feature_matrix(feature_dict, year, 0)
        # self.feature_names[0] = 'previous exact cast betweenness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "betweenness")
        # self.add_to_feature_matrix(feature_dict, year, 1)
        # self.feature_names[1] = 'previous exact crew betweenness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "betweenness")
        # self.add_to_feature_matrix(feature_dict, year, 2)
        # self.feature_names[2] = 'previous till cast betweenness centrality'
        #
        # feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "betweenness")
        # self.add_to_feature_matrix(feature_dict, year, 3)
        # self.feature_names[3] = 'previous till crew betweenness centrality'


        self.add_to_feature_matrix()
        

    def add_to_feature_matrix_small_world(self, year , index):
        print 5

    def add_to_feature_matrix(self, feature_dict, year , index):
        feature = []
        for key, y in self.sorted_movies.iteritems():
            if y == year:
                try:
                    feature.append(feature_dict[key])
                except Exception as e:
                    feature.append(0)
        if year == 1996:
            self.feature_matrix.append(feature)
        else:
            self.feature_matrix[index].extend(feature)

        #print len(self.feature_matrix[0])

    def create_target_vector(self):
        y = []
        for key in self.sorted_movies.keys():
            rounded = int(round(self.movies[key]["rating"]))
            y.append(rounded)
        return np.array(y)


k = Feature_Extraction()
k.feature_extraction()
print len(k.create_target_vector())

