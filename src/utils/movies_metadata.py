import pandas as pd
from datetime import datetime


def load_cast_crew():
    movies = pd.read_csv(r"../../data/credits.csv").as_matrix()
    movies_data = load_movies()
    for row in movies:
        id = str(row[2])
        if id in movies_data:
            movies_actors, movies_crew = list(), list()
            for actor in eval(row[0]):
                movies_actors.append(str(actor["id"]))
            for crew in eval(row[1]):
                if 'Producer' == crew['job'] or 'Director' == crew['job'] or 'Writing' == crew['department']:
                    if 'Writing' == crew['department']:
                        movies_crew.append({str(crew["id"]): "Writer"})
                    else:
                        movies_crew.append({str(crew["id"]): crew["job"]})
            movies_data[id]["actors"] = movies_actors
            movies_data[id]["crew"] = movies_crew
            print movies_data[id]
            exit()
    return movies_data


def load_movies():
    movies = pd.read_csv(r"../../data/movies_metadata.csv").as_matrix()

    movies_data = dict()
    for s in movies:
        try:
            d = datetime.strptime(str(s[14]), '%Y-%m-%d')
            if 1990 <= d.year <= 2016 and 'Documentary' not in str(s[3]) and 'en' in str(s[17]) and float(s[15]) > 0 and float(s[22]) > 0:
                mov = dict()
                mov["name"] = s[7]
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
    for movie in movies:
        if movie[2] in movies_data:
            movies_actors = list()
            for actor in eval(movie[0]):
                movies_actors[actor["id"]] = {"name": actor["name"], "movies": set()}

    for movie in movies:
        if movie[2] in movies_data:
            movies_actors = list()
            for actor in eval(movie[0]):
                movies_actors[actor["id"]]['movies'].add(movie[2])
                print movies_actors[actor["id"]]
                exit()

load_people()