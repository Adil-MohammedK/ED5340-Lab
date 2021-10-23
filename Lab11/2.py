from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# In[4]
my_data = pd.read_csv("Logistic_regression_ls.csv")
x_train = np.ones((len(my_data), 2))
x_train[:, 0] = my_data.x1
x_train[:, 1] = my_data.x2
y_train = my_data.label

# In[5]
clf = LogisticRegression().fit(x_train, y_train)
print("Coefficients: ", clf.coef_)
print("Intercepts: ", clf.intercept_)

print(clf.predict(x_train[:2, :]))
print(clf.predict_proba(x_train[:2, :]))

print(clf.score(x_train, y_train))

# %%
fig = plt.figure(figsize=(18, 7))
ax = fig.add_subplot(1, 2, 1)
ax.scatter(x_train[:, 0], x_train[:, 1])
x = np.arange(0, 9, 1)
y = (-clf.intercept_[0] - clf.coef_[0][0] * x) / clf.coef_[0][1]
ax.plot(x, y, "r-")
ax.set_xlabel("x0")
ax.set_ylabel("x1")
ax.set_title("Logistic regression fit", fontsize=20)  # set title
plt.show()

# %%
