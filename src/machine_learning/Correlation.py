import numpy as np
import collections
import os
import pickle
import matplotlib.pyplot as plt

project_folder = os.path.dirname(__file__).split("src")[0]


class Correlation:
	def __init__(self):
		self.feature_names = pickle.load(open(project_folder+ 'dicts/feature_names.p' , 'rb'))
		self.X = pickle.load(open(project_folder+ 'dicts/last_fixed.p' , 'rb')).T
		self.y = pickle.load(open(project_folder+ 'dicts/roundedratings.p' , 'rb'))
		self.n = self.X.shape[0]
		self.d = self.X.shape[1]
		print 'Feature matrix X with shape:' , self.X.shape , 'is loaded'
		print 'Target Vector y with shape:' , self.y.shape, 'is loaded'
		print '********************************************************'

	def pearson(self):
		fm = np.zeros(61 * 61).reshape(61,61)
		for feature in range(self.X.shape[1]):
			print "-" * 30
			print str(feature)
			print "-" * 30
			for inner_feature in range(self.X.shape[1]):
				if feature != inner_feature:
					if abs(np.corrcoef(self.X[:, feature], self.X[:, inner_feature])[0, 1]) > 0.6:
						print inner_feature, np.corrcoef(self.X[:, feature],
							self.X[:, inner_feature])[0, 1], str(inner_feature)
						fm[inner_feature][feature] = abs(np.corrcoef(self.X[:, feature],
							self.X[:, inner_feature])[0, 1])

		plt.imshow(fm , cmap='YlGn')
		plt.colorbar()
		plt.show()


c = Correlation()
c.pearson()