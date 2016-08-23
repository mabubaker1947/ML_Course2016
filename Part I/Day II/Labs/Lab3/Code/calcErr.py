import numpy as np

def calcErr(T, Y):
    return np.mean(np.sign(T) != np.sign(Y))
