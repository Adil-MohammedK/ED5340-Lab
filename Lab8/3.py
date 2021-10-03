import numpy as np
import matplotlib.pyplot as plt


def f1(x, y):
    return (x - 10) ** 2 + (y - 10) ** 2


def plot3D(Func, xlimit, ylimit, title="3D plot"):

    fig = plt.figure(figsize=(18, 7))
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    # x and y axis
    x = np.arange(-xlimit, xlimit, 0.5)
    y = np.arange(-ylimit, ylimit, 0.5)
    X, Y = np.meshgrid(x, y)
    Z = Func(X, Y)
    plt.title(title)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, cmap="viridis_r")


def plotContour(Func, xlimit, ylimit, title="Contour plot"):

    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(1, 1, 1)
    x = np.arange(-xlimit, xlimit, 0.5)
    y = np.arange(-ylimit, ylimit, 0.5)
    X, Y = np.meshgrid(x, y)
    Z = Func(X, Y)
    cp = ax.contour(X, Y, Z)
    plt.clabel(cp, fontsize=8)
    plt.title(title)
    plt.suptitle("3D graphs with contour")
    # Mark start point
    ax.plot(*s_point, "ko")
    ax.annotate("Start point", s_point)
    # Mark optimal point
    ax.plot(x_opt, y_opt, "ko")
    ax.annotate(f"Optimal point, alpha=({round(alpha_opt, 2)})", (x_opt, y_opt))
    # Draw search direction
    points = np.array([s_point + a * s_dirn for a in range(4)])
    ax.plot(points[:, 0], points[:, 1], "b--")

    plt.show()


def get_param(f_mv, start, drx):
    def parametric(alpha):
        return f_mv(*(start + alpha * drx))

    return parametric


def bracket_search(obj, a=-100, b=100, n=10):
    x1 = a
    dx = (b - a) / n
    x2 = x1 + dx
    x3 = x2 + dx
    while not (obj(x1) >= obj(x2) and obj(x2) <= obj(x3)):
        x1 = x2
        x2 = x3
        x3 = x2 + dx
        if x3 > b:
            return False, None, None
    return True, (x1, x3)


def interval_halving(obj, a, b, errlim=1e-5):
    while abs(b - a) > errlim:
        xm = (a + b) / 2
        x1 = (a + xm) / 2
        x2 = (xm + b) / 2
        if obj(x1) < obj(xm):
            b, xm = xm, x1
        else:
            if obj(x2) < obj(xm):
                a, xm = xm, x2
            else:
                a, b = x1, x2

    return (a + b) / 2


# My Starting point
s_point = np.array([2, 1])
# My Search direction
s_dirn = np.array([2, 5])

alpha_fun = get_param(f1, s_point, s_dirn)
# Find Crude bounds
found, (a, b) = bracket_search(alpha_fun, n=100)
# find optimal value of alpha
alpha_opt = interval_halving(alpha_fun, a, b)
# Find the optimal x and y values
x_opt, y_opt = s_point + alpha_opt * s_dirn
print("Optimal value is ", x_opt, y_opt)


plot3D(f1, 30, 30)
plotContour(f1, 30, 30)
