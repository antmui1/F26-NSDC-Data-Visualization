import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/week-3/Inequality in Education.csv")
	
# For printing dataframe in full
# print(data)

# for printing the first n rows of the dataframe
# print(data.head(10))

# For printing only one column of the dataframe
# print(data["Country"])

# For printing a set of multiple columns of the dataframe
# print(data[["Country", "ISO3"]])

# For printing a filtered dataframe based on a condition
# data = data[data["HDI Rank (2021)"] <= 20]
# print(data)

# For printing a filtered dataframe based on multiple conditions
# data["HDI Rank (2021)"] = 12
# data["new_modified_column"] = data["HDI Rank (2021)"] * 3 + 4
# print(data)

# For creating a new column based on a boolean statement
data["flag"] = data["HDI Rank (2021)"] <= 20
print(data[["Country", "HDI Rank (2021)", "flag"]].head(20))
