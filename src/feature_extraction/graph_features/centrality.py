from graph_tool.all import *
import graph_tool as gt
from src.feature_extraction.utils import Feature, project_folder
import pickle
import os


class Centrality():

    def __init__(self):
        self.f = Feature()


    def avg_team_centrality(self, year , feature_type = 'exact' ,  cast_crew = 'actors' , centrality = 'closeness'):
        movies_ids = self.f.load_desired_movies(year, feature_type )
        movies = self.f.movies
        if centrality == 'closeness':
            actors_centrality, g = self.closeness(year,feature_type = 'exact' ,  cast_crew = 'actors' )
        actors_ids = self.convert_ids(g)
        centerality_actors = dict()
        for i ,c in enumerate(actors_centrality):
            centerality_actors[actors_ids[i]] = c
        movies_centerality = dict()
        for mid , movie in movies.iteritems():
            if mid in movies_ids:
                sum_centrality = 0.0
                count = 0.0
                for aid in movies[mid]['actors']:
                    sum_centrality += centerality_actors[aid]
                movies_centerality[mid] = sum_centrality / count
                print movies_centerality[mid]

        # implement crew
        # implement other centrality measures



    #*****************************************************************************
    def convert_ids(self , g):
        aids = []
        gids = g.vp['id']
        for v in g.vertices():
            aids.append(gids[v])
        return aids

    def closeness(self, year , feature_type = 'exact' ,  cast_crew = 'actors'):
        g = self.get_graph_file(year, feature_type ,cast_crew)
        weights = g.ep['weight']
        maximum = max(weights.get_array())

        for e in g.edges():
            weights[e] = maximum + 1 -weights[e]
        return gt.centrality.closeness(g,weight = weights).get_array() , g

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



c = Centrality()
c.avg_team_centrality(1995)