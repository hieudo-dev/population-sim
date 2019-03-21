import numpy as np
from math import log


def Exponential(lmda):
	return -1 * (1.0 / lmda) * log(Uniform())

def Uniform():
	return np.random.uniform()