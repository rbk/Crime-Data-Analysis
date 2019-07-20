import pandas

cols = [
    'year', 
    'state_name', 
    'population', 
    'homicide',
    'rape_revised',
    'robbery',
    'aggravated_assault',
    'burglary',
    'larceny',
    'motor_vehicle_theft'
]

# LIMIT SCOPE
cols = [
    'year', 
    'state_name', 
    'population', 
    'homicide',
]

raw_data = pandas.read_csv('../data/estimated_crimes.csv', usecols=cols)


# Get the totals for the year 2017
# The query expression below is evalutated python code.
# the reason for "state_name.isnull" is that in our CSV file
# the estimated totals for all states doesn't have a state name
totals_2017 = raw_data.query('year == 2017 and state_name.isnull()')

print(raw_data.info())
"""
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
"""

# Dictionary of dataframes. One frame for each crime
result = {}

crimes = [
    'homicide',
    'rape_revised',
    'robbery',
    'aggravated_assault',
    'burglary',
    'larceny',
    'motor_vehicle_theft',
]

# Get 2017 state data
# We use notnull because the state name is not null for states
data = raw_data.query('year == 2017 and state_name.notnull()')

# Ranked By Total Homicides
ranked_th = data.sort_values(by=['homicide'], ascending=False).head(10).reset_index()
del ranked_th['index']
print(ranked_th.head(10))


# Note: New York did make the top 10 in homicides
# even though they are in the top ten pop size.
# I assumed New York would have the most reported homicides.
# Maybe New York has the least reported Homicdes.
# Note: New York is not OCR certified so that mean not enough agencies are reporting
# New York should actually be excluded from conclusions based on this.
print(data.sort_values(by=['population'], ascending=False).head(10))

# Ranked By Total Homicides Relative to the Population Size




"""
      year      state_name  population  homicide
137   2017      California    39536653      1830
1034  2017           Texas    28304596      1412
252   2017         Florida    20984400      1057
367   2017        Illinois    12802023       997
919   2017    Pennsylvania    12805537       739
850   2017            Ohio    11658609       710
275   2017         Georgia    10429379       703
597   2017        Missouri     6113532       600
666   2017  North Carolina    10273419       591
459   2017       Louisiana     4684333       582
"""