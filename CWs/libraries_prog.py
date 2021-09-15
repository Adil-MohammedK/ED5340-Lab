import pandas as pd
import numpy as np

# Read CSV file into DataFrame df
df = pd.read_csv("testdata.csv")

# Show dataframe
print(df)

# print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(id(arr), id(arr[0]))
print(type(arr))
print(arr.itemsize, arr.strides)

import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x ** 3

plt.plot(x, y, color="red")
plt.show()
