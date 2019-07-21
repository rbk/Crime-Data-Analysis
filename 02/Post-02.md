---
title: Crime Data Exploration with Python3 and Pandas: Part 2 
published: true
description: 
tags: data exploration, python, pandas
canonical_url: 
cover_image: 
series: Pandas Crime
---

<aside>
<h2>FBI Disclaimer</h2>
<blockquote>
    "The data found on the Crime Data Explorer represents reported crime, and is not an exhaustive report of all crime that occurs. It’s important to consider the various factors that lead to crime activity and crime reporting in a community before interpreting the data. Without these considerations the available data can be deceiving. Factors to consider include population size and density, economic conditions, employment rates, prosecutorial, judicial, and correctional policies, administrative and investigative emphases of law enforcement, citizens’ attitudes toward crime and policing, and the effective strength of the police force."
</blockquote>
- (Quote Source)[https://crime-data-explorer.fr.cloud.gov/explorer/state/new-york/crime]
- (For more information on the use of the UCR database)[https://ucr.fbi.gov/ucr-statistics-their-proper-use]
</aside>

```
-    year      state_name  population  homicide
-    2017      California    39536653      1830
-    2017           Texas    28304596      1412
-    2017         Florida    20984400      1057
x    2017        New York    19849399       548
-    2017    Pennsylvania    12805537       739
-    2017        Illinois    12802023       997
-    2017            Ohio    11658609       710
-    2017         Georgia    10429379       703
-    2017  North Carolina    10273419       591
-    2017        Michigan     9962311       569
```

**Part 2 in Crime Dataset Analysis Series***
In the last post from this series we learned useful Pandas functions to manipulate our dataset and calculated the overall crime rate  (relative to the national average) for each state in the United States. 

## Objective
The object of the post series is to explore the Uniform Crime Reporting (UCR) Program's datasets. In this post we'll use Pandas (a python package) to dig deeper into the crime statistic for homicide. We will prepare the dataset for comparison and rank each state based on number of crimes per capita.  

## About the data
The dataset we are using is the `estimated_crimes.csv`. This file contains the estimated crimes for 7 types of crime, from the years 1995 to 2017, for the United States. For more information about this dataset and how it is compiled visit the <a href="https://crime-data-explorer.fr.cloud.gov/">Cime Data Explorer.</a>

## Preparing the data
For data manipulation we will use Pandas. The first thing we need to do is download the dataset and load it into a Pandas dataframe.

**If you need the dataset you can download it here: https://github.com/rbk/Crime-Data-Analysis**

In the following code, we use pandas to open the `estimated_crimes.csv` into a <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html">dataframe</a>. 

We specify the columns we want to work with by specifying the `usecols` attribute. This attribute tells the read_csv function to only load in the column with the header that are in the usecols array.

```python
import pandas

cols = [
    'year',
    'state_name',
    'population',
    'homicide',
]

raw_data = pandas.read_csv('../data/estimated_crimes.csv', usecols=cols)
```

If you are curious on how to find out what the header of your CSV are, use the `info` function:

```python
data = pandas.read_csv('../data/estimated_crimes.csv')
print(data.info())
```
The result should look like this:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1196 entries, 0 to 1195
Data columns (total 16 columns):
year                   1196 non-null int64
state_id               1173 non-null float64
state_abbr             1173 non-null object
state_name             1173 non-null object
population             1196 non-null int64
violent_crime          1196 non-null int64
homicide               1196 non-null int64
rape_legacy            1196 non-null int64
rape_revised           260 non-null float64
robbery                1196 non-null int64
aggravated_assault     1196 non-null int64
property_crime         1196 non-null int64
burglary               1196 non-null int64
larceny                1196 non-null int64
motor_vehicle_theft    1196 non-null int64
caveats                71 non-null object
dtypes: float64(2), int64(11), object(3)

```

## Top 10 States Ranked By Total Homicides
## Top 10 States Ranked By Total Homicides Relative to the Population  Size
## What can we infer from this analysis
## Conclusion