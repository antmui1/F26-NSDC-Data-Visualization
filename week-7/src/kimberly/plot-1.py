from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

# Bar Chart: Rural vs. Urban School Completion
plot_data = data[(data["country"] == "Brazil") & (data["year"] == 2014) & (data["survey"] == "PNAD") & (data["category"] == "Location")]
plot_data = plot_data.dropna(subset=["location", "comp_upsec_v2_m"])

x = plot_data["location"]
y = plot_data["comp_upsec_v2_m"] * 100

plt.bar(x, y, color=["#2E7D32", "#F57C00"])
plt.xlabel("Location")
plt.ylabel("Upper-secondary completion rate (%)")
plt.title("Upper-Secondary School Completion by Location, Brazil, 2008")
plt.ylim(0, 100)

rates = plot_data.groupby("location")["comp_upsec_v2_m"].mean() * 100

print("Rural completion rate:", rates["Rural"], "%")
print("Urban completion rate:", rates["Urban"], "%")

gap = abs(rates["Urban"] - rates["Rural"])

print("Difference:", gap, "percentage points")

plt.show()

# Observation
# When comparing the two groups, I can see that the Urban group has the higher completion rate of over 60%. 
# In regards to the gap in percentage points, there's an approximate 20% difference between the two groups in Brazil's school completion rates.