## Bar Chart: School Completion by Wealth

How does upper-secondary school completion differ across wealth groups in a country of your choice?

- Filter to your chosen `country` and `category == "Wealth"`.
- Choose one `year` and one `survey` with completion data for all five wealth quintiles.
- Use `wealth` for the x-axis and `comp_upsec_v2_m` for the y-axis.
- Order the bars from Quintile 1 (poorest) to Quintile 5 (richest).
- Compare the groups. Does completion increase consistently with wealth?

## Line Plot: Youth Literacy Over Time

How has youth literacy changed over time in a country of your choice?

- Filter to your chosen `country` and `category == "Total"`.
- Choose a country with youth literacy data for at least three different years.
- Use `year` for the x-axis and `literacy_1524_m` for the y-axis. This indicator measures literacy among people ages 15–24.
- Remove rows missing either variable.
- Sort by `year` before plotting, and add markers to show the actual observations.
- Check for multiple surveys in the same year. Choose one observation per year and explain your selection.
- Display literacy rates as percentages.
- Identify the survey sources in a caption. Differences between sources may affect comparisons over time.
- Describe the pattern: has youth literacy increased, decreased, or remained relatively stable?

## For Every Chart

- Remove rows missing the variables needed for your chart using `.dropna(subset=[...])`.
- Display completion rates as percentages. The CSV stores them as proportions, so multiply by 100 if your axis runs from 0 to 100.
- Include a descriptive title identifying the country or countries and year or years, axis labels, and a legend when needed.