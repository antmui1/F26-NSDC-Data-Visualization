from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


# To read a file from a CSV, you use pd.read_csv() and then in the parentheses, you put the file path in quotes. This CSV is a bit weird, so I've added some extra stuff so the CSV loads correctly.

data = pd.read_csv("data/week-5/1779962350-wide_2026_apr_v2.csv", encoding="latin-1", low_memory=False)

# 1. Get to know the data. Try using data.head(), data.shape(), data.columns, and data.describe to get a sense of what's actually in this data.

# Write code here:

print(data.shape)
print(data.head(5))
print(data.columns)
print(data.describe())

# Based on what you can gather from these functions and from skimming the PDF metadata, what actually is this data? What does one row mean?

# Answer here: 

# 2. Filter rows and select columns.
# You can select a specific column by doing data["column_name"].

print(data["country"])

# You can select multiple columns by doing data[["column_1", "column_2", "column_3"]]

print(data[["country", "year", "income_group"]])

# You can filter the data by doing data[data["country"] == "Zambia"] or data[data["year"] > 2023]

print(data[data["country"] == "Zambia"])
print(data[data["year"] > 2023])

# You can do a combination of these by filtering, and then selecting the ideal columns: data[data["country"] == "Zambia"][["year", "primary_completion"]] will filter the data to only rows with Zambia and then only select the year and primary_completion columns.

print(data[data["country"] == "Zambia"][["year", "comp_prim_v2_m"]])

# Try it out: Print out only the country and year columns in data.

# Write code here:

print(data[["country", "year"]])

# print(data[["country", "year"]])

# Print out only rows where the country is "Malawi"

# Write code here:

print(data[data["country"] == "Malawi"])

# Print out rows where the primary completion rate is > .6 and the year is in the last 3 years

# Write code here:

print(data[(data["comp_prim_v2_m"] > 0.6) & (data["year"] > 2020)])


# 3. Your first visualization

# Firstly, save the the primary completion pct column as a variable called primary_completion_rate.
# Then, save the lower secondary completion pct column as a variable called secondary_lower_completion rate

# Write code here:

primary_completion_rate = data["comp_prim_v2_m"]
secondary_lower_completion_rate = data["comp_lowsec_v2_m"]



# Each dot represents one national survey record. A country can appear in
# multiple years, so the dots are not a set of unique countries.

# Then, remove the hashtags in the code below:


plt.figure(figsize=(8, 6))
plt.scatter(
    primary_completion_rate,
    secondary_lower_completion_rate,
    alpha=0.7,
 )
plt.xlabel("Primary school completion (%)")
plt.ylabel("Lower secondary school completion (%)")
plt.title(
    "Primary and lower secondary school completion\n"
    f"DHS national survey records"
 )
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# Run the file, and congrats! You've made your first visualization.

