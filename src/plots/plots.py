import numpy as np
import collections
import os
import pickle
import matplotlib.pyplot as plt


project_folder = os.path.dirname(__file__).split("src")[0]


class Plot:
	def __init__(self):
		self.X = pickle.load(open(project_folder + 'dicts/third_fixed.p', 'rb')).T
		self.yc = pickle.load(open(project_folder + 'dicts/roundedratings.p', 'rb'))
		self.yr = pickle.load(open(project_folder + 'dicts/ratings.p', 'rb'))

	def plot_features_c(self):
		for i in range(0,self.X.shape[1]):
			plt.plot(self.X[:,i], self.yc , 'g.')
			plt.savefig(project_folder + 'plots/feature_rounded_ratings/feature_' + str(i) + '.png')

	def plot_features_r(self):
		for i in range(0,self.X.shape[1]):
			plt.plot(self.X[:,i], self.yr , 'g.')
			plt.savefig(project_folder + 'plots/feature_ratings/feature_' + str(i) + '.png')



p = Plot()
p.plot_features_r()
p.plot_features_c()
