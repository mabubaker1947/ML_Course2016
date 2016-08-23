from MixGauss import *
from scipy.linalg import eigh

def PCA(X, k):
    """Computes the first k eigenvectors, eigenvalues and projections of the
    matrix X'*X/n where n is the number of rows in X.

    X is the dataset
    k is the number of components

    V is a matrix of the form [v_1, ..., v_k] where v_i is the i-th
    eigenvector
    d is the list of the first k eigenvalues
    X_proj is the projection of X on the linear space spanned by the
    eigenvectors in V
    """

    n = X.shape[0]
    m = X.shape[1]
    D, V = eigh(np.dot(X.T, X)/n, eigvals=(m-k, m-1))
    d = D * (D>0)
    ind = np.argsort(d)[::-1]
    d = d[ind]
    V = V[:,ind]
    X_proj = np.dot(X,V)

    return V, d, X_proj


if __name__ == "__main__":
    D = 30
    N = 1000
    sigma_noise = 0.01
    sigma = 0.7
    k = 10

    # 2.4
    #for sigma_noise in [0, 0.01, 0.1, 0.5, 0.7, np.linspace(1,2,5)]:

    # Draw from a Gaussian distribution
    X2tr, Y2tr = MixGauss([[1, 1], [-1, -1]], [2*sigma, sigma], 1000)
    Y2tr[Y2tr==1] = -1
    Y2tr[Y2tr==0] = 1

    X2ts, Y2ts = MixGauss([[1, 1], [-1, -1]], [sigma, sigma], 1000)
    Y2ts[Y2ts==1] = -1
    Y2ts[Y2ts==0] = 1

    # Add noise
    Xtr = np.concatenate((X2tr, normal(0, sigma_noise, size=(2*N, D-2))), axis=1)
    Xts = np.concatenate((X2ts, normal(0, sigma_noise, size=(2*N, D-2))), axis=1)

    V, d, X_proj = PCA(Xtr, k)

    # 2.2
    #plt.scatter(X_proj[:,0], X_proj[:,1], 25, Y2tr)
    #plt.axis('equal')
    #plt.title("Principal components")
    #plt.show()

    # 2.3
    #plt.plot(range(10), np.sqrt(d))
    #plt.title("10 largest eigenvalues") 
    #plt.show()

    #name = {0: "largest", 1: "second largest", 2: "third largest"}
    #for i in range(3):
    #    plt.title("Coefficients of the " + name[i] + " eigenvector")
    #    plt.scatter(range(D), np.abs(V[:,i]))
    #    plt.show()
    #print V.shape
