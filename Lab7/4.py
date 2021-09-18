import numpy as np
import matplotlib.pyplot as plt

# function for z axis
def f(x, y):
    return (x - 10) ** 2 + (y - 10) ** 2


fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection="3d")
# x and y axis
x = np.arange(-20, 50, 0.5)
y = np.arange(-20, 50, 0.5)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.title("3D Plot")
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False)

ax = fig.add_subplot(1, 2, 2)
ax.contour(X, Y, Z)
plt.title("Contour Plot")
plt.suptitle("3D graphs with contour")
plt.show()
