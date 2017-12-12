import numpy as np 
import pandas as pd

from graph_tool.all import *
import graph_tool as gt 

import pickle
from datetime import datetime
import collections

import matplotlib.pyplot as plt


#
# cleanmovies = pickle.load(open('cleanmovies.p' , 'rb'))
#
# credits = pd.read_csv('data/credits.csv')
# #print credits.describe()
#
# file = open('actor.graphml' , 'w')
# file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
#   '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
#     'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
#     'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
#      'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')
#
#
# credits = credits.as_matrix()
# #print type(credits)
#
# actors = {}
# idconvert = {}
#
# print cleanmovies
#
# cleancredits = []
# for movie in credits:
# 	if str(movie[2]) in cleanmovies:
# 		#print movie[2]
# 		cleancredits.append(movie[0])
#
# moviecast = np.array(cleancredits)
# #print cast[0]
#
#
#
#
#
# i = 0
# for cast in moviecast:
# 	cast = eval(cast)
# 	for actor in cast:
# 		#print actor['id']
# 		if actor['id'] not in actors:
# 			actors[actor['id']] = actor['name']
# 			file.write('<node id = \"' + str(actor['id']) +  ' \" /> \n')
# 			idconvert[i] = actor['id']
# 			i += 1
#
# for cast in moviecast:
# 	cast = eval(cast)
# 	for i in range(len(cast)):
# 		for j in range(i+1 , len(cast)):
# 			actor1 = cast[i]
# 			actor2 = cast[j]
# 			file.write('<edge source =\"' + str(actor1['id']) +  ' \" target = \"' + str(actor2['id']) +  ' \" /> \n')
#
#
# file.write('</graph>\n</graphml>')
# file.close()
#
# g = Graph(directed = False)
# g = load_graph("actor.graphml")
#
#
# # pos = gt.draw.sfdp_layout(g)
# # gt.draw.graph_draw(g,pos = pos)
# # print 'finish loading'
# #
# #
# #
# pickle.dump(g, open('graph.p' , 'wb'))
# pickle.dump( actors , open('actors.p' , 'wb'))
# pickle.dump(idconvert , open('idconvert.p' , 'wb'))

#
# g = pickle.load(open('graph.p' , 'rb'))
# actors = pickle.load(open('actors.p', 'rb'))
# idconvert = pickle.load(open('idconvert.p' , 'rb'))
# cleanmovies = pickle.load(open('cleanmovies.p' , 'rb'))
# # s = sorted(pr.get_array(), reverse = True)[:20]
#
# #
# # print pr[0]
# # print actors[idconvert[0]]
# #
# pgrnk = gt.centrality.pagerank(g).get_array()
# pr = np.argsort(pgrnk)
# for rank in pr[len(pr) - 400 :]:
# 	print actors[idconvert[rank]]
#
# actorpgrank ={}
# for i in range(len(pgrnk)):
# 	actorpgrank[idconvert[i]] = pgrnk[i]
#

#pr = np.argsort(gt.centrality.closeness(g).get_array())
#for rank in pr[len(pr) - 20 :]:
	#print actors[idconvert[rank]]

#
# print '******************************************'
#
# for v in g.vertices():
# 	s = actors[idconvert[v]]
# 	if 'Tom' in s:
# 		print s

#
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
# count = 0
# for s in meta:
# 	try:
# 		d = datetime.strptime(str(s[14]) , '%Y-%m-%d')
# 		if d.year > 2016:
# 			count += 1
# 	except Exception as e:
# 		pass
#
# print count
#
# count = 0
# for s in meta:
# 	try:
# 		if s[7] == 'en' and datetime.strptime(str(s[14]) , '%Y-%m-%d').year > 2010 :
# 			count += 1
# 	except Exception as e:
# 		pass
#
# print count
#
#



# data cleaning
# credits = pd.read_csv('data/credits.csv').as_matrix()
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
#
# cleanmovies = set()
#
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
# count = 0
# for s in meta:
# 	try:
# 		d = datetime.strptime(str(s[14]) , '%Y-%m-%d')
# 		if d.year >= 1990 and s[7] == 'en' and\
# 			'Documentary' not in s[3] and s[15] > 0 and \
# 				s[22] > 0:
# 			cleanmovies.add(s[5])
# 			count += 1
# 	except Exception as e:
# 		pass
#
#
# pickle.dump(cleanmovies, open('cleanmovies.p' , 'wb'))
#
# yd = {}
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
# for s in meta:
# 	try:
# 		if s[5] in cleanmovies:
# 			yd[str(s[5])] = s[15]
# 			if s[5] == '19995':
# 				print s[8]
# 	except Exception as e:
# 		pass
#
# xd = {}
# credits = pd.read_csv('data/credits.csv').as_matrix()
# for movie in credits:
# 	try:
# 		if str(movie[2]) in cleanmovies:
# 			cast = eval(movie[0])
# 			count = 0.0
# 			for actor in cast:
# 				count += actorpgrank[actor['id']]
# 			count /=  len(cast)
# 			xd[str(movie[2])] = count
# 	except Exception as e:
# 		pass
#
#
# X = []
# y = []
# testX = []
# testy = []
# max = 0
# s = 0
# for i in xd:
# 	if yd[i] > 875457937:
# 		X.append(xd[i])
# 		y.append(yd[i])
# 		if yd[i] > max:
# 			max = yd[i]
# 			s = i
# X = X / np.max(X)
# plt.plot(X,y , 'ro')
# plt.show()
# print np.sort(y)[len(y)- 50]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# pos = gt.draw.sfdp_layout(g, eweight = g.edge_properties['weight'])
# #gt.draw.graph_draw(g,pos = pos)
# w =  g.edge_properties['weight']
#
# #
# # for e in g.edges():
# # 	print e, w[e]
#
#
# credits = pd.read_csv('data/credits.csv').as_matrix()
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
#
# cleanmovies = set()
#
# meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
# count = 0
# for s in meta:
# 	try:
# 		d = datetime.strptime(str(s[14]) , '%Y-%m-%d')
# 		if d.year == 1994 and s[7] == 'en' and\
# 			'Documentary' not in s[3] and s[15] > 0 and \
# 				s[22] > 0:
# 			cleanmovies.add(s[5])
# 	except Exception as e:
# 		pass
#
# print len(cleanmovies)
#
#
# file = open('actor1994.graphml' , 'w')
# file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
#   '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
#     'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
#     'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
#      'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')
#
#
#
#
# actors = {}
# idconvert = {}
#
#
#
# cleancredits = []
# for movie in credits:
# 	if str(movie[2]) in cleanmovies:
# 		#print movie[2]
# 		cleancredits.append(movie[0])
#
# moviecast = np.array(cleancredits)
# #print cast[0]
#
#
#
#
#
# i = 0
# for cast in moviecast:
# 	cast = eval(cast)
# 	for actor in cast:
# 		#print actor['id']
# 		if actor['id'] not in actors:
# 			actors[actor['id']] = actor['name']
# 			file.write('<node id = \"' + str(actor['id']) +  ' \" /> \n')
# 			idconvert[i] = actor['id']
# 			i += 1
#
# for cast in moviecast:
# 	cast = eval(cast)
# 	for i in range(len(cast)):
# 		for j in range(i+1 , len(cast)):
# 			actor1 = cast[i]
# 			actor2 = cast[j]
# 			file.write('<edge source =\"' + str(actor1['id']) +  ' \" target = \"' + str(actor2['id']) +  ' \" /> \n')
#
#
# file.write('</graph>\n</graphml>')
# file.close()

# g = Graph(directed = False)
# g = load_graph("actor1994.graphml")
# pos = gt.draw.sfdp_layout(g)
#gt.draw.graph_draw(g,pos = pos)


#
# print actors[idconvert[g.vertex(845)]]
# g.list_properties()

#
# for i, v in enumerate(g.vertices()):
# 	print [item for item, count in collections.Counter(v.out_edges()).items() if count > 1]

#
# for i in  g.vertex(845).out_edges():
# 	print i


#
# file = open('actor1994complete.graphml' , 'w')
# file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
#   '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
#     'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
#     'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
#      'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')
#
# file.write('<key id=\"d0\" for=\"node\" attr.name=\"id\" attr.type=\"int\" />' +
#   	'<key id=\"d1\" for=\"edge\" attr.name=\"weight\" attr.type=\"int\"> ' +
# 	'<default>1</default></key>')
#
#
# i = 0
# for cast in moviecast:
# 	cast = eval(cast)
# 	for actor in cast:
# 		if actor['id'] not in actors:
# 			actors[actor['id']] = actor['name']
# 			file.write('<node id = \"' + str(actor['id']) +  ' \" > \n')
# 			file.write('<data key=\"d0\">'+ str(actor['id']) +  '</data> \n')
# 			file.write('</node> \n')
#
# for v in g.vertices():
# 	id = str(idconvert[g.vertex(v)])
# 	file.write('<node id = \"' + id + ' \" > \n')
# 	file.write('<data key=\"d0\">' + id + '</data> \n')
# 	file.write('</node> \n')
#
# for i, v in enumerate(g.vertices()):
# 	s = [item for item, count in collections.Counter(v.out_edges()).items() if count > 1]
# 	for v1 in v.out_neighbours():
# 		a1 = str(idconvert[g.vertex(v)])
# 		a2 = str(idconvert[g.vertex(v1)])
# 		file.write('<edge source =\"' + a1 + ' \" target = \"' + a2 + ' \" > \n')
# 		if s != []:
# 			number = str(len(s) + 1)
# 			file.write('<data key=\"d1\">'+ number +  '</data> \n')
# 		file.write('</edge>')
#
#
# file.write('</graph>\n</graphml>')
# file.close()



# g2 = Graph(directed = False)
# g2 = load_graph("actor1994complete.graphml")
# weights = g2.edge_properties['weight']
# ids = g2.vp['id']
#
# for e in g2.edges():
# 	if weights[e] > 1:
# 		print weights[e] , e

#***********************************************************
#***********************************************************
#***********************************************************

print '*****************************************************'

# Finding relevant and clean movies for graph creation for a
# particular year


cleanMoviesIDs = set()
movies_metadata = pd.read_csv('data/movies_metadata.csv').\
				as_matrix()
year = 2016
count = 0
for movie in movies_metadata:
	try:
		d = datetime.strptime(str(movie[14]) , '%Y-%m-%d')
		if d.year == year and movie[7] == 'en' and \
				'Documentary' not in movie[3] and \
				movie[15] > 0 and movie[22] > 0:
			cleanMoviesIDs.add(movie[5])
	except Exception as e:
		pass

print 'There are ' + str(len(cleanMoviesIDs)) + \
	' clean movies made in ' + str(year)
print '*****************************************************'


# creating cleanCast and cleanCrew

credits = pd.read_csv('data/credits.csv').as_matrix()
cleanCast = [] # contains cast for the clean movies of year = year
cleanCrew = [] # contains crew for the clean movies of year = year
movieIDs = [] # contains ID for the clean movies of year = year in order

for movie in credits:
	if str(movie[2]) in cleanMoviesIDs:
		cleanCast.append(eval(movie[0]))
		cleanCrew.append(eval(movie[1]))
		movieIDs.append(movie[2])




print 'Clean Cast and Crew retrieved for year: ' + str(year)
print '*****************************************************'

# creating graphml file
file = open('actors'+ str(year)+ '.graphml' , 'w')
file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
  '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
    'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
    'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
     'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')

file.write('<key id=\"d0\" for=\"node\" attr.name=\"id\" attr.type=\"int\" />' +
  	'<key id=\"d1\" for=\"edge\" attr.name=\"weight\" attr.type=\"int\"> ' +
	'<default>1</default></key>\n')
# file.write('<key id=\"d2\" for=\"node\" attr.name=\"isActor\" attr.type=\"int\" />')
# file.write('<key id=\"d3\" for=\"node\" attr.name=\"isCrew\" attr.type=\"int\" />')

actorsName = {} # a dictionary mapping actor IDs to names
crewName = {} # a dictionary mapping crew IDs to names

for i in range(len(cleanCast)):
	cast = cleanCast[i]
	crew = cleanCrew[i]
	id = movieIDs[i]
	for actor in cast:
		if actor['id'] not in actorsName:
			actorsName[actor['id']] = actor['name']
			file.write('<node id = \"' + str(actor['id']) + '\" > \n')
			file.write('<data key=\"d0\">'+ str(actor['id']) + '</data> \n')
			#file.write('<data key= "d2">1</data>' )
			file.write('</node> \n')
	# for member in crew:
	# 	if member['job'] == 'Director' or \
	# 		member['job'] == 'Writer' or \
	# 		member['job'] == 'Producer':
	# 		if member['id'] not in crewName:
	# 			crewName[member['id']] = member['name']
	# 			file.write('<node id = \"' + str(member['id']) + '\" > \n')
	# 			file.write('<data key=\"d0\">' + str(member['id']) + '</data> \n')
	# 			file.write('<data key= "d3">1</data>')
	# 			file.write('</node> \n')


for cast in cleanCast:
	edgeSet = set()
	for i in range(len(cast)):
		a1 = cast[i]
		for j in range(i+1 , len(cast)):
			a2 = cast[j]
			if a1['id'] != a2['id']:
				edgeSet.add( (str(a1['id']) , str (a2['id'])))
	for edge in edgeSet:
		alt = (edge[1], edge[0])
		if alt not in edgeSet:
			file.write('<edge source =\"' + edge[0] + \
					   '\" target = \"' + edge[1] + '\" />\n')



file.write('</graph> </graphml>')
file.close()



g = load_graph('actors'+ str(year)+ '.graphml')
print g.list_properties()
ids = g.vp['id']
weights = g.ep['weight']
for v in g.vertices():
	s = v.out_neighbours()
	c =  collections.Counter(s)
	for v2 in c:
		if c[v2] > 1:
			print v , v2 , actorsName[ids[v]], actorsName[ids[v2]], c[v2]
			weights[g.edge(v,v2)] = c[v2]
count = 0
for e in g.edges():
	if weights[e] > 1:
		count += 1
print count , 'edges were multiple edges'

g.save('actors' + str(year) + 'complete.graphml' , 'graphml')

print 'complete graph is saved!'