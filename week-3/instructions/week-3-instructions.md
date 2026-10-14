# Week 3

The main goals of Week 3 are to ensure that everything is configured correctly. This is the main goal of this week. This might also be a shorter meeting. The meeting is to ensure that everyone generally understands what they're doing in a repo, and the 1-1 is time to ensure that everyone is able to make PRs. Admittedly, if you have any experience with Git and GitHub and VSCode, this is probably review, but also, there's always gaps in knowledge. I don't even fully understand Git sometimes. So it's helpful to know.

## Goals

By the end of this week, you should be able to:

- have Python, Git, GitHub, and VSCode installed and configured
- be able to run Python scripts
- be able to develop in a repo 
- be able to make PRs
- be able to get data in a CSV into a DataFrame
- (supplemental) understand other types of data storage/use cases

## Resources

Feel free to use these whenever you see fit. Being able to utilize documention/the internet to your coding benefit is important.
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Numpy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/index.html)
- [Seaborn documentation](https://seaborn.pydata.org/)
- [Scikit-learn documentation](https://scikit-learn.org/stable/index.html)
- [StackOverflow](https://stackoverflow.com/questions)

## For People Reading This

This is a Markdown file. Markdown is like a text file except you can do a little more stuff in making your text slightly more aesthetic. When we do writeups of our development/making PR descriptions/making issues, we typically write a little something in Markdown. It's relatively intuitive, if there's any questions about how to write in Markdown, you can google it, but primarily, if you're reading this and see the raw Markdown, you can press Ctrl+K and then V to open a split screen preview of this. 

## Installing Necessary Packages

We have a file in this repo called `requirements.txt`. Python has a set of functionalities, but you get the most of Python from using libraries. When imported, these allow you to use a variety of functions that vastly, vastly increase your capabilities to code. 

In the bottom right hand corner, press the button that has an X and a warning sign. This will open up your bottom bar with problems. Press Terminal, and then enter:
```{bash}
pip install -r requirements.txt
```

This should install a bunch of different libraries that will be used in this project. Generally, if you're installing libraries, you will use something called pip, which is very convenient, but sometimes it's not as convenient. In that case, you sometimes need to download libraries separately. For the sake of this project, the libraries we may be using are all accessible by running the above command.

## Checking That Your Python Works

On the explorer on the left of your screen, open up `week-3/instructions/week-3-test-code.py`, and press the sideways triangles in the upper right corner of your code window. This should run the Python file and, assuming everything is configured correctly, should print out your Python version, your Python filepath, and all the packages you have installed.

Alternatively, open your terminal and run:

```{bash}
& python week-3\instructions\week-3-test-code.py
```
and assuming your terminal in in the repo folder, it should work.

## Importing Data

This section is about importing data into your Python in a way that you're able to modify and actually do stuff with it. 

I think I should cover the question as to why we're doing this in Python. Why not Google Sheets or Excel, where I personally started doing data science? Why not Tableau, a very, very useful tool for data analysis and visualization? Why not R, a language dedicated to data science? And to be honest, I don't really have a great answer to that. I just feel like the earlier you can learn how to code, the quicker you can sharpen your technical skills, and thus, the more you can advance your data science skills. At some point, Sheets/Excel is too limited for you to do data science at your fullest potential, so you will need to learn how to code. So why not do it now?

Why not R? That's actually a good question. This is partially due to the fact that I barely know R and also, would not feel comfortable enough teaching it. But an actual realistic answer is that Python is versatile enough of a language and beginner friendly enough that you can do other things besides data science if you know Python. Not saying don't learn R. Definitely learn R. But be able to do other things.

Right now, we have a dataset in the repo in `data\week-3\Inequality in Education.csv`. This is saved as a Comma-Separated Values (CSV). I'll get more into file types in the supplemental (whenever I make it), but for right now, we're using a CSV because it's easy enough to both see and modify. You can also open a CSV in Google Sheets/Excel.

To import this data, add this to your code:

```{python}
data = pd.read_csv("data/week-3/Inequality in Education.csv")
```

This saves the data from the CSV into the DataFrame `data`. A dataframe is a type of data structure that's especially good for messing around with.

To see your dataframe, add this to your code:
```{python}
print(data)
```

or you can use this for seeing the first n rows:

```{python}
data.head(n)
```

## Data Exploration

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

## Action Items:
- Everyone:
  - Please write some code (I literally do not care how simple or complicated the code is.) and put it in your Python file. Make sure to save it.
    - Due: before your 1-1
  - If you don't have a 1-1 time finalized with me, please ensure that we get that finalized with a location
    - Due: ASAP
  - If you don't have VSCode, Python, Git, and GitHub configured, please get that configured.
    - Due: ASAP
  - If you're interested in learning more, check out the supplemental materials for week 3 (releasing sometime soon)
    - Due: Whenever you like
- Anthony:
  - Finish Week 3 Supplementals
    - Due: ASAP
  - Make Week 4 Materials
    - Due: By next week