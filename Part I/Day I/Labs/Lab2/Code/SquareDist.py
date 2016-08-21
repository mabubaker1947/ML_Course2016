import numpy as np

def SquareDist(X1, X2):
    """SQUAREDIST - computes Euclidean SQUARED distance matrix

    E = distance(X1, X2)
    X1 - (NxD) matrix
    X2 - (MxD) matrix
    
    Returns:
    E - (NxM) Euclidean SQUARED distances between vectors in X1 and X2
    """

    N = X1.shape[0]
    M = X2.shape[0]
    a = np.ones((N, M))

    D = (a.T * np.sum(X1**2, axis=1)).T
    D += a * np.sum(X2**2, axis=1)
    D -= 2 * np.dot(X1, X2.T)

    return D

if __name__ == "__main__":
    a = [[1*i,2*i,4*i,5*i] for i in range(10)]
    b = [[3*i,6*i,3*i,3*i] for i in range(4)]
    D = SquareDist(np.asarray(a), np.asarray(b))
    print D


    """
   [[    0.    63.   252.   567.]
    [   46.    25.   130.   361.]
    [  184.    79.   100.   247.]
    [  414.   225.   162.   225.]
    [  736.   463.   316.   295.]
    [ 1150.   793.   562.   457.]
    [ 1656.  1215.   900.   711.]
    [ 2254.  1729.  1330.  1057.]
    [ 2944.  2335.  1852.  1495.]
    [ 3726.  3033.  2466.  2025.]]
    """
