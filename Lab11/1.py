import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# In[4]
data = pd.read_csv("univariate_linear_regression.csv")
x_train = np.ones((len(data), 1))
x_train[:, 0] = data.x
X = x_train
y = data.y
reg = LinearRegression().fit(X, y)

# In[5]
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[3], [5]])))
# In[6]
plt.scatter(X, y)
x = np.linspace(-10, 10, 100)
y = reg.coef_[0] * x + reg.intercept_
plt.plot(x, y, "-r", label="y")
plt.title("Graph of y")
plt.xlabel("x", color="#1C2833")
plt.ylabel("y", color="#1C2833")
plt.legend(loc="upper left")
plt.grid()
plt.show()
# %%
