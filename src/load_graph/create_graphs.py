import pickle
import ast
from datetime import datetime
import pandas as pd
from graph_tool.all import *
import graph_tool as gt


def load_cast():
    actors = pd.read_csv(r"../../data/credits.csv").as_matrix()
    actors_dict = dict()
    for actor_id in actors:
        actors_dict[actor_id[2]] = {"cast": actor_id[0], "crew": actor_id[1]}
    return actors_dict


def all_to_all(l):
    result = [(l[p1], l[p2]) for p1 in range(len(l)) for p2 in range(p1 + 1, len(l))]
    result = [sort_by_hand(i) for i in list(set(result)) if i[0] != i[1]]
    return result


def sort_by_hand(value):
    if value[0] > value[1]:
        return value[1], value[0]
    else:
        return value[0], value[1]


def create_graphml_file(data, year, previous):
    if previous == 0:
        #folder = "../../graphs/year_by_year/crew/"
        folder = "../../graphs/year_by_year/actors/"
    else:
        #folder = "../../graphs/cumulative/crew/"
        folder = "../../graphs/cumulative/actors/"
    fileName = folder + str(year) + '.graphml'
    file = open(fileName , 'w')
    file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
               '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
               'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
               'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
               'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')

    file.write('<key id=\"d0\" for=\"node\" attr.name=\"id\" attr.type=\"int\" />' +
               '<key id=\"d1\" for=\"edge\" attr.name=\"weight\" attr.type=\"int\"> ' +
               '<default>1</default></key>\n')

    node_set = set()
    for edge in data.keys():
        node_set.add(edge[0])
        node_set.add(edge[1])

    for node in node_set:
        file.write('<node id = \"' + str(node) + '\" > \n')
        file.write('<data key=\"d0\">' + str(node) + '</data> \n')
        file.write('</node> \n')

    for edge, weight in data.iteritems():
        file.write('<edge source =\"' + str(edge[0]) + \
                   '\" target = \"' + str(edge[1]) + '\" >\n')
        file.write('<data key=\"d1\">' + str(weight) + '</data> \n')
        file.write('</edge>\n')

    file.write('</graph> </graphml>')
    file.close()
    return fileName


def create_movie_graph(year , previous):
    actors_dict = load_cast()
    movies = pd.read_csv(r"../../data/movies_metadata.csv").as_matrix()
    movies_id = list()
    network_pairs = list()
    staff_info = dict()
    for s in movies:
        try:
            d = datetime.strptime(str(s[14]) , '%Y-%m-%d')
            if previous == 0:
                if d.year == year and 'Documentary' not in str(s[3]) and 'en' in str(s[17]) and float(s[15]) > 0 and float(s[22]) > 0:
                    movies_id.append(ast.literal_eval(s[5]))
            if previous == 1:
                if year >= d.year >= 1990 and 'Documentary' not in str(s[3]) and 'en' in str(s[17]) and float(s[15]) > 0 and float(s[22]) > 0:
                    movies_id.append(ast.literal_eval(s[5]))
        except Exception as e:
            pass
    print(len(movies_id))

    for m_id in movies_id:
        temp_list = list()
        # for actor in ast.literal_eval(actors_dict[m_id]["crew"]):
        #     if 'Producer' == actor['job'] or 'Director' == actor['job'] or 'Writing' == actor['department']:
        #         temp_list.append(actor["id"])
        #         staff_info[actor["id"]] = actor["name"]

        for actor in eval(actors_dict[m_id]['cast']):
            temp_list.append(actor['id'])
            staff_info[actor["id"]] = actor["name"]
        pairs = all_to_all(temp_list)
        for v in pairs:
            network_pairs.append(v)

    # pairs with weights
    weighted_pairs = dict()
    for pair in network_pairs:

        if pair in weighted_pairs:
            weighted_pairs[pair] += 1
        else:
            weighted_pairs[pair] = 1

    return create_graphml_file(weighted_pairs, year, previous)


def create_one_year_dataset():
    for year in range(1995, 2016):
        fileName = create_movie_graph(year, 1)
        g = load_graph(fileName)
        pickle.dump(g, open(fileName.replace(".graphml", "") + '.p', 'wb'))


create_one_year_dataset()

# g = pickle.load(open('../../graphs/year_by_year/1996.p', 'rb'))
