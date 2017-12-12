import numpy as np 
import pandas as pd

from graph_tool.all import *
import graph_tool as gt 

import pickle
from datetime import datetime

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

g = load_graph('test.graphml')



pos = gt.draw.sfdp_layout(g, eweight = g.edge_properties['weight'])
#gt.draw.graph_draw(g,pos = pos)
w =  g.edge_properties['weight']

#
# for e in g.edges():
# 	print e, w[e]


credits = pd.read_csv('data/credits.csv').as_matrix()
meta = pd.read_csv('data/movies_metadata.csv').as_matrix()

cleanmovies = set()

meta = pd.read_csv('data/movies_metadata.csv').as_matrix()
count = 0
for s in meta:
	try:
		d = datetime.strptime(str(s[14]) , '%Y-%m-%d')
		if d.year == 1994 and s[7] == 'en' and\
			'Documentary' not in s[3] and s[15] > 0 and \
				s[22] > 0:
			cleanmovies.add(s[5])
	except Exception as e:
		pass

print len(cleanmovies)


file = open('actor1994.graphml' , 'w')
file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?> ' +
  '<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" ' +
    'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" ' +
    'xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns' +
     'http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\"> <graph id=\"G\" edgedefault=\"undirected\">\n')




actors = {}
idconvert = {}



cleancredits = []
for movie in credits:
	if str(movie[2]) in cleanmovies:
		#print movie[2]
		cleancredits.append(movie[0])

moviecast = np.array(cleancredits)
#print cast[0]





i = 0
for cast in moviecast:
	cast = eval(cast)
	for actor in cast:
		#print actor['id']
		if actor['id'] not in actors:
			actors[actor['id']] = actor['name']
			file.write('<node id = \"' + str(actor['id']) +  ' \" /> \n')
			idconvert[i] = actor['id']
			i += 1

for cast in moviecast:
	cast = eval(cast)
	for i in range(len(cast)):
		for j in range(i+1 , len(cast)):
			actor1 = cast[i]
			actor2 = cast[j]
			file.write('<edge source =\"' + str(actor1['id']) +  ' \" target = \"' + str(actor2['id']) +  ' \" /> \n')


file.write('</graph>\n</graphml>')
file.close()

g = Graph(directed = False)
g = load_graph("actor1994.graphml")
pos = gt.draw.sfdp_layout(g)
gt.draw.graph_draw(g,pos = pos)
