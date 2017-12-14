import pandas as pd
from datetime import datetime
import pickle


def load_cast_crew():
    movies = pd.read_csv(r"../../data/credits.csv").as_matrix()
    movies_data = load_movies()
    for row in movies:
        id = str(row[2])
        if id in movies_data:
            movies_actors, movies_crew = list(), dict()
            for actor in eval(row[0]):
                movies_actors.append(str(actor["id"]))
            for crew in eval(row[1]):
                if 'Producer' == crew['job'] or 'Director' == crew['job'] or 'Writing' == crew['department']:
                    movies_crew[str(crew["id"])] = list()
            for crew in eval(row[1]):
                if 'Producer' == crew['job'] or 'Director' == crew['job'] or 'Writing' == crew['department']:
                    if 'Writing' == crew['department']:
                        movies_crew[str(crew["id"])].append("Writer")
                    else:
                        movies_crew[str(crew["id"])].append(crew["job"])
            movies_data[id]["actors"] = movies_actors
            movies_data[id]["crew"] = movies_crew

    return movies_data


def load_movies():
    movies = pd.read_csv(r"../../data/movies_metadata.csv").as_matrix()

    movies_data = dict()
    for s in movies:
        try:
            d = datetime.strptime(str(s[14]), '%Y-%m-%d')
            if 1990 <= d.year <= 2016 and 'Documentary' not in str(s[3]) and 'en' in str(s[17]) and float(s[15]) > 0 and float(s[22]) > 0:
                mov = dict()
                mov["name"] = s[8]
                mov["year"] = d.year
                mov["revenue"] = float(s[15])
                mov["rating"] = float(s[22])
                mov["genre"] = [k['name'] for k in eval(s[3])]
                movies_data[s[5]] = mov

        except Exception:
            pass
    return movies_data


def load_people():
    movies_data = load_movies()
    movies = pd.read_csv(r"../../data/credits.csv").as_matrix()
    actors = dict()
    crew = dict()
    for movie in movies:
        if str(movie[2]) in movies_data:
            for actor in eval(movie[0]):
                actors[actor["id"]] = {"name": actor["name"], "movies": set()}
    for movie in movies:
        if str(movie[2]) in movies_data:
            for actor in eval(movie[0]):
                actors[actor["id"]]["movies"].add(str(movie[2]))

    for movie in movies:
        if str(movie[2]) in movies_data:
            for c in eval(movie[1]):
                if 'Producer' == c['job'] or 'Director' == c['job'] or 'Writing' == c['department']:
                    crew[c["id"]] = {"name": c["name"], "movies": dict()}



    for movie in movies:
        if str(movie[2]) in movies_data:
            for c in eval(movie[1]):
                if 'Producer' == c['job'] or 'Director' == c['job'] or 'Writing' == c['department']:
                    crew[c["id"]]["movies"][str(movie[2])] = []

    for movie in movies:
        if str(movie[2]) in movies_data:
            for c in eval(movie[1]):
                if 'Producer' == c['job'] or 'Director' == c['job'] or 'Writing' == c['department']:
                    if c['department'] == 'Writing':
                        crew[c["id"]]["movies"][str(movie[2])].append('Writer')
                    else:
                        crew[c["id"]]["movies"][str(movie[2])].append(c['job'])

    return actors, crew


actors, crew = load_people()
movies = load_cast_crew()

folder = "../../dicts/"
print movies


pickle.dump(actors, open(folder + "actors.p", 'wb'))
pickle.dump(crew, open(folder + "crew.p", 'wb'))
pickle.dump(movies, open(folder + "movies.p", 'wb'))
