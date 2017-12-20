import numpy as np
import collections
import os
import pickle
from sklearn.linear_model import LogisticRegression , SGDClassifier
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier , ExtraTreesClassifier
from sklearn.preprocessing import scale
from xgboost.sklearn import XGBClassifier
from sklearn.svm import LinearSVC
project_folder = os.path.dirname(__file__).split("src")[0]


class Classification:
	def __init__(self):
		self.feature_names = pickle.load(open(project_folder+ 'dicts/feature_names.p' , 'rb'))
		X = pickle.load(open(project_folder+ 'dicts/third.p' , 'rb')).T
		y = pickle.load(open(project_folder+ 'dicts/roundedratings.p' , 'rb'))
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

	def logitic_regression(self):
		#self.X , self.testX = self.scale_sets(self.X, self.testX)
		clf = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1,
						   random_state=None, solver='liblinear', max_iter=1000, multi_class='ovr',
						   warm_start=False, n_jobs=-1)
		model = clf.fit(self.X, self.y)

		self.calculate_accuracy('Logistic', model)


	def random_forest(self):
		clf = RandomForestClassifier(n_estimators=500, criterion='gini', min_samples_split=2,
							   min_samples_leaf=2, max_leaf_nodes=100, n_jobs=-1)
		model = clf.fit(self.X, self.y)
		#self.calculate_accuracy('random forest', model)
		self.calculate_RMSE('random Forest' , model)

	def sgd(self):
		clf = SGDClassifier(alpha=.0001, n_iter=500, penalty="elasticnet", n_jobs=-1)
		model = clf.fit(self.X, self.y)
		self.calculate_accuracy('sgd', model)

	def gradient_bossting(self):
		clf = GradientBoostingClassifier(max_depth=10, max_leaf_nodes=850, min_samples_leaf=15, learning_rate=0.1)
		model = clf.fit(self.X , self.y)
		self.calculate_accuracy('Gradient Boosting' , model)

	def xtratree(self):
		clf = ExtraTreesClassifier(n_estimators=1000 , max_depth=100 , min_samples_leaf=3)
		model = clf.fit(self.X, self.y)
		self.calculate_accuracy('Xtra tree' , model)

	def XGB(self):
		clf = XGBClassifier()
		model = clf.fit(self.X, self.y)
		self.calculate_accuracy('XGB' , model)

	def linearSVM(self):
		clf = LinearSVC()
		model = clf.fit(self.X, self.y)
		self.calculate_RMSE('SVM' , model)
		self.calculate_accuracy('SVM' , model)


	def calculate_accuracy(self , name , model):
		train_pred = model.predict(self.X)
		print(name +' train accuracy = {}'.format((train_pred == self.y).mean()))
		test_pred = model.predict(self.testX)
		print(name + ' test accuracy = {}'.format((test_pred == self.testy).mean()))

	def calculate_RMSE(self, name , model):
		train_pred = model.predict(self.X)
		print(name + 'train RMSE = {}'.format(np.sqrt((train_pred - self.y) ** 2).mean()))
		test_pred = model.predict(self.testX)
		print(name + ' test RMSE = {}'.format(np.sqrt((test_pred - self.testy) ** 2).mean()))


	def scale_sets(self,x_train, x_test):
		x_train = scale(x_train) if x_train is not None else x_train
		x_test = scale(x_test) if x_test is not None else x_test
		return x_train, x_test





c = Classification()
#c.logitic_regression()
c.random_forest()
c.linearSVM()





