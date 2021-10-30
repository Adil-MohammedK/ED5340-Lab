import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# In[1]:
my_data = pd.read_csv("k_means_data.csv")
X = np.ones((len(my_data), 2))
X[:, 0] = my_data.x1
X[:, 1] = my_data.x2

plt.scatter(X[:, 0], X[:, 1])
plt.show()


def cluster_variance(n):
    variances = []
    kmeans = []
    outputs = []
    K = [i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        variance = 0
        model = KMeans(n_clusters=i, verbose=2).fit(X)
        kmeans.append(model)
        variances.append(model.inertia_)

    return variances, K, n


variances, K, n = cluster_variance(10)
plt.plot(K, variances)
plt.ylabel("Inertia ( Total Distance )")
plt.xlabel("K Value")
plt.xticks([i for i in range(1, n + 1)])
plt.show()

# Here we can see from graph that the elbow is at K=4.
# So we can use K=4 for our model. and 4 clusters.

# In[3]:
