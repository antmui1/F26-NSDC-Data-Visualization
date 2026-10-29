import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("data/week-3/Inequality in Education.csv")
print(data[data["Inequality in Education (2020)"] <= 10].sort_values("Inequality in Education (2020)", ascending=False).head(10))   
data["Inequality in Education (2021)"] = 12
print(data)
data["new_modified_column"] = data["Inequality in Education (2021)"] * 3 + 4
print (data)
data["flag"] = data["Inequality in Education (2021)"] <= 20
print(data)