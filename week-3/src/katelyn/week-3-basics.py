import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/week-3/Inequality in Education.csv")
print(data)

data["Country"]

data[["Country", "ISO3"]]

data[data["HDI Rank (2021)"] <= 20]

data["HDI Rank (2021)"] = 12
data["new_modified_column"] = data["HDI Rank (2021)"] * 3 + 4

print("hello hello hello \nwhatup\nyo\nyo")
print("this is all ik how to do")
print("just print stuff")

print("this is how u run the thing according to google remember this unless there is a faster way but idk any other way:\npython week-3/src/katelyn/week-3-basics.py")