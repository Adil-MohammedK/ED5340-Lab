import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import sympy as sp
from math import fabs, sqrt


def f1(x, y):
    return (x - 10) ** 2 + (y - 10) ** 2


fstr = "(x-10)**2+(y-10)**2"


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


# calculating partial derivative
def partial_derivative_x_y(ginput, der_var, val):

    x, y = sp.symbols("x y")
    function = lambda x, y: ginput
    derivative_x = sp.lambdify((x, y), sp.diff(function(x, y), x))
    derivative_y = sp.lambdify((x, y), sp.diff(function(x, y), y))
    if der_var == "x":
        return derivative_x(val[0], val[1])
    if der_var == "y":
        return derivative_y(val[0], val[1])


def gradDescent(Func, xinit, yinit, iter, limit1, limit2):

    s_point = np.array([xinit, yinit])
    s_dirn = np.array(
        [
            -partial_derivative_x_y(fstr, "x", (xinit, yinit)),
            -partial_derivative_x_y(fstr, "y", (xinit, yinit)),
        ]
    )
    delJ = np.array(
        [
            partial_derivative_x_y(fstr, "x", (xinit, yinit)),
            partial_derivative_x_y(fstr, "y", (xinit, yinit)),
        ]
    )
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    x = np.arange(-30, 30, 0.5)
    y = np.arange(-30, 30, 0.5)
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
        # Find the optimal x and y values
        x_opt, y_opt = s_point + alpha_opt * s_dirn

        delJ = np.array(
            [
                partial_derivative_x_y(fstr, "x", (s_point[0], s_point[1])),
                partial_derivative_x_y(fstr, "y", (s_point[0], s_point[1])),
            ]
        )

        if fabs(sqrt(delJ[0] ** 2 + delJ[1] ** 2)) <= limit1:
            break
        elif x > iter:
            break

        x_new = s_point[0] + alpha_opt * s_dirn[0]
        y_new = s_point[1] + alpha_opt * s_dirn[1]

        if (
            fabs(
                sqrt(
                    partial_derivative_x_y(fstr, "x", (x_new, y_new)) ** 2
                    + partial_derivative_x_y(fstr, "y", (s_point[0], s_point[1])) ** 2
                )
            )
            <= limit2
        ):
            break

        if (
            fabs(sqrt((x_new - s_point[0]) ** 2 + (y_new - s_point[1]) ** 2)) / sqrt(s_point[1] ** 2 + s_point[1] ** 2)
        ) <= limit1:
            break

        # Mark optimal point
        ax.plot(x_opt, y_opt, "ko")
        ax.annotate(f"point {(x+1)} at {(x_opt,y_opt)}, alpha=({round(alpha_opt, 3)})", (x_opt, y_opt))
        # Draw search direction
        points = np.array([s_point + a * s_dirn for a in range(2)])
        ax.plot(points[:, 0], points[:, 1], "b--")

        s_point = np.array([x_new, y_new])
        s_dirn = np.array(
            [
                -partial_derivative_x_y(fstr, "x", (s_point[0], s_point[1])),
                -partial_derivative_x_y(fstr, "y", (s_point[1], s_point[1])),
            ]
        )

    return x_new, y_new, x


x_opt, y_opt, niter = gradDescent(f1, 2, 1, 100, 0.001, 0.001)
print(f"Optimal value is {(x_opt, y_opt)}")
print("number of iteration: ", niter)
plot3D(f1, 30, 30)
plt.show()
