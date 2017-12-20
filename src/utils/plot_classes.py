
import matplotlib.pyplot as plt
import pickle

import os
project_folder = os.path.dirname(__file__).split("src")[0]
from sklearn.datasets import make_classification
X = pickle.load(open(project_folder + 'dicts/last_fixed.p', 'rb')).T
y = pickle.load(open(project_folder + 'dicts/roundedratings.p', 'rb'))

plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, edgecolor='k')
plt.show()