from kNNClassify import *
from numpy.random import permutation

def holdoutCVkNN(X, Y, perc, nrip, intK):
    """
    X: the dataset (test set excluded)
    Y: the labels (test set excluded)
    perc: percentage of the dataset to be used for validation
    nrip: number of repetitions of the test for each couple of parameters
    intK: list of regularization parameters
    for example intK = [1 3 5 7 9 11 17 21 31 41 51 71]

    Output:
    k: value k in intK that minimize the mean of the validation error
    Vm, Vs: mean and variance of the validation error for each couple of parameters
    Tm, Ts: mean and variance of the error computed on the training set for each couple
    of parameters

    Example of code:
    intK = np.array([1, 3, 5, 7, 9, 11, 17, 21, 31, 41, 51, 71])
    X, Y = MixGauss([[0, 0], [1, 1]], [0.5, 0.25], 1000)
    Y[Y==2] = -1
    k, Vm, Vs, Tm, Ts = holdoutCVkNN(X, Y, 0.5, 10, intK)
    plt.errorbar(intK, Vm, yerr=np.sqrt(Vs), color="b", label="Validation error")
    plt.hold("on")
    plt.errorbar(intK, Tm, yerr=np.sqrt(Ts), color='r', label="Training error")
    plt.legend()
    plt.title("Parameter selection for K-NN")
    plt.xlabel('k')
    plt.ylabel('Error')
    plt.show()
    """

    nK = np.prod(intK.shape)

    n = X.shape[0]
    ntr = int(np.ceil(n*(1-perc)))

    Tm = np.zeros(nK)
    Ts = np.zeros(nK)
    Vm = np.zeros(nK)
    Vs = np.zeros(nK)

    ym = (Y.max() + Y.min()) / 2.

    ik = 0
    for k in intK:
        for rip in range(nrip):

            I = permutation(n)

            # Training set
            Xtr = X[I[:ntr + 1], :]
            Ytr = Y[I[:ntr + 1]]

            # Validation set
            Xvl = X[I[ntr + 1:], :]
            Yvl = Y[I[ntr + 1:]]

            trError = calcErr(kNNClassify(Xtr, Ytr, k, Xtr), Ytr, ym)
            Tm[ik] = Tm[ik] + trError
            Ts[ik] = Ts[ik] + trError**2

            valError = calcErr(kNNClassify(Xtr, Ytr, k, Xvl), Yvl, ym)
            Vm[ik] = Vm[ik] + valError
            Vs[ik] = Vs[ik] + valError**2

            print('k: %2d, iter: %3d, valErr: %0.3f, trErr: %0.3f' % (k, rip, valError, trError))

        # Next ik
        ik = ik + 1

    # Average over trials
    Tm = Tm / nrip
    Ts = Ts / nrip - Tm**2

    Vm = Vm / nrip
    Vs = Vs / nrip - Vm**2

    # Optimum k selection (minimizes validation error)
    k = intK[Vm == Vm.min()].min()  # choose minimum k/model with least complexity

    return k , Vm, Vs, Tm, Ts


def calcErr(T, Y, m):
    #from IPython import embed; embed()
    vT = (T >= m)
    vY = (Y >= m)
    return  float(np.sum(vT.T != vY)) / np.prod(Y.shape)


if __name__ == "__main__":
    intK = np.array([1, 3, 5, 7, 9, 11, 17, 21, 31, 41, 51, 71])
    X, Y = MixGauss([[0, 0], [1, 1]], [0.5, 0.25], 1000)
    Y[Y==2] = -1
    k, Vm, Vs, Tm, Ts = holdoutCVkNN(X, Y, 0.5, 10, intK)

    plt.errorbar(intK, Vm, yerr=np.sqrt(Vs), color="b", label="Validation error")
    plt.hold("on")
    plt.errorbar(intK, Tm, yerr=np.sqrt(Ts), color='r', label="Training error")
    plt.legend()
    plt.title("Parameter selection for K-NN")
    plt.xlabel('k')
    plt.ylabel('Error')
    plt.show()
