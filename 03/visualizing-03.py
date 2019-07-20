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

raw_data = pandas.read_csv('../data/estimated_crimes.csv', usecols=cols)

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

# Pie Chart Crime by Category
for crime in crimes:
    print(crime, data[crime].sum())

