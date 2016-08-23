from OMatchingPursuit import *
from numpy.random import permutation

def holdoutCVOMP(X, Y, perc, nrip, intIter):
    """
    X: the training examples
    Y: the training labels
    perc: fraction of the dataset to be used for validation
    nrip: number of repetitions of the test for each couple of parameters
    intIter: range of iteration for the Orthogonal Matching Pursuit

    Output:
    it: the number of iterations of OMP that minimize the classification
    error on the validation set
    Vm, Vs: median and variance of the validation error for each couple of parameters
    Tm, Ts: median and variance of the error computed on the training set for each couple
    of parameters
    """

    nIter = len(intIter)

    n = X.shape[0]
    ntr = int(np.ceil(n*(1-perc)))

    tmn = np.zeros((nIter, nrip))
    vmn = np.zeros((nIter, nrip))

    for rip in range(nrip):
        I = permutation(n)
        Xtr = X[I[:ntr + 1], :]
        Ytr = Y[I[:ntr + 1]]
        Xvl = X[I[ntr+1:], :]
        Yvl = Y[I[ntr+1:]]

        iit = 0
        for it in intIter:
            w = OMatchingPursuit(Xtr, Ytr, it)[0]
            tmn[iit, rip] = calcErr(np.dot(Xtr,w), Ytr)
            vmn[iit, rip] = calcErr(np.dot(Xvl,w), Yvl)

            print('rip\tIter\tvalErr\ttrErr\n%d\t%d\t%01.05f\t%01.05f' % (rip, it, vmn[iit,rip], tmn[iit,rip]))
            iit = iit + 1;

    Tm = np.median(tmn, axis=1)
    Ts = np.std(tmn, ddof=1, axis=1)
    Vm = np.median(vmn, axis=1)
    Vs = np.std(vmn, ddof=1, axis=1)

    row = (Vm == Vm.min()).nonzero()[0]
    it = intIter[row[0]]

    return it, Vm, Vs, Tm, Ts


if __name__ == "__main__":
    perc = 0.5
    nrip = 30
    D = 30
    N = 1000
    sigma_noise = 0.01
    sigma = 0.7
    intIter = range(2, D)

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

    it, Vm, Vs, Tm, Ts = holdoutCVOMP(Xtr, Y2tr, 0.5, 5, intIter)
    plt.errorbar(intIter, Vm, fmt="-o", yerr=Vs, color="b", label="Validation error")
    plt.hold("on")
    plt.errorbar(intIter, Tm, fmt="-o", yerr=Ts, color='r', label="Training error")
    plt.legend() 
    plt.title("Selection of the Iteration Number for OMP")
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')
    plt.show()
