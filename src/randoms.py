import numpy as np
from math import log


def Exponential(lmda):
	return -1 * (1.0 / lmda) * log(Uniform())

def Uniform(l=0.0, r=1.0):
	return np.random.uniform(low=l, high=r)