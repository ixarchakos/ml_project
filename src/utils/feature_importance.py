
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.ensemble import RandomForestClassifier
import os
project_folder = os.path.dirname(__file__).split("src")[0]
# Build a classification task using 3 informative features

def feature_importance():
    X = pickle.load(open(project_folder + 'dicts/last_fixed.p', 'rb')).T
    y = pickle.load(open(project_folder + 'dicts/roundedratings.p', 'rb'))

    # Build a forest and compute the feature importances
    forest = RandomForestClassifier(min_samples_split=0.1, n_estimators=200, criterion='gini')

    forest.fit(X, y)
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    print("Feature ranking:")

    for f in range(X.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(X.shape[1]), importances[indices],
           color="r", yerr=std[indices], align="center")
    plt.xticks(range(X.shape[1]), indices)
    plt.xlim([-1, X.shape[1]])
    plt.show()