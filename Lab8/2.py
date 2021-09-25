import matplotlib.pyplot as plt
import numpy as np


def f1(x, y):
    return (x - 2) ** 2 + (y - 2) ** 2


def f2(x, y):
    return x ** 2 - y ** 2


def plot3D(Func, xlimit, ylimit, title):

    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    # x and y axis
    x = np.arange(-xlimit, xlimit, 0.5)
    y = np.arange(-ylimit, ylimit, 0.5)
    X, Y = np.meshgrid(x, y)
    Z = Func(X, Y)
    plt.title(title)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)


def plotContour(Func, xlimit, ylimit, title):

    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 2)
    x = np.arange(-xlimit, xlimit, 0.5)
    y = np.arange(-ylimit, ylimit, 0.5)
    X, Y = np.meshgrid(x, y)
    Z = Func(X, Y)
    cp = ax.contour(X, Y, Z)
    plt.clabel(cp, fontsize=8)
    plt.title(title)
    plt.suptitle("3D graphs with contour")
    plt.show()


plot3D(f1, 20, 20, "3D plot for f1")
plotContour(f1, 20, 20, "Contour plot for f1")

plot3D(f2, 20, 20, "3D plot for f1")
plotContour(f2, 20, 20, "Contour plot for f1")
plt.show()
# ax = fig.add_subplot(1, 2, 2)
# cp = ax.contour(X, Y, Z)
# plt.clabel(cp, fontsize=8)
# plt.title("Contour Plot")
# plt.suptitle("3D graphs with contour")
# plt.show()
