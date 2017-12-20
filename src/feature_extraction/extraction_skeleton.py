from src.feature_extraction.utils import Feature
from src.feature_extraction.normal_features.features import Normal_Features
from src.feature_extraction.graph_features.centrality import Centrality
import operator
import numpy as np
import collections
import os
import pickle
project_folder = os.path.dirname(__file__).split("src")[0]

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
            self.simple_features_movies_per_year(year)
        self.save_feature_matrix('first')
        for year in range(1996, 2016):
            self.complex_features_movies_per_year(year)
        self.save_feature_matrix('second')
        for year in range(1996, 2016):
            self.very_complex_features_movies_per_year(year)
        self.save_feature_matrix('third')
        for year in range(1996,2016):
            self.very_very_complex_features_movies_per_year(year)
        self.save_feature_matrix('last')

        print len(self.feature_matrix[len(self.feature_matrix) - 1])
        print len(self.feature_matrix)
        print self.count

    def save_feature_matrix(self , name):
        fm = np.array(self.feature_matrix)
        pickle.dump(fm, open(project_folder + 'dicts/' + name + '.p', 'wb'))
        fm = pickle.load(open(project_folder + 'dicts/' + name + '.p', 'rb'))
        print name, " has been created: " + str(len(fm))

    def sort_by_year(self):
        temp = dict()
        sorted_dict = collections.OrderedDict()
        for m_id, movie in self.movies.iteritems():
            if movie["year"] >= 1996 and movie['year'] <= 2015:
                temp[m_id] = movie["year"]
        for key in sorted(temp.items(), key=operator.itemgetter(1)):
            sorted_dict[key[0]] = key[1]
        return sorted_dict

    def simple_features_movies_per_year(self, year):
        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[0]
        self.add_to_feature_matrix(feature_dict , year , 0)
        self.feature_names[0] = 'previous exact cast rating'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "rating")[1]
        self.add_to_feature_matrix(feature_dict,year,1)
        self.feature_names[1] = 'previous exact crew rating'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "revenue")[0]
        self.add_to_feature_matrix(feature_dict , year , 2)
        self.feature_names[2] = 'previous exact cast revenue'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'exact', "revenue")[1]
        self.add_to_feature_matrix(feature_dict, year, 3)
        self.feature_names[3] = 'previous exact crew revenue'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "rating")[0]
        self.add_to_feature_matrix(feature_dict, year, 4)
        self.feature_names[4] = 'previous till cast rating'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "rating")[1]
        self.add_to_feature_matrix(feature_dict, year, 5)
        self.feature_names[5] = 'previous till crew rating'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "revenue")[0]
        self.add_to_feature_matrix(feature_dict, year, 6)
        self.feature_names[6] = 'previous till cast revenue'

        feature_dict = self.nf.avg_team_aggregate_value(year, 'till', "revenue")[1]
        self.add_to_feature_matrix(feature_dict, year, 7)
        self.feature_names[7] = 'previous till crew revenue'


        feature_dict = self.nf.avg_previous_team_individual_experience(year, 'exact')[0]
        self.add_to_feature_matrix(feature_dict, year, 8)
        self.feature_names[8] = 'previous exact cast individual experience'

        feature_dict = self.nf.avg_previous_team_individual_experience(year, 'exact')[1]
        self.add_to_feature_matrix(feature_dict, year, 9)
        self.feature_names[9] = 'previous exact crew individual experience'

        feature_dict = self.nf.avg_previous_team_individual_experience(year, 'till')[0]
        self.add_to_feature_matrix(feature_dict, year, 10)
        self.feature_names[10] = 'previous till cast individual experience'

        feature_dict = self.nf.avg_previous_team_individual_experience(year, 'till')[1]
        self.add_to_feature_matrix(feature_dict, year, 11)
        self.feature_names[11] = 'previous till crew individual experience'


        feature_dict = self.nf.team_size(year)[0]
        self.add_to_feature_matrix(feature_dict, year, 12)
        self.feature_names[12] = 'cast size'

        feature_dict = self.nf.team_size(year)[1]
        self.add_to_feature_matrix(feature_dict, year, 13)
        self.feature_names[13] = 'crew size'

        feature_dict = self.nf.team_tenure(year, 'exact')[0]
        self.add_to_feature_matrix(feature_dict, year, 14)
        self.feature_names[14] = 'cast exact tenure'

        feature_dict = self.nf.team_tenure(year,  'exact')[1]
        self.add_to_feature_matrix(feature_dict, year, 15)
        self.feature_names[15] = 'crew exact tenure'

        feature_dict = self.nf.team_tenure(year, 'till')[0]
        self.add_to_feature_matrix(feature_dict, year, 16)
        self.feature_names[16] = 'cast tenure till'

        feature_dict = self.nf.team_tenure(year, 'till')[1]
        self.add_to_feature_matrix(feature_dict, year, 17)
        self.feature_names[17] = 'crew tenure till'

        feature_dict = self.nf.average_team_combined_stats(year, 'experience')
        self.add_to_feature_matrix(feature_dict, year, 18)
        self.feature_names[18] = 'dyads previous experience'

        feature_dict = self.nf.average_team_combined_stats(year, 'rating')
        self.add_to_feature_matrix(feature_dict, year, 19)
        self.feature_names[19] = 'dyads previous rating'

        feature_dict = self.nf.average_team_combined_stats(year, 'revenue')
        self.add_to_feature_matrix(feature_dict, year, 20)
        self.feature_names[20] = 'dyads previous revenue'


        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "degree")
        self.add_to_feature_matrix(feature_dict, year, 21)
        self.feature_names[21] = 'previous exact cast degree centrality'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "degree")
        self.add_to_feature_matrix(feature_dict, year, 22)
        self.feature_names[22] = 'previous exact crew degree centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "degree")
        self.add_to_feature_matrix(feature_dict, year, 23)
        self.feature_names[23] = 'previous till cast degree centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "degree")
        self.add_to_feature_matrix(feature_dict, year, 24)
        self.feature_names[24] = 'previous till crew degree centrality'

        #######################################################
        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "pagerank")
        self.add_to_feature_matrix(feature_dict, year, 25)
        self.feature_names[25] = 'previous exact cast pagerank'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "pagerank")
        self.add_to_feature_matrix(feature_dict, year, 26)
        self.feature_names[26] = 'previous exact crew pagerank'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "pagerank")
        self.add_to_feature_matrix(feature_dict, year, 27)
        self.feature_names[27] = 'previous till cast pagerank'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "pagerank")
        self.add_to_feature_matrix(feature_dict, year, 28)
        self.feature_names[28] = 'previous till crew pagerank'
        ####################################################

        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "eigentrust")
        self.add_to_feature_matrix(feature_dict, year, 29)
        self.feature_names[29] = 'previous exact cast eigentrust'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "eigentrust")
        self.add_to_feature_matrix(feature_dict, year, 30)
        self.feature_names[30] = 'previous exact crew eigentrust'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "eigentrust")
        self.add_to_feature_matrix(feature_dict, year, 31)
        self.feature_names[31] = 'previous till cast eigentrust'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "eigentrust")
        self.add_to_feature_matrix(feature_dict, year, 32)
        self.feature_names[32] = 'previous till crew eigentrust'
        ###################################################
        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "cc")
        self.add_to_feature_matrix(feature_dict, year, 33)
        self.feature_names[33] = 'previous exact cast clustering coefficient'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "cc")
        self.add_to_feature_matrix(feature_dict, year, 34)
        self.feature_names[34] = 'previous exact crew clustering coefficient'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "cc")
        self.add_to_feature_matrix(feature_dict, year, 35)
        self.feature_names[35] = 'previous till cast clustering coefficient'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "cc")
        self.add_to_feature_matrix(feature_dict, year, 36)
        self.feature_names[36] = 'previous till crew clustering coefficient'
        ######################################################


    def complex_features_movies_per_year(self, year):

        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "closeness")
        self.add_to_feature_matrix(feature_dict, year, 37)
        self.feature_names[37] = 'previous exact cast closeness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "closeness")
        self.add_to_feature_matrix(feature_dict, year, 38)
        self.feature_names[38] = 'previous exact crew closeness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "closeness")
        self.add_to_feature_matrix(feature_dict, year, 39)
        self.feature_names[39] = 'previous till cast closeness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "closeness")
        self.add_to_feature_matrix(feature_dict, year, 40)
        self.feature_names[40] = 'previous till crew closeness centrality'

    def very_complex_features_movies_per_year(self, year):

        feature_dict = self.gf.avg_team_centrality(year, "exact", "actors", "betweenness")
        self.add_to_feature_matrix(feature_dict, year, 41)
        self.feature_names[41] = 'previous exact cast betweenness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "exact", "crew", "betweenness")
        self.add_to_feature_matrix(feature_dict, year, 42)
        self.feature_names[42] = 'previous exact crew betweenness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "actors", "betweenness")
        self.add_to_feature_matrix(feature_dict, year, 43)
        self.feature_names[43] = 'previous till cast betweenness centrality'

        feature_dict = self.gf.avg_team_centrality(year, "till", "crew", "betweenness")
        self.add_to_feature_matrix(feature_dict, year, 44)
        self.feature_names[44] = 'previous till crew betweenness centrality'

    def very_very_complex_features_movies_per_year(self, year):
        value = self.gf.small_world_coefficient(year , 'exact' , 'actors')[0]
        self.add_to_feature_matrix_small_world(value, year , 45)
        self.feature_names[45] = 'Previous cast exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'actors')[1]
        self.add_to_feature_matrix_small_world(value, year, 46)
        self.feature_names[46] = 'Previous cast exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'actors')[2]
        self.add_to_feature_matrix_small_world(value, year, 47)
        self.feature_names[47] = 'Previous cast exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'actors')[3]
        self.add_to_feature_matrix_small_world(value, year, 48)
        self.feature_names[48] = 'Previous cast exact gcc'
        #################################################################3

        value = self.gf.small_world_coefficient(year, 'till', 'actors')[0]
        self.add_to_feature_matrix_small_world(value, year, 49)
        self.feature_names[49] = 'Previous cast till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'actors')[1]
        self.add_to_feature_matrix_small_world(value, year, 50)
        self.feature_names[50] = 'Previous cast till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'actors')[2]
        self.add_to_feature_matrix_small_world(value, year, 51)
        self.feature_names[51] = 'Previous cast till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'actors')[3]
        self.add_to_feature_matrix_small_world(value, year, 52)
        self.feature_names[52] = 'Previous cast till gcc'
        ###############################################################

        value = self.gf.small_world_coefficient(year, 'exact', 'crew')[0]
        self.add_to_feature_matrix_small_world(value, year, 53)
        self.feature_names[53] = 'Previous crew exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'crew')[1]
        self.add_to_feature_matrix_small_world(value, year, 54)
        self.feature_names[54] = 'Previous crew exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'crew')[2]
        self.add_to_feature_matrix_small_world(value, year, 55)
        self.feature_names[55] = 'Previous crew exact gcc'

        value = self.gf.small_world_coefficient(year, 'exact', 'crew')[3]
        self.add_to_feature_matrix_small_world(value, year, 56)
        self.feature_names[56] = 'Previous crew exact gcc'
        #################################################################
        value = self.gf.small_world_coefficient(year, 'till', 'crew')[0]
        self.add_to_feature_matrix_small_world(value, year, 57)
        self.feature_names[57] = 'Previous crew till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'crew')[1]
        self.add_to_feature_matrix_small_world(value, year, 58)
        self.feature_names[58] = 'Previous crew till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'crew')[2]
        self.add_to_feature_matrix_small_world(value, year, 59)
        self.feature_names[59] = 'Previous crew till gcc'

        value = self.gf.small_world_coefficient(year, 'till', 'crew')[3]
        self.add_to_feature_matrix_small_world(value, year, 60)
        self.feature_names[60] = 'Previous crew till gcc'

        

    def add_to_feature_matrix_small_world(self, value , year , index):
       feature = []
       for key, y in self.sorted_movies.iteritems():
           if y == year:
               try:
                   feature.append(value)
               except Exception as e:
                   feature.append(0)
       if year == 1996:
           self.feature_matrix.append(feature)
       else:
           self.feature_matrix[index].extend(feature)


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

    def create_target_vector_3_class(self):
        y = []
        for key in self.sorted_movies.keys():
            if 5 >= self.movies[key]["rating"] >= 0:
                y.append(1)
            elif 7 >= self.movies[key]["rating"] >= 5.1:
                y.append(2)
            elif 15 >= self.movies[key]["rating"] >= 7.1:
                y.append(3)
        return np.array(y)

    def create_target_vector(self):
        y = []
        for key in self.sorted_movies.keys():
            rounded = int(round(self.movies[key]["rating"]))
            y.append(rounded)
        return np.array(y)

    def create_target_vector_regression_rating(self):
        y = []
        for key in self.sorted_movies.keys():
            y.append(self.movies[key]['rating'])
        pickle.dump(np.array(y), open(project_folder + 'dicts/' + 'ratings' + '.p', 'wb'))
        return np.array(y)

    def create_feature_names(self):
        pickle.dump(self.feature_names, open(project_folder + 'dicts/' + 'feature_names' + '.p', 'wb'))
        return self.feature_names


k = Feature_Extraction()
#k.feature_extraction()
print len(k.create_target_vector())
y = k.create_target_vector_5_class()
pickle.dump(y, open(project_folder + 'dicts/' + '5classes' + '.p', 'wb'))

# y = pickle.load(open(project_folder + 'dicts/' + 'roundedratings' + '.p', 'rb'))
# print  " has been created: " + str(len(y))

#k.feature_extraction()