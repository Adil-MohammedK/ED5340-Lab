import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

my_data = pd.read_csv("Logistic_regression_ls.csv")
X = np.ones((len(my_data), 2))
X[:, 0] = my_data.x1
X[:, 1] = my_data.x2
pca = PCA(n_components=2)
pca.fit(X)

print(pca.explained_variance_ratio_)
print(pca.singular_values_)

# SVD full solver
pca = PCA(n_components=2, svd_solver="full")
pca.fit(X)

print(pca.explained_variance_ratio_)
print(pca.singular_values_)

# SVD arpack solver
pca = PCA(n_components=1, svd_solver="arpack")
pca.fit(X)

print(pca.explained_variance_ratio_)
print(pca.singular_values_)
