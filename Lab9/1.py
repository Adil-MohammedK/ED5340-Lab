import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import sympy as sp
from math import fabs, sqrt
import pandas as pd
import csv


def costFn(w0, w1, diff=None):
    if diff == None:
        sum = 0
        for i in range(len(data)):
            sum += (w0 + w1 * data.iloc[i].x - data.iloc[i].y) ** 2
        return sum / (2 * len(data))
    elif diff == "x":
        sum = 0
        for i in range(len(data)):
            sum += w0 + w1 * data.iloc[i].x - data.iloc[i].y
        return sum / (len(data))
    elif diff == "y":
        sum = 0
        for i in range(len(data)):
            sum += (w0 + w1 * data.iloc[i].x - data.iloc[i].y) * data.iloc[i].x
        return sum / (len(data))


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

    plt.show()


def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    x = np.linspace(-10, 10, 100)
    y = slope * x + intercept
    plt.plot(x, y, "-r", label="y")
    plt.title("Graph of y")
    plt.xlabel("x", color="#1C2833")
    plt.ylabel("y", color="#1C2833")
    plt.legend(loc="upper left")
    plt.grid()


def plotPoints():
    data.plot.scatter(x="x", y="y")


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


def deriv(Func, x):
    return derivative(Func, x, dx=1e-6)


def dubderiv(Func, x):
    return derivative(derivative(Func, x, dx=1e-6), x, dx=1e-6)


def newtonRaph(Func, init, iter=100):
    print("Newton=Raphson Method")
    w1 = init
    k = 1
    wk = w1
    iterations = iter
    for x in range(0, iterations):
        wk1 = wk - (deriv(Func, wk) / wk)
        if fabs(deriv(Func, wk1)) < 0.0001:
            break
        else:
            k += 1
            wk = wk1
    return wk


# calculating partial derivative
def partial_derivative_x_y(der_var, val):

    derivative_x = costFn(val[0], val[1], "x")
    derivative_y = costFn(val[0], val[1], "y")
    if der_var == "x":
        return derivative_x
    if der_var == "y":
        return derivative_y


def gradDescent(Func, xinit, yinit, iter, limit1, limit2):

    s_point = np.array([xinit, yinit])
    s_dirn = np.array(
        [
            -partial_derivative_x_y("x", (xinit, yinit)),
            -partial_derivative_x_y("y", (xinit, yinit)),
        ]
    )
    delJ = np.array([s_dirn[0] * -1, s_dirn[1] * -1])

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(-30, 30, 60)
    y = np.linspace(-30, 30, 60)
    X, Y = np.meshgrid(x, y)
    Z = Func(X, Y)
    cp = ax.contour(X, Y, Z)
    plt.clabel(cp, fontsize=7)
    plt.title("Contour plot")
    plt.suptitle("3D graphs with contour")
    # Mark start point
    ax.plot(*s_point, "ko")
    ax.annotate(f"Point 0 at {(s_point[0],s_point[1])}", s_point)

    for x in range(iter):

        # ax.plot(*s_point, "ko")
        # ax.annotate("Start point", s_point)

        f_sv = get_param(Func, s_point, s_dirn)
        # crude bounds of alpha
        found, (a, b) = bracket_search(f_sv, n=100)
        # optimal value of alpha
        alpha_opt = interval_halving(f_sv, a, b)
        # alpha_opt = newtonRaph(f_sv, a, 100)
        # Find the optimal x and y values
        x_opt, y_opt = s_point + alpha_opt * s_dirn

        delJ = np.array(
            [
                partial_derivative_x_y("x", (s_point[0], s_point[1])),
                partial_derivative_x_y("y", (s_point[0], s_point[1])),
            ]
        )

        if fabs(sqrt(delJ[0] ** 2 + delJ[1] ** 2)) <= limit1:
            print("Breaking at limit2")
            break
        elif x > iter:
            print("iterations limit")
            break

        x_new = s_point[0] + alpha_opt * s_dirn[0]
        y_new = s_point[1] + alpha_opt * s_dirn[1]

        if fabs(sqrt(partial_derivative_x_y("x", (x_new, y_new)) ** 2 + delJ[1] ** 2)) <= limit2:
            print("Breaking at limit2 after new point")
            break

        if (
            fabs(sqrt((x_new - s_point[0]) ** 2 + (y_new - s_point[1]) ** 2)) / sqrt(s_point[1] ** 2 + s_point[1] ** 2)
        ) <= limit1:
            print("breaking at limit1")
            break

        # Mark optimal point
        ax.plot(x_opt, y_opt, "ko")
        # ax.annotate(f"point {(x+1)} at {(x_opt,y_opt)}, alpha=({round(alpha_opt, 3)})", (x_opt, y_opt))
        # Draw search direction
        points = np.array([s_point + a * s_dirn for a in range(2)])
        ax.plot(points[:, 0], points[:, 1], "b--")

        s_point = np.array([x_new, y_new])
        s_dirn = np.array(
            [
                -partial_derivative_x_y("x", (s_point[0], s_point[1])),
                -partial_derivative_x_y("y", (s_point[1], s_point[1])),
            ]
        )
    ax.plot(x_new, y_new, "ko")
    ax.annotate(f"Final point at {round(x_new,3),round(y_new,3)}, alpha=({round(alpha_opt, 3)})", (x_new, y_new))

    return x_new, y_new, x


data = pd.read_csv("univariate_linear_regression.csv")
print(data.iloc[0].x)
# print(len(data))
# print(costFn(1, 2, data))

x_opt, y_opt, niter = gradDescent(costFn, 15, -10, 100, 0.0001, 0.0001)
print(f"Optimal value is {(x_opt, y_opt)}")
print("number of iteration: ", niter)
plot3D(costFn, 30, 30)
plotPoints()
abline(y_opt, x_opt)
plt.show()
