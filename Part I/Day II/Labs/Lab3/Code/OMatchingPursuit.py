from MixGauss import *
from calcErr import *

def OMatchingPursuit(X, Y, T):
    """Orthogonal Maching Pursuit

    X input data
    Y output labels
    T number of iterations

    w estimated coefficients
    r residuals
    I indices"""

    N, D = X.shape

    # Initialization of residual, coefficient vector and index set I
    r = Y
    w = np.zeros(D)
    I = []

    for i in range(T-1):
        I_tmp = range(D)

		# Select the column of X which most "explains" the residual
        a_max = -1
        for j in I_tmp:
            a_tmp = (np.dot(r.T, X[:,j])**2) / (np.dot(X[:,j].T, X[:,j]))
            if a_tmp > a_max:
                a_max = a_tmp
                j_max = j

		# Add the index to the set of indexes
        if np.sum(I == j_max) == 0:
            I.append(j_max)

        # Compute the M matrix
        M_I = np.zeros((D,D))
        for j in I:
            M_I[j,j] = 1

        A = np.dot(np.dot(M_I, X.T), np.dot(X, M_I))
        B = np.dot(np.dot(M_I, X.T), Y)

		# Update w
        w = np.dot(np.linalg.pinv(A), B)

		# Update the residual
        r = Y - np.dot(X, w)


    return w, r, I

if __name__ == "__main__":
    D = 30
    N = 1000
    sigma_noise = 0.01
    sigma = 0.7

    # Draw from a Gaussian distribution
    X2tr, Y2tr = MixGauss([[1, 1], [-1, -1]], [sigma, sigma], 1000)
    Y2tr[Y2tr==1] = -1
    Y2tr[Y2tr==0] = 1

    X2ts, Y2ts = MixGauss([[1, 1], [-1, -1]], [sigma, sigma], 1000)
    Y2ts[Y2ts==1] = -1
    Y2ts[Y2ts==0] = 1

    # Add noise
    Xtr = np.concatenate((X2tr, normal(0, sigma_noise, size=(2*N, D-2))), axis=1)
    Xts = np.concatenate((X2ts, normal(0, sigma_noise, size=(2*N, D-2))), axis=1)

    mean = np.mean(Xtr, axis=0)
    std = np.std(Xtr, axis=0, ddof=1)

    Xts -= mean
    Xtr -= mean
    Xts = Xts/std
    Xtr = Xtr/std

    error = []
    T = range(1, 10)
    for t in T:
        w, r, I = OMatchingPursuit(Xtr, Y2tr, t)
        Ypred = np.sign(np.dot(Xts, w))
        error.append(calcErr(Y2ts, Ypred))
        #plt.stem(range(D), w)
        #plt.xlim([-1, D])
        #plt.show()

    plt.plot(T, error)
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')
    plt.show()
