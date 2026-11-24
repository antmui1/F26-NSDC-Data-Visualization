from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

## Scatter Plot: Primary vs. Upper-Secondary Completion

#Do countries with higher primary completion rates also tend to have higher upper-secondary completion rates?

#- Filter to `year == 2022` and `category == "Total"`. Keep multiple countries for this comparison.
#- Use `comp_prim_v2_m` for the x-axis and `comp_upsec_v2_m` for the y-axis.
#- Check whether any country has multiple survey records. If so, select one survey per country and explain your choice.
#- Each dot should represent one country.
#- Optionally, color the dots using `income_group`.
#- Describe the relationship and identify any countries that stand out.

plot_data = data[(data["year"] == 2022) & (data["category"] == "Total")]

plot_data = plot_data.dropna(subset=["comp_prim_v2_m", "comp_upsec_v2_m"])

x = plot_data["comp_prim_v2_m"] * 100
y = plot_data["comp_upsec_v2_m"] * 100 

plt.scatter(x, y, label = "countries")
plt.xlabel("Primary Completion Rate")
plt.ylabel("Upper-Secondary Completion Rate")
plt.title("Scatter Plot: Primary vs. Upper-Secondary Completion")
plt.legend()
plt.show()