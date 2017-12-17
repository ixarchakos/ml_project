from src.feature_extraction.utils import Feature


class Normal_Features:

    def __init__(self):
        self.f = Feature()

    def avg_team_aggregate_value(self, year=1990, feature_type="exact", value="revenue"):

        movies_team_value_actors = dict()
        movies_team_value_crew = dict()
        current_movie_ids = self.f.load_desired_movies(year, "exact")
        a_income = self.actors_aggregate_value(year-1, feature_type=feature_type, cast_crew="actors", value=value)
        c_income = self.actors_aggregate_value(year-1, feature_type=feature_type, cast_crew="crew", value=value)
        for m_id in current_movie_ids:
            sum_a_values = 0.0
            sum_c_values = 0.0
            count_a = 0
            count_c = 0
            for actor_id in self.f.movies[m_id]["actors"]:
                if actor_id in a_income:
                    sum_a_values += a_income[actor_id]
                count_a += 1
            for crew_id in self.f.movies[m_id]["crew"].keys():
                if crew_id in c_income:
                    sum_c_values += c_income[crew_id]
                count_c += 1
            if count_c > 0:
                movies_team_value_crew[m_id] = sum_c_values / count_c
            if count_a > 0:
                movies_team_value_actors[m_id] = sum_a_values/count_a
        return movies_team_value_actors, movies_team_value_actors

    def avg_previous_team_individual_experience(self, year=1990, feature_type="exact"):
        movies_ids = self.f.load_desired_movies(year, feature_type)
        actors_experience = dict()
        crew_experience = dict()
        a_experience = self.actors_individual_experience(year-1, feature_type, cast_crew="actors")
        c_experience = self.actors_individual_experience(year-1, feature_type, cast_crew="crew")
        for m_id in movies_ids:
            sum_a_values = 0.0
            sum_c_values = 0.0
            count_a = 0
            count_c = 0
            for actor_id in self.f.movies[m_id]["actors"]:
                if actor_id in a_experience:
                    sum_a_values += a_experience[actor_id]
                count_a += 1
            for crew_id in self.f.movies[m_id]["crew"].keys():
                if crew_id in c_experience:
                    sum_c_values += c_experience[crew_id]
                count_c += 1
            if count_c > 0:
                crew_experience[m_id] = sum_c_values / count_c
            if count_a > 0:
                actors_experience[m_id] = sum_a_values / count_a
        return actors_experience, crew_experience

    def team_size(self, year, feature_type="exact"):
        movies_ids = self.f.load_desired_movies(year, feature_type)
        actor_number, crew_number = dict(), dict()
        for m_id in movies_ids:
            actor_number[m_id] = len(self.f.movies[m_id]["actors"])
            crew_number[m_id] = len(self.f.movies[m_id]["crew"])
        return actor_number, crew_number

    def team_tenure(self, year, feature_type="exact"):
        movies_ids = self.f.load_desired_movies(year, "till")
        actors_tenure, crew_tenure = self.people_tenure(year-1)
        movies_tenure_actor, movies_tenure_crew = dict(), dict()
        for m_id in movies_ids:
            sum_a = 0.0
            count_a = 0.0
            sum_c = 0.0
            count_c = 0.0
            for actors_id in self.f.movies[m_id]["actors"]:
                sum_a += actors_tenure[int(actors_id)]
                count_a += 1
            if count_a > 0:
                movies_tenure_actor[m_id] = sum_a/count_a

            for crew_id in self.f.movies[m_id]["crew"]:
                sum_c += crew_tenure[int(crew_id)]
                count_c += 1
            if count_c > 0:
                movies_tenure_crew[m_id] = sum_c / count_c
        return movies_tenure_actor, movies_tenure_crew

    def average_team_combined_stats(self, year, value="experience"):
        movies_ids = self.f.load_desired_movies(year, "exact")
        movies = self.f.movies
        pair_values = self.pairs_features(year-1, value)
        movies_team_average_stats = dict()
        for key, movie in movies.iteritems():
            if key in movies_ids:
                actors_crew = movies[key]["actors"] + movies[key]["crew"].keys()
                possible_pairs = self.all_to_all(list(set(actors_crew)))
                total = 0.0
                count = 0.0
                for pair in possible_pairs:
                    if pair in pair_values:
                        print pair_values[pair][0]
                        total += pair_values[pair][0]
                    count += 1
                if count > 0:
                    movies_team_average_stats[key] = float(total) / float(count)
                else:
                    movies_team_average_stats[key] = 0
        print movies_team_average_stats
    #*************************************************************************************
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

    def actors_individual_experience(self,  year, feature_type="exact", cast_crew="actors"):
        movies_ids = self.f.load_desired_movies(year, feature_type)
        actors_movie_count = dict()
        for m_id in movies_ids:

            if cast_crew == "crew":
                for crew in self.f.movies[m_id][cast_crew].keys():
                    if crew in actors_movie_count:
                        actors_movie_count[crew] += 1
                    else:
                        actors_movie_count[crew] = 1
            else:
                for actor_id in self.f.movies[m_id][cast_crew]:
                    if actor_id in actors_movie_count:
                        actors_movie_count[actor_id] += 1
                    else:
                        actors_movie_count[actor_id] = 1

        return actors_movie_count

    def people_tenure(self, year):
        movies_ids = self.f.load_desired_movies(year, 'till')
        movies = self.f.movies
        actors_ids = self.f.actors
        crew = self.f.crew
        actor_tenure = dict()
        for key, actor in actors_ids.iteritems():
            max = -2000
            min = 4000
            for movie in actor["movies"]:
                if movie in movies_ids:
                    myear = movies[movie]['year']
                    if min > myear:
                        min = myear
                    if max < myear:
                        max = myear
            if max - min >= 0:
                actor_tenure[key] = max - min


        crew_tenure = dict()
        for key, c in crew.iteritems():
            max = -2000
            min = 4000
            for movie in c["movies"]:

                if movie in movies_ids:
                    myear = movies[movie]['year']
                    if min > myear:
                        min = myear
                    if max < myear:
                        max = myear
            if max - min >= 0:
                crew_tenure[key] = max - min

        return actor_tenure, crew_tenure

    def pairs_features(self, year, value="revenue"):
        movies_ids = self.f.load_desired_movies(year, "till")
        movies = self.f.movies
        from collections import defaultdict

        pair_experience = defaultdict(list)
        for key, movie in movies.iteritems():
            if key in movies_ids:
                actors_crew = movie["actors"] + movie["crew"].keys()
                dyads = self.all_to_all(list(set(actors_crew)))
                dyads_to_dict = dict()
                if value == "experience":
                    for v in dyads:
                        dyads_to_dict[v] = 1
                elif value == "revenue":
                    for v in dyads:
                        dyads_to_dict[v] = movie["revenue"]
                elif value == "rating":
                    for v in dyads:
                        dyads_to_dict[v] = movie["rating"]
                for k, v in dyads_to_dict.iteritems():
                    pair_experience[k].append(v)
        for k, v in pair_experience.iteritems():
            if type(v) is list:
                if len(v) > 1:
                    pair_experience[k] = [sum(v)]

        return pair_experience

    def all_to_all(self, l):
        result = [(l[p1], l[p2]) for p1 in range(len(l)) for p2 in range(p1 + 1, len(l))]
        result = [self.sort_by_hand(i) for i in list(set(result)) if i[0] != i[1]]
        return result

    def sort_by_hand(self, value):
        if value[0] > value[1]:
            return value[1], value[0]
        else:
            return value[0], value[1]

# k = Normal_Features()
# print k.average_team_combined_stats(2010, value="rating")
