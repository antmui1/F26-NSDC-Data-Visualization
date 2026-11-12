## Bar Chart: School Completion by Wealth

How does upper-secondary school completion differ across wealth groups in a country of your choice?

- Filter to your chosen `country` and `category == "Wealth"`.
- Choose one `year` and one `survey` with completion data for all five wealth quintiles.
- Use `wealth` for the x-axis and `comp_upsec_v2_m` for the y-axis.
- Order the bars from Quintile 1 (poorest) to Quintile 5 (richest).
- Compare the groups. Does completion increase consistently with wealth?

## Scatter Plot: Primary vs. Upper-Secondary Completion

Do countries with higher primary completion rates also tend to have higher upper-secondary completion rates?

- Filter to `year == 2022` and `category == "Total"`. Keep multiple countries for this comparison.
- Use `comp_prim_v2_m` for the x-axis and `comp_upsec_v2_m` for the y-axis.
- Check whether any country has multiple survey records. If so, select one survey per country and explain your choice.
- Each dot should represent one country.
- Optionally, color the dots using `income_group`.
- Describe the relationship and identify any countries that stand out.

## For Every Chart

- Remove rows missing the variables needed for your chart using `.dropna(subset=[...])`.
- Display completion rates as percentages. The CSV stores them as proportions, so multiply by 100 if your axis runs from 0 to 100.
- Include a descriptive title identifying the country or countries and year or years, axis labels, and a legend when needed.