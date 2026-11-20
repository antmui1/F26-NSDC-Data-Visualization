from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)
#filtering
data = data.dropna(subset=["comp_upsec_v2_m"])
fltr = data[(data["iso_code"] == "COD") & (data["category"] == "Location") & (data["year"] == 2007)]
#x fliters
fltro = fltr[(fltr["location"] == "Urban")]
fltrt = fltr[(fltr["location"] == "Rural")]
#y filters
fltryo = fltro["comp_upsec_v2_m"].item() * 100
fltryt = fltrt["comp_upsec_v2_m"].item() * 100

#plotting
x = ["Urban", "Rural"]
y = [fltryo, fltryt]
plt.bar(x, y)
plt.xlabel("Location")
plt.ylabel("Upper-secondary school completion rate (%)")
plt.title("Upper-secondary completion by location, Dominican Republic of the Congo, 2007")
plt.ylim(0, 100)
plt.show()