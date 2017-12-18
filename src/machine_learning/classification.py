import numpy as np
import collections
import os
import pickle
project_folder = os.path.dirname(__file__).split("src")[0]
class Classification:
	def __init__(self):
		X = pickle.load(open(project_folder+ 'dicts/third.p' , 'rb')).T
		y = pickle.load(open(project_folder+ 'dicts/roundedratings.p' , 'rb')).T
		self.d = len(X[1])
		self.n = len(X[0])
		print self.d , self.n , len(y)

c = Classification()