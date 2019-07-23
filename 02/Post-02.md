---
title: Crime Data Exploration with Python3 and Pandas: Part 2 
published: true
description: Analyzing the homcide rate for the United States 2017 UCR dataset
tags: data exploration, python, pandas
canonical_url: https://blog.richardkeller.net/crime-data-exploration-with-python3-and-pandas-part-2/
cover_image: https://s3.amazonaws.com/blog.richardkeller.net/posts/crime-data-analysis-01/crime-2.jpg
series: Pandas Crime
---

## Objective
The purpose of this post series is to explore datasets from the UCR (Uniforn Crime Reporting Program). In this post, we'll use Pandas to dig deeper into crime statistics for homicide. After preparing the dataset for comparison, we'll rank each state based on number of crimes per capita.

Follow along or checkout the code on [Github.](https://github.com/rbk/Crime-Data-Analysis)

## About the data
The dataset we are using is the `estimated_crimes.csv` downloaded from the <a href="https://crime-data-explorer.fr.cloud.gov/">Cime Data Explorer</a> website. This file contains the estimated crimes for 7 types of crimes, from the years 1995 to 2017, for the United States. For more information about this dataset and how it is compiled visit the <a href="https://crime-data-explorer.fr.cloud.gov/">Cime Data Explorer.</a>

## Preparing the data
For data manipulation we will use Pandas. The first thing we need to do is download the dataset and load it into a Pandas dataframe.

If you need the dataset you can download it here: [https://github.com/rbk/Crime-Data-Analysis](https://github.com/rbk/Crime-Data-Analysis)

In the following code, we use pandas to open the **estimated_crimes.csv** into a <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html">dataframe</a>. 

We specify the columns we want to work with by specifying the **usecols** attribute. This attribute tells the **read_csv** function to only load in the column with the headers that are in the cols array:

```python
import pandas

cols = [
    'year',
    'state_name',
    'population',
    'homicide',
]

raw_data = pandas.read_csv('../data/estimated_crimes.csv', usecols=cols)

print(raw_data.head())
```

### Output:

```
   year state_name  population  homicide
0  1995        NaN   262803276     21606
1  1996        NaN   265228572     19645
2  1997        NaN   267783607     18211
3  1998        NaN   270248003     16974
4  1999        NaN   272690813     15522
```

If you are curious on how to find out what the headers of your CSV are, use the **info** function:

```python
data = pandas.read_csv('../data/estimated_crimes.csv')
print(data.info())
```
### Output:

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
Now that we have our data loaded into a dataframe, we can start processing the data. The first thing we will do is rank the states by the number of homicides. 

This is a bad idea. Let's do it anyway to see why.

This is a very simple task. First, we query the dataframe by the year:

```python
# Get 2017 state data
# We use notnull because the state name is not null for states
data = raw_data.query('year == 2017 and state_name.notnull()')
```
Next we sort the data using **sort_values**.
Using the **by** attribute, we provide an array of columns to sort by. In this case we are sorting by the count of homicides.

```python
# Ranked By Total Homicides
ranked_by_total = data.sort_values(by=['homicide'], ascending=False)
ranked_by_total = ranked_by_total.reset_index()
del ranked_by_total['index']
print(ranked_by_total.head(10))
```

### Output:

```
   year      state_name  population  homicide
0  2017      California    39536653      1830
1  2017           Texas    28304596      1412
2  2017         Florida    20984400      1057
3  2017        Illinois    12802023       997
4  2017    Pennsylvania    12805537       739
5  2017            Ohio    11658609       710
6  2017         Georgia    10429379       703
7  2017        Missouri     6113532       600
8  2017  North Carolina    10273419       591
9  2017       Louisiana     4684333       582
```

The homicide column above is sorted by count.

From this simple sort we can say that California has the most homicides per year. Statistically this is true, but they also have the largest population of any state.

*Top 10 States By Population*
```
   year      state_name  population  homicide
0  2017      California    39536653      1830
0  2017           Texas    28304596      1412
0  2017         Florida    20984400      1057
0  2017        New York    19849399       548
0  2017    Pennsylvania    12805537       739
0  2017        Illinois    12802023       997
0  2017            Ohio    11658609       710
0  2017         Georgia    10429379       703
0  2017  North Carolina    10273419       591
0  2017        Michigan     9962311       569
```

Ranking the states in this way doesn't make sense because the number of homicides is not proportional to the number of people in the states.

From looking at the homicides ranked vs the populations, you can see that there is a strong correlation between the number of homicides and the population.

Next, we will rank the states by homicide rate.

## Top 10 States Ranked By Total Homicides Relative to the Population Size
Now we will rank the states in homcide by the population size. This will give us a clearer picture of the homcide rate, e.g. the number of homicides per 100,000 people.


First, we'll use Pandas **apply** function to create a new row.
The apply function takes the name of a function and "applies" the result of the function to each row. Our function is called **per_capital**. 

The per_capita function takes each row of data and performs a calculation to normalize data.

The result is that we have a column for each row with the number of homicides per 100,000 people.

```python
# Ranked By Total Homicides Relative to the Population Size
# Per 100,000 people
def per_capita(row):
    """Calculate the homcide rate per capita."""
    total_homicides = row['homicide']
    population = row['population']
    count = (total_homicides / population) * 100000
    return count

data['per_captia'] = data.apply(per_capita, axis=1)

# Ranked By Total Homicides
ranked_by_population = data.sort_values(by=['per_captia'], ascending=False)
ranked_by_population = ranked_by_population.reset_index()
del ranked_by_population['index']
print(ranked_by_population.head(50))
```

Finally, we print all the rows.

### Output:

```
    year            state_name  population  homicide  per_captia
0   2017  District of Columbia      693972       116   16.715372
1   2017             Louisiana     4684333       582   12.424394
2   2017              Missouri     6113532       600    9.814294
3   2017                Nevada     2998039       274    9.139307
4   2017              Maryland     6052177       546    9.021547
5   2017              Arkansas     3004279       258    8.587751
6   2017                Alaska      739795        62    8.380700
7   2017               Alabama     4874747       404    8.287610
8   2017           Mississippi     2984100       245    8.210181
9   2017             Tennessee     6715984       527    7.846951
10  2017              Illinois    12802023       997    7.787832
11  2017        South Carolina     5024369       390    7.762169
12  2017            New Mexico     2088070       148    7.087885
13  2017               Georgia    10429379       703    6.740574
14  2017              Oklahoma     3930864       242    6.156407
15  2017                  Ohio    11658609       710    6.089920
16  2017               Indiana     6666818       397    5.954865
17  2017               Arizona     7016270       416    5.929076
18  2017              Kentucky     4454189       263    5.904554
19  2017          Pennsylvania    12805537       739    5.770941
20  2017        North Carolina    10273419       591    5.752710
21  2017              Michigan     9962311       569    5.711526
22  2017              Delaware      961939        54    5.613662
23  2017                Kansas     2913123       160    5.492387
24  2017              Virginia     8470020       453    5.348275
25  2017               Florida    20984400      1057    5.037075
26  2017                 Texas    28304596      1412    4.988589
27  2017         West Virginia     1815857        85    4.680985
28  2017            California    39536653      1830    4.628616
29  2017              Colorado     5607154       221    3.941393
30  2017               Montana     1050493        41    3.902929
31  2017            New Jersey     9005644       324    3.597744
32  2017                  Iowa     3145711       104    3.306089
33  2017             Wisconsin     5795483       186    3.209396
34  2017            Washington     7405743       230    3.105698
35  2017          South Dakota      869666        25    2.874667
36  2017           Connecticut     3588184       102    2.842664
37  2017              New York    19849399       548    2.760789
38  2017                Hawaii     1427538        39    2.731976
39  2017               Wyoming      579315        15    2.589265
40  2017         Massachusetts     6859819       173    2.521932
41  2017                Oregon     4142776       104    2.510394
42  2017                  Utah     3101833        73    2.353447
43  2017               Vermont      623657        14    2.244824
44  2017              Nebraska     1920076        43    2.239495
45  2017             Minnesota     5576606       113    2.026322
46  2017          Rhode Island     1059639        20    1.887435
47  2017                 Idaho     1716943        32    1.863778
48  2017                 Maine     1335907        23    1.721677
49  2017          North Dakota      755393        10    1.323814
50  2017         New Hampshire     1342795        14    1.042601

```

## What can we infer from this analysis
The new column **per_capita**, gives us a more accurate description of the homicide rate per 100,000 people for each state. For example, we could say that for every 100,000 people in Louisiana, there are 2.4 homicides reported. 

Here are a few more conclusions we can draw from this analysis:

- The District of Columbia has the highest homicide rate, ranking #1 for the most homicides per capita (per 100,000 people).
- Although California has the largest population, the homicide rate ranks #29 in the country.
- New Hampshire has the lowest homicide rate.

## Conclusion

The lesson from this analysis is that sorting by count doesn't tell the full story about the data. California would be ranked #1 in homicides from the first analysis, but in reality, California has a lower homicide rate than 28 other states. This is a simple example of how data can be decieving.

To recap, we used Pandas **read_csv** to explore the Estimated Crime 2017 dataset. We ranked states by total homicides. Then we looked at the homicide rate, which gave of very different views of how the states rank in homicdes.

Thanks for reading!

### FBI Disclaimer
> "The data found on the Crime Data Explorer represents reported crime, and is not an exhaustive report of all crime that occurs. It’s important to consider the various factors that lead to crime activity and crime reporting in a community before interpreting the data. Without these considerations the available data can be deceiving. Factors to consider include population size and density, economic conditions, employment rates, prosecutorial, judicial, and correctional policies, administrative and investigative emphases of law enforcement, citizens’ attitudes toward crime and policing, and the effective strength of the police force."
>
> --- [Crime Data Explorer, Retrieved 19:45, July 22, 2019](https://crime-data-explorer.fr.cloud.gov/explorer/state/new-york/crime)

- [For more information on the use of the UCR database](https://ucr.fbi.gov/ucr-statistics-their-proper-use)
