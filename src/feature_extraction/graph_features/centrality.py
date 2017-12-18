from graph_tool.all import *
import graph_tool as gt
from src.feature_extraction.utils import Feature, project_folder
import pickle
import os
import numpy as np


class Centrality:

    def __init__(self):
        self.f = Feature()


    def avg_team_centrality(self, year , feature_type = 'exact' ,  cast_crew = 'actors' , centrality = 'closeness'):
        # implement crew
        # implement other centrality measures

        movieids = self.f.load_desired_movies( year , type = 'exact')
        movies = self.f.movies
        # calculations
        if centrality == 'closeness':
            actors_centrality , g = self.closeness(year - 1,feature_type , cast_crew)
        if centrality == 'pagerank':
            actors_centrality , g = self.pagerank(year - 1, feature_type, cast_crew)
        if centrality == 'betweenness':
            actors_centrality, g = self.betweenness(year - 1 , feature_type , cast_crew)
        if centrality == 'eigentrust':
            actors_centrality, g = self.eigentrust(year - 1 , feature_type , cast_crew)
        if centrality == 'pagerankRating':
            actors_centrality , g = self.pagerank_rating(year - 1 , feature_type, cast_crew)
        if centrality == 'cc':
            actors_centrality ,g = self.clusteringCoeff(year -1 , feature_type , cast_crew)
        if centrality == 'degree':
            actors_centrality , g = self.degree(year -1 , feature_type , cast_crew)
        idconvert = self.convert_ids(g)
        actors_converted_centrality = {}
        for i , c in enumerate(actors_centrality):
            actors_converted_centrality[str(idconvert[i])] = c

        # averaging
        movie_centrality = {}
        for mid in movieids:
            sum_centrality = 0.0
            count = 0
            if cast_crew == 'actors':
                for aid in movies[mid]['actors']:
                    if aid in actors_converted_centrality:
                        sum_centrality += actors_converted_centrality[aid]
                        count += 1
            if cast_crew == 'crew':
                for cid in movies[mid]['crew']:
                    if cid in actors_converted_centrality:
                        sum_centrality += actors_converted_centrality[cid]
                        count += 1

            if count > 0:
                movie_centrality[mid] = sum_centrality / count
        # for key, value in sorted(movie_centrality.iteritems(), key=lambda (k, v): (v, k)):
        #     print "%s: %s" % (movies[key]['name'], value)
        return movie_centrality


    def average_pair_trust(self,year, feature_type , cast_crew):
        pass

    def small_world_coefficient(self , year , feature_type , cast_crew):
        gcc ,  gccstd = self.networkCC(year, feature_type , cast_crew)
        avg_shortest_path = self.average_shortest_path(year, feature_type , cast_crew)
        print gcc, gccstd, avg_shortest_path, gcc / avg_shortest_path
        return gcc, gccstd , avg_shortest_path , gcc / avg_shortest_path

    #*****************************************************************************
    def convert_ids(self , g):
        aids = []
        gids = g.vp['id']
        for v in g.vertices():
            aids.append(gids[v])
        return aids

    def average_shortest_path(self,year, feature_type, cast_crew):
        g = self.get_graph_file(year, feature_type, cast_crew)
        weights = g.ep['weight']
        maximum = max(weights.get_array())
        print 'calculating avg shortest path on graph of year', year, feature_type
        for e in g.edges():
            weights[e] = maximum + 1 - weights[e]
        all_asp = gt.topology.shortest_distance(g , weights = weights)
        all_avg_asp = []
        for v in g.vertices():
            all_avg_asp.append(np.average(all_asp[v].get_array()))
        return np.average(all_avg_asp)


    def networkCC(self ,year , feature_type , cast_crew):
        g = self.get_graph_file(year , feature_type , cast_crew)
        print 'calculating Network CC on graph of year', year, feature_type
        return gt.clustering.global_clustering(g)

    def degree(self , year , feature_type , cast_crew):
        g = self.get_graph_file(year, feature_type, cast_crew)
        print 'calculating degree centrality coefficient on graph of year', year, feature_type
        c = []
        for v in g.vertices():
            c.append(v.out_degree())
        return c , g


    def clusteringCoeff(self , year , feature_type , cast_crew):
        g = self.get_graph_file(year, feature_type, cast_crew)
        print 'calculating clustering coefficient on graph of year', year, feature_type
        s = gt.clustering.local_clustering(g)
        return list(s.get_array()) , g


    def pagerank_rating(self, year , feature_type , cast_crew = 'actors'):
        pass
    def eigentrust(self, year, feature_type = 'exact' , cast_crew = 'actors'):
        g = self.get_graph_file(year, feature_type, cast_crew)
        weights = g.ep['weight']
        print 'calculating eigentrust on graph of year', year, feature_type
        maximum = max(weights.get_array())
        for e in g.edges():
            weights[e] = weights[e] / maximum
        return gt.centrality.eigentrust(g, trust_map=weights).get_array(), g
    def pagerank(self, year, feature_type = 'exact' , cast_crew = 'actors'):
        g = self.get_graph_file(year, feature_type, cast_crew)
        weights = g.ep['weight']
        print 'calculating pagerank on graph of year' , year , feature_type

        return gt.centrality.pagerank(g,weight = weights).get_array() , g

    def closeness(self, year , feature_type = 'exact' ,  cast_crew = 'actors'):
        g = self.get_graph_file(year, feature_type ,cast_crew)
        weights = g.ep['weight']
        maximum = max(weights.get_array())
        print 'calculating closeness on graph of year' , year , feature_type
        for e in g.edges():
            weights[e] = maximum + 1 -weights[e]
        return gt.centrality.closeness(g,weight = weights).get_array() , g

    def betweenness(self,year ,feature_type = 'exact' , cast_crew = 'actors'):
        g = self.get_graph_file(year, feature_type, cast_crew)
        weights = g.ep['weight']
        maximum = max(weights.get_array())
        print 'calculating betweenness on graph of year' , year , feature_type
        for e in g.edges():
            weights[e] = maximum + 1 - weights[e]
        return gt.centrality.betweenness(g, weight=weights)[0].get_array(), g

    def get_graph_file(self , year , feature_type = 'exact' ,  cast_crew = 'actors'):
        project_folder = os.path.dirname(__file__).split("src")[0]
        folder = project_folder + 'graphs/'
        if feature_type == 'exact':
            folder += 'year_by_year/'
        else:
            folder += 'cumulative/'
        folder += cast_crew
        fileName = folder + '/' + str(year) + '.p'
        return pickle.load(open(fileName , 'rb'))


#
#
#
# c = Centrality()
# #c.avg_team_centrality(2014 , 'till' , centrality='degree' , cast_crew = 'actors')
# c.small_world_coefficient(1995, feature_type= 'exact' , cast_crew = 'actors')