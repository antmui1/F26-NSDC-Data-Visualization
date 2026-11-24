from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

# Bar Chart: School Completion by Wealth

## - Filter to your chosen `country` and `category == "Wealth"`.
## - Choose one `year` and one `survey` with completion data for all five wealth quintiles.
## - Use `wealth` for the x-axis and `comp_upsec_v2_m` for the y-axis.
## - Order the bars from Quintile 1 (poorest) to Quintile 5 (richest).
## - Compare the groups. Does completion increase consistently with wealth?

print(data[data["category"] == "Wealth"].dropna(subset=["wealth", "comp_upsec_v2_m"]))

plot_data = data[(data["country"] == "Viet Nam") & (data["category"] == "Wealth") & (data["year"] == 2021) & (data["survey"] == "MICS")]

plot_data = plot_data.dropna(subset=["wealth", "comp_upsec_v2_m"])

x = plot_data["wealth"]
y = plot_data["comp_upsec_v2_m"] * 100

plt.bar(x, y) 
plt.xlabel("Wealth Quintile")
plt.ylabel("Completion Rate (%)")
plt.title("School Completion by Wealth Quintile in Viet Nam (2021, MICS Survey)")
plt.show()



print(data[data["category"] == "Wealth"].dropna(subset=["wealth", "comp_upsec_v2_m"]))