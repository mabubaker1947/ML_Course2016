from SquareDist import *
from MixGauss import *

def kNNClassify(Xtr, Ytr, k, Xte):
    """ Class kNNClassify(Xtr, Ytr, k, Xte)

    INPUT PARAMETERS
    Xtr training input
    Ytr training output
    k number of neighbours
    Xte test input

    OUTPUT PARAMETERS
    Ypred estimated test output

    EXAMPLE
    kNNClassify(Xtr, Ytr, 5, Xte);
    """

    n = Xtr.shape[0]
    m = Xte.shape[0]

    if k > n:
        k = n

    ylab = np.unique(Ytr);
    ym = np.sum(ylab) / 2.

    # Center output (if output is not in {-1, 1})
    Ytrm = Ytr - ym

    Ypred = np.zeros((m, 1))

    DistMat = SquareDist(Xtr, Xte)

    for j in range(m):
        SortdDistMat = DistMat[:,j]

        I = np.argsort(SortdDistMat)
        idx = I[:k]

        # Assumes labels are {-1,1}.  
        val = np.sum(Ytrm[idx] / k)

        Ypred[j] = np.sign(val)

    # Map back to original output vals
    Ypred = Ypred + ym
    return Ypred

if __name__ == "__main__":
    print "No running example, see separate"
