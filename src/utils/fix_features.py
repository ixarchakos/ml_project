import numpy as np
import collections
import os
import pickle
project_folder = os.path.dirname(__file__).split("src")[0]

def fix_features():
	first = load_dict('first')
	second = load_dict('second')
	third = load_dict('third')
	last = load_dict('last')

	print first.shape
	print second.shape
	print third.shape
	print last.shape

	second_fixed = np.concatenate((first[0:37] , second[37:]))
	print second_fixed.shape
	save_dict('second_fixed' , second_fixed )
	third_fixed = np.concatenate((first[0:37] , third[37:]))
	print third_fixed.shape
	save_dict('third_fixed' , third_fixed )

	last_fixed = np.concatenate((first[0:37], last[37:]))
	print last_fixed.shape
	save_dict('last_fixed' , last_fixed )


def load_dict(name):
	return pickle.load(open(project_folder + 'dicts/' + name + '.p', 'rb'))

def save_dict(name ,dict):
	pickle.dump(dict, open(project_folder + 'dicts/' + name + '.p' , 'wb'))

fix_features()