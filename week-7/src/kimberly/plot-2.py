
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

# Line Plot: Youth Literacy Over Time
plot_data = data[(data["country"] == "Cambodia") & (data["category"] == "Total")]

plot_data = plot_data.dropna(subset=["year", "literacy_1524_m", "survey"])
plot_data = plot_data.sort_values("year")

print(plot_data[["year", "survey", "literacy_1524_m"]])

x = plot_data["year"]
y = plot_data["literacy_1524_m"] * 100

plt.plot(x, y, color="#214AA4", marker="o", label="Youth Literacy Measurement (Ages 15-24)")

plt.xlabel("Year")
plt.ylabel("Youth literacy rate (%)")
plt.title("Cambodia's Youth Literacy Rate Over Time")
plt.legend()

plt.figtext(0.5, 0.01, "Source: Demographic and Health Survey (DHS)", ha="center", fontsize=8)

plt.tight_layout()
plt.show()

# Observation
# When looking at Cambodia's youth literacy rate over time, I can see it's been steadily increasing from 2004 to 2021. 
# I can also see that the literacy rate has jumped from 78% in 2004 to 94% in 2021.