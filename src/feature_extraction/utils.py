import pickle


class Feature:

    def __init__(self):
        self.movies = pickle.load(open('../../../dicts/movies.p'))
        self.actors = pickle.load(open('../../../dicts/actors.p'))
        self.crew = pickle.load(open('../../../dicts/crew.p'))
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
