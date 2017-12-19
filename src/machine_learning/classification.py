import numpy as np
import os
import pickle
from sklearn.linear_model import LogisticRegression , SGDClassifier
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier , ExtraTreesClassifier
from sklearn.preprocessing import scale
from xgboost.sklearn import XGBClassifier
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.decomposition import PCA
project_folder = os.path.dirname(__file__).split("src")[0]


class Classification:

	def __init__(self, number_of_features=0):
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
		if number_of_features > 0:
			print "PCA procedure starts"
			self.X, self.testX = self.dimensionality_reduction(self.X, self.testX, number_of_features)

		print self.X.shape , self.y.shape, self.testX.shape, self.testy.shape
		print '********************************************************'

	def create_data_sets(self, X, y):
		return train_test_split(X,y , test_size = 0.20 , random_state=42)

	def logitic_regression(self):
		#self.X , self.testX = self.scale_sets(self.X, self.testX)
		clf = LogisticRegression(n_jobs=-1)
		model = clf.fit(self.X, self.y)
		self.calculate_accuracy('Logistic', model)
		self.calculate_RMSE("Logistic", model)


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
		clf = GradientBoostingClassifier(loss="exponential", max_depth=10, max_leaf_nodes=350, min_samples_leaf=15, learning_rate=0.01)
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
		self.calculate_RMSE('SVM', model)
		self.calculate_accuracy('SVM', model)

	def calculate_f1(self, name, model):
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

	def dimensionality_reduction(self, train, test, components=25):
			return PCA(n_components=components).fit_transform(train), PCA\
			(n_components=components).fit_transform(test)

	def grid_search(self, algorithm_list):
		# XGBoost parameters
		# Random Forest parameters
		rfc_params = [{"criterion": ["gini", "entropy"], "min_samples_split": [i / 10.0 for i in range(1, 11)],
		"n_estimators": [i for i in range(200, 601, 100)]}]
		# Logistic Regression parameters
		lr_params = [{"penalty": ["l1", "l2"], "tol": [1e-3, 1e-4, 1e-5]}]
		# Linear SVC
		lsvc_params = [{"tol": [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7], "C": [i / 10.0 for i in range(1, 22, 1)]}]
		# mlp parameters
		mlp_params = [{"hidden_layer_sizes": [(100, 50), (150, 100), (250, 150), (400, 250), (150, 100, 50)],
		"momentum": [0.6, 0.7, 0.8], "batch_size": [25, 50, 75], "learning_rate":["adaptive"],
		"activation": ["logistic"]}]
		# Multinomial Naive Bayes parameters
		mnb_params = [{"alpha": [i / 10.0 for i in range(1, 11)]}]
		# Grid search
		for algorithm in algorithm_list:

			if algorithm_list[0] == "all":
				self.grid_search(["lr", "svc", "rfc", "mlp", "mnb", "xgb"])
			if algorithm == "lr":
				model = GridSearchCV(LogisticRegression(), lr_params, n_jobs=-1, cv=10).fit(self.X, self.y)
				self.print_results(model, "LogisticRegression")
			elif algorithm == "svc":
				model = GridSearchCV(LinearSVC(), lsvc_params, n_jobs=-1, cv=10).fit(self.X, self.y)
				self.print_results(model, "SVC")
			elif algorithm == "rfc":
				model = GridSearchCV(RandomForestClassifier(), rfc_params, n_jobs=-1, cv=10).fit(self.X, self.y)
				self.print_results(model, "RandomForests")
			elif algorithm == "mlp":
				model = GridSearchCV(MLPClassifier(), mlp_params, n_jobs=-1, cv=10).fit(self.X, self.y)
				self.print_results(model, "MLP")
			elif algorithm == "mnb":
				model = GridSearchCV(MultinomialNB(), mnb_params, n_jobs=-1, cv=10).fit(self.X, self.y)
				self.print_results(model, "MultinomialNB")
			elif algorithm == "xgb":
				model = GridSearchCV(XGBClassifier(), {}, n_jobs=-1, cv=2, verbose=True).fit(self.X, self.y)
				self.print_results(model, "XGBoost")

	def print_results(self, model, msg):
		print(msg + " best parameters: " + str(model.best_params_))
		self.calculate_accuracy(msg, model)
		self.calculate_RMSE(msg, model)
		self.calculate_f1(msg, model)


# Grid search with all the features and PCA with 15, 25, 30, 40 principal components
for features in [20]:
	print
	print "Features " + str(features)
	print "-"*50
	c = Classification(features)
	c.grid_search(["all"])
	print "-" * 50


c = Classification()
#c.logitic_regression()
c.random_forest()
c.linearSVM()
