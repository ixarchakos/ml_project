import numpy as np
import collections
import os
import pickle
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import Lasso


project_folder = os.path.dirname(__file__).split("src")[0]


class Regression:
	def __init__(self):
		self.feature_names = pickle.load(open(project_folder+ 'dicts/feature_names.p' , 'rb'))
		X = pickle.load(open(project_folder+ 'dicts/third.p' , 'rb')).T
		y = pickle.load(open(project_folder+ 'dicts/ratings.p' , 'rb'))
		self.n = X.shape[0]
		self.d = X.shape[1]
		print 'Feature matrix X with shape:' , X.shape , 'is loaded'
		print 'Target Vector y with shape:' , y.shape, 'is loaded'
		print '********************************************************'
		print 'Create training and test sets with following shapes: '
		self.X,self.testX,self.y, self.testy = self.create_data_sets(X,y)
		print self.X.shape , self.y.shape, self.testX.shape, self.testy.shape
		print '********************************************************'

	def create_data_sets(self, X, y):
		return train_test_split(X,y , test_size = 0.20 , random_state=42)

	def xgboost(self):
		clf = XGBRegressor(n_estimators=150, learning_rate=0.08, gamma=0, subsample=0.75,
								   colsample_bytree=1, max_depth=7)

		model = clf.fit(self.X , self.y)
		self.calculate_RMSE('XGB' , model)

	def kernelridge(self):
		clf = KernelRidge(alpha = 1 , kernel='rbf' , degree = 1)
		model =clf.fit(self.X,self.y)
		self.calculate_RMSE('Kernel Ridge' , model)

	def lasso(self):
		clf = Lasso()
		model = clf.fit(self.X, self.y)
		self.calculate_RMSE('Lasso' , model)

	def calculate_RMSE(self, name , model):
		train_pred = model.predict(self.X)
		print(name + ' train RMSE = {}'.format(np.sqrt((train_pred - self.y) ** 2).mean()))
		test_pred = model.predict(self.testX)
		print(name + ' test RMSE = {}'.format(np.sqrt((test_pred - self.testy) ** 2).mean()))


r = Regression()
r.xgboost()
r.kernelridge()