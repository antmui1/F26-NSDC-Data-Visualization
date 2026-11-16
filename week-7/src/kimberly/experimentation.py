from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

# How To Make A Scatter Plot:
# plot_data = data[(data["year"] == 2022) & (data["category"] == "Total")]
# The data["category"] == "Total" is so that we get whole country numbers, rather than just a demographic.

# plot_data = plot_data.dropna(subset=["comp_prim_v2_m", "comp_upsec_v2_m"])

# x = plot_data["comp_prim_v2_m"]
# y = plot_data["comp_upsec_v2_m"]

# plt.scatter(x, y, label = "Data")
# plt.xlabel("Primary school completion rate")
# plt.ylabel("Upper secondary school completion rate")
# plt.legend()
# plt.title("Primary vs upper-secondary school completion rate, 2022")
# plt.show()

# How To Make A Line Plot:
# plot_data = data[(data["country"] == "Afghanistan") & (data["category"] == "Total")]

# plot_data = plot_data.dropna(subset=["comp_prim_v2_m"])
# plot_data = plot_data.sort_values("year")

# x = plot_data["year"]
# y = plot_data["comp_prim_v2_m"]

# plt.plot(x, y, label = "Trend")
# plt.xlabel("Year")
# plt.ylabel("Primary school completion rate")
# plt.title("Afghanistan's overall primary school completion rate over time")
# plt.legend()
# plt.show()

# How To Make A Bar Chart:
# plot_data = data[(data["country"] == "Afghanistan") & (data["year"] == 2022) & (data["survey"] == "MICS") & (data["category"] == "Sex")]
# plot_data = plot_data.dropna(subset=["sex", "comp_prim_v2_m"])

# x = plot_data["sex"]
# y = plot_data["comp_prim_v2_m"] * 100

# plt.bar(x, y)
# plt.xlabel("Sex")
# plt.ylabel("Primary school completion rate (%)")
# plt.title("Primary School Completion by Sex, Afghanistan, 2022")
# plt.ylim(0, 100)
# plt.show()
