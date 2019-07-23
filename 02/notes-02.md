# Project Notes

## 02 Outline/Task
- [x] Objective - Data Exploration, Ask Questions
- [x] Preparing the data
- [x] Top 10 States Ranked By Homicides (Total)
- [x] Top 10 States Ranked By Homicides (Relative to Population Size)
- [ ] Describe the difference


## Data Exploration + Ask Questions
- Which state has the most violent crime relative to population?
    - Burglary?
    - Car theft?
- Top three states for each type of crime
- Relative to the national average

## NOTE: Important to normalize the data

- Your conclusions can have a serious bias based on population.
To avoid this bias you need to normalize the data


What percentage of each type of crime in each state?

1. Each crime, #1 state for each crime (NOT RELATIVE TO POPULATION)
1. Each crime, #1 state for each crime (!!! -> RELATIVE TO POPULATION)

## Example End Results: 

- CSV file example: Ranked NOT RELATIVE
    - state
    - rank
    - crime
    - percentage of total crimes for the year
    - number of this type of crimes 

    ```csv
    Oklahoma, #1, Rape, 30%, 1000
    Alaska, #1, Car Theft, 12%, 
    ```
- CSV: Relative ranked
    - state
    - rank
    - crime
    -
    - percentage of total relative to average


## How to calculate rank?

1. Non relative I could say
    - Most thefts in the US happen in California
    - New York Has the most robberies
    (this doesn take account of pop size)
2. Relative to size I could say
    - Most homicides per capital happen in New Orleans
    - California ranks #44 for homicides per capita

## Resources and Documentation

- **read_csv** - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- **Dataframe.query** - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html
