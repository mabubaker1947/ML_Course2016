from kNNClassify import *

def separatingFkNN(Xtr, Ytr, k, step=0.1):
    """ Class separatingF(Xtr,Ytr,k)

 Classifies points on a regular grid sampled using k-Nearest Neighbors
 (kNNClassify) and plots the separating contour.

 Xtr - training examples
 Ytr - training labels
 k - number of neighbors for kNN
 step - spacing in x,y directions for grid: 0.1 (default)

 Example:
 Xtr, Ytr = MixGauss([[0, 0], [0,1], [1, 1], [1,0]], [0.5, 0.2, 0.25, 0.25], 100)
 Ytr = (Ytr % 2) * 2 - 1 
 Xts, Yts = MixGauss([[0, 0], [0,1], [1, 1], [1,0]], [0.5, 0.2, 0.25, 0.25], 100)
 Yts = (Yts % 2) * 2 - 1
 k = 10
 separatingFkNN(Xtr, Ytr, k)
 plt.hold("on")
 plt.scatter(Xts[:, 0], Xts[:, 1], 25, Yts)
 plt.show()

"""

    # Define regular grid using training set X
    x_N = int((Xtr[:,0].max() - Xtr[:, 0].min()) / step)
    y_N = int((Xtr[:,1].max() - Xtr[:, 1].min()) / step)
    x = np.linspace(Xtr[:,0].min(), Xtr[:, 0].max(), x_N)
    y = np.linspace(Xtr[:,1].min(), Xtr[:, 1].max(), y_N)

    X, Y = np.meshgrid(x, y)

    XGrid = np.concatenate((X.reshape(x_N*y_N, 1), Y.reshape(x_N*y_N, 1)), axis=1) # Add one to the other

    # Classify points in the grid
    YGrid = kNNClassify(Xtr, Ytr,  k, XGrid);

    # Draw contour
    Ygrid = YGrid.reshape(np.prod(y.shape), np.prod(x.shape))
    plt.contour(x, y, YGrid.reshape(y_N, x_N), [0])


if __name__ == "__main__":
    Xtr, Ytr = MixGauss([[0, 0], [0,1], [1, 1], [1,0]], [0.5, 0.2, 0.25, 0.25], 100)
    Ytr = (Ytr % 2) * 2 - 1
    Xts, Yts = MixGauss([[0, 0], [0,1], [1, 1], [1,0]], [0.5, 0.2, 0.25, 0.25], 100)
    Yts = (Yts % 2) * 2 - 1
    k = 10
    separatingFkNN(Xtr, Ytr, k)
    plt.hold("on")
    plt.scatter(Xts[:, 0], Xts[:, 1], 25, Yts)
    plt.show()
