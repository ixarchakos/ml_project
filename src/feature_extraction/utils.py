import pickle
import os
project_folder = os.path.dirname(__file__).split("src")[0]


class Feature:

    def __init__(self):
        self.movies = pickle.load(open(project_folder + 'dicts/movies.p'))
        self.actors = pickle.load(open(project_folder + 'dicts/actors.p'))
        self.crew = pickle.load(open(project_folder + 'dicts/crew.p'))

    def load_desired_movies(self, year, type="exact"):
        id_list = list()
        if type == "exact":
            for m_id, movie in self.movies.iteritems():
                if movie["year"] == year:
                    id_list.append(m_id)
        else:
            for m_id, movie in self.movies.iteritems():
                if movie["year"] <= year:
                    id_list.append(m_id)
        return id_list
