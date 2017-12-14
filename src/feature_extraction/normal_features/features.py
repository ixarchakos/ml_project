from src.feature_extraction.utils import Feature
import numpy as np

class Normal_Features:

    def __init__(self):
        self.f = Feature()

    def avg_team_aggregate_value(self, year=1990, feature_type="exact", value="revenue"):

        movies_ids = self.f.load_desired_movies(year, feature_type)
        movies_team_value_actors = dict()
        movies_team_value_crew = dict()
        a_income = self.actors_aggregate_value(year, feature_type=feature_type, cast_crew="actors", value=value)
        c_income = self.actors_aggregate_value(year, feature_type=feature_type, cast_crew="crew", value=value)
        for m_id in movies_ids:
            sum_a_values = 0.0
            sum_c_values = 0.0
            count_a = 0
            count_c = 0
            for actor_id in self.f.movies[m_id]["actors"]:
                sum_a_values += a_income[actor_id]
                count_a += 1
            for crew_id in self.f.movies[m_id]["crew"].keys():
                sum_c_values += c_income[crew_id]
                count_c +=1
            if count_c > 0:
                movies_team_value_crew[m_id] = sum_c_values / count_c
            if count_a > 0:
                movies_team_value_actors[m_id] = sum_a_values/count_a
        return movies_team_value_actors , movies_team_value_actors

    def actors_aggregate_value(self, year, feature_type="exact", cast_crew="actors", value="revenue"):
        actors_income = dict()
        movies_ids = self.f.load_desired_movies(year, feature_type)
        actors_movie_count = dict()
        for m_id in movies_ids:
            if cast_crew == "crew":
                for crew in self.f.movies[m_id][cast_crew].keys():
                    if crew in actors_income:
                        actors_income[crew] += self.f.movies[m_id][value]
                        actors_movie_count[crew] += 1
                    else:
                        actors_income[crew] = self.f.movies[m_id][value]
                        actors_movie_count[crew] = 1

            else:
                for actor_id in self.f.movies[m_id][cast_crew]:
                    if actor_id in actors_income:
                        actors_income[actor_id] += self.f.movies[m_id][value]
                        actors_movie_count[actor_id] += 1
                    else:
                        actors_income[actor_id] = self.f.movies[m_id][value]
                        actors_movie_count[actor_id] = 1


        for id in actors_income:
            actors_income[id] /= actors_movie_count[id]
        return actors_income


k = Normal_Features()
print k.avg_team_aggregate_value(2015, feature_type="till", value="rating")