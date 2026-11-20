from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)
fltr = data[(data["year"] == 2022) & (data["category"] == "Total")]
fltr = fltr.dropna(subset=["comp_prim_v2_m", "comp_upsec_v2_m"])
x = fltr["comp_prim_v2_m"] *100
y = fltr["comp_upsec_v2_m"] *100

plt.scatter(x, y, label = "Data")
plt.xlabel("Primary school completion rate (%)")
plt.ylabel("Upper secondary school completion rate (%)")
plt.legend()
plt.title("Primary vs upper-secondary school completion rate, 2022")
plt.show()