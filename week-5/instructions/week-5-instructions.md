# Week 5

The main goals of Week 5 are to actually be able to wrangle with the data and prepare the data for visualizations. 

## Goals

By the end of this week, you should be able to:

- do the development cycle of creating a branch, making commits, pushing the branch, making a PR, and then merging the PR
- ingest data as a CSV and turn it into a DataFrame
- do very basic DataFrame operations
- do basic EDA
- make your first ever visualization

## Resources

Feel free to use these whenever you see fit. Being able to utilize documention/the internet to your coding benefit is important.
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Numpy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/index.html)
- [Seaborn documentation](https://seaborn.pydata.org/)
- [Scikit-learn documentation](https://scikit-learn.org/stable/index.html)
- [StackOverflow](https://stackoverflow.com/questions)

## For People Reading This

Press Ctrl+K and then V to open a split screen preview of this Markdown file.

## Data Exploration Guide (from Week 3)

I think one of the benefits of coding in Python/a new language for the first time is exploring stuff. I'm not sure how long it's going to take me to run through this set of instructions during the meeting, and we're inevitably going to run into technical difficulties. So this is a section where I'm going to tell you about possible things you could do with your data, and some time before your 1-1, I want you to try some stuff out and save it in your Python file.

Let's say you want to see only one column of your data. You'd use:
```{python}
data["Country"]
```
to see only the column named "Country".

If you wanted to see a set of multiple columns, you'd use:
```{python}
data[["Country", "ISO3"]]
```
to see the columns "Country" and "ISO3". In general, if you have some dataframe and you want to see only one column, you'd use `data["column_name"]`, and if you wanted to see multiple columns, you'd use `data[["col_1", "col_2", "col_3"]]` to see col_1, col_2, and col_3.

This is great and all, but there's still ~200 rows in this, which is hard to look through. So what if you wanted to filter this dataset? You can.

```{python}
data[data["HDI Rank (2021)"] <= 20]
```

In particular, what this does is that it filters data to rows in which `data["HDI Rank (2021)"] <= 20`. 

What if you want to add/modify columns? You can.

```{python}
data["HDI Rank (2021)"] = 12
data["new_modified_column"] = data["HDI Rank (2021)"] * 3 + 4
```

This code segment sets all of the "HDI Rank (2021)" values to 12, and then it creates a new column of data called "new_modified_column" which takes the HDI Rank values, multiplies them by 3, and adds 4. So each value in "new_modified_column" should be 36.

Let's look back at `data["HDI Rank (2021)"] <= 20`. This is a boolean statement, so it either gives a true or a false. Let's say we then did:

```{python}
data["flag"] = data["HDI Rank (2021)"] <= 20
```
This creates a new column called "flag" and sets it equal to "True" if HDI Rank is <= 20 and "False" if not. 

These boolean statements can be as complicated or as simple as you'd like. Use `&` for the logical and operator, `|` for the logical or operator, `~` for the logical not operator, and `==` to check if two values are equal.

Feel free to explore more. We'll get into more specific and applicable coding next week, but for right now, feel free to explore using this guide and using the resources.

