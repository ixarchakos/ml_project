import os
import pickle
project_folder = os.path.dirname(__file__).split("src")[0]
from src.feature_extraction.extraction_skeleton import Feature_Extraction
from src.machine_learning.classification import Classification
from src.machine_learning.regression import Regression
from src.utils.feature_importance import feature_importance

if __name__ == "__main__":
    run_feature_extraction = False
    # feature extraction -- don't run it, takes a day
    if run_feature_extraction:
        features = Feature_Extraction()

    # load feature matrix
    feature_matrix = pickle.load(open(project_folder + '/dicts/last_fixed.p', 'rb'))

    # machine learning
    # classification - 9 classes with cross validation and PCA
    # it is a slow procedure!
    for num_of_features in [0]:
        print
        print "Features " + str(num_of_features)
        print "-" * 50
        c = Classification(num_of_features)
        c.grid_search(["all"])
        print "-" * 50

    # regression
    # Run lasso, xgboost and kernel ridge regression algorithms
    r = Regression()
    r.lasso()
    r.xgboost()
    r.kernelridge()

    # run feature importance
    feature_importance()