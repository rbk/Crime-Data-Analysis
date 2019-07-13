import pandas

# Which columns to use
columns = ['year', 'state_name', 'population', 'violent_crime', 'property_crime']

# Get the data into a dataframe from csv
data = pandas.read_csv('estimated_crimes.csv', usecols=columns)

# print(data.head())

# Keep rows with latest year (2017)
# Pandas Dataframe - <class 'pandas.core.frame.DataFrame'>
data = data.query('year == 2017')

# Remove rows where state doesn't have a name
# data = data.dropna() # or next line
data = data[data['state_name'].notnull()]

# Define function to compute per captia crimes
# Base 1000
def crime_per_capita(row, arg):
    total_crimes = row['violent_crime'] + row['property_crime']
    population = row['population']
    count = (total_crimes/population)*arg
    return count

# Create row and apply computation function
# Number of crimes (violent and property) per XXX people per year
data['crime_per_1000'] = data.apply(crime_per_capita, args=(1000,), axis=1)

# Get National Average
total_population = data['population'].sum()
total_crimes =+ data['violent_crime'].sum() + data['property_crime'].sum()
national_average_per_cap = (total_crimes/total_population)*1000

# add column of diff to national average
def compute_diff(row):
    diff = row['crime_per_1000'] - national_average_per_cap
    return diff

data['diff_of_national_average'] = data.apply(compute_diff, axis=1)

# TODO add column of percent diff compared to national average
def compute_percent(row):
    percent = (row['crime_per_1000']/national_average_per_cap)*100
    # return str(int(percent)) + "%"
    if percent > 100:
        return "+" + str(int(percent-100)) + "%"
    return "-" + str(100 - int(percent)) + "%"

data['percent_diff_national'] = data.apply(compute_percent, axis=1)
"""
    Vermont has least number of crimes per person in 2017.
    (or at least lowest number of reported crimes were collected)
"""

"""
District of Columbia has worst crime rate.
Could it be attributed to the number of reported crime is higher?
Could it be that the area of DC is so much smaller that surrounding cities
crimes are swallowed up in DC?
There are just more bad people there?
"""

print("National Crime Rate Average Per Capita(1000): ", national_average_per_cap)
data = data.drop(['population', 'violent_crime', 'property_crime'], axis=1)
print(data.head(200))