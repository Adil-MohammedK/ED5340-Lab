import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0, 2 * np.pi, 150)

radius = 0.4

x = radius * np.cos(angle)
y = radius * np.sin(angle)

fig, axe = plt.subplots(2, 2, figsize=(10, 8))
axe[0, 0].plot(x, y)
axe[0, 0].set_title("Parametric Circle")

axe[1, 0].plot(angle, x)
axe[1, 0].set_title("x-theta curve")

axe[1, 1].plot(angle, y)
axe[1, 1].set_title("y-theta curve")
# axes1.set_aspect(1)
plt.suptitle("MAIN TITLE")
plt.show()
