import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_csv("data2.csv")

# Show dataframe
print(df)

# Row wise
for x in df.iterrows():
    print(x)

# Column wise
# print(df.get(key="Marks"))
for x in df.get(key="Students"):
    print(x)
for x in df.get(key="Marks"):
    print(x)
