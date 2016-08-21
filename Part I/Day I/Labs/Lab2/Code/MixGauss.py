import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

def MixGauss(means, sigmas, n):
    """Class MixGauss(means, sigmas, n)

    means: (size dxp) and should be of the form [m1, ... ,mp]
    sigmas: (size px1) should be in the form [sigma_1;...; sigma_p]
    n: number of points per class
    X: obtained input data matrix (size 2n x d)
    Y: obtained output data vector (size 2n)
    
    X, Y = MixGauss([[0, 0], [1,0], [1,1], [0, 1]], [0.2, 0.1, 0.2, 0.1], 200)
    plt.scatter(X[:,0], X[:,1], 25, Y)
    plt.title("Synthetic data with Gaussian distribution")
    plt.show()
    """

    d = len(sigmas)

    X = np.zeros((n*d, 2))
    Y = np.zeros(n*d)
    for i, s in enumerate(sigmas):
        X[i*n:(i+1)*n, 0] = normal(means[i][0], s, n)
        X[i*n:(i+1)*n, 1] = normal(means[i][1], s, n)
        Y[i*n:(i+1)*n] = i

    return X, Y


if __name__ == "__main__":
    # Run example
    X, Y = MixGauss([[0, 0], [1,0], [1,1], [0, 1]], [0.2, 0.1, 0.2, 0.1], 200)
    plt.scatter(X[:,0], X[:,1], 25, Y)
    plt.title("Synthetic data with Gaussian distribution")
    plt.show()



