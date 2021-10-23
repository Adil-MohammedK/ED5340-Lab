import numpy as np
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# In[4]
my_data = pd.read_csv("Logistic_regression_ls.csv")
x_train = np.ones((len(my_data), 2))
x_train[:, 0] = my_data.x1
x_train[:, 1] = my_data.x2
y_train = my_data.label
from sklearn.svm import SVC

# In[5]
# clf = make_pipeline(StandardScaler(), SVC(gamma="auto"))
clf = SVC(gamma="auto")
clf.fit(x_train, y_train)

# %%
print(clf.score(x_train[2:], y_train[2:]))
print(clf.predict([[-0.9, 1]]))

# %%
plt.plot(clf.support_vectors_)
plt.show()

# %%
