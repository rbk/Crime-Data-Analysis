# notes.md

## 02 Outline/Task
- [x] Objective - Data Exploration, Ask Questions
- [x] Preparing the data
- [ ] States Ranked By Crime
- [ ] States Ranked By Crime (Relative to Population Size)
- [ ] Describe the difference

## 03 Outline/Task
- [ ] Objective - Visualize Data
- [ ] Recap Ranked States Differences
- [ ] Matplot overview
- [ ] Graph Top 5 for Each Crime
- [ ] Graph Top 5 for Each Crime (Relative to Population Size)



- Which state has the most violent crime relative to population?
    - Burglary?
    - Car theft?
- Top three states for each type of crime
- Relative to the national average

## Important to normalize the data

- Your conclusions can have a serious bias based on population.
To avoid this bias you need to normalize the data


What percentage of each type of crime in each state?

1. Each crime, #1 state for each crime (NOT RELATIVE TO POPULATION)
1. Each crime, #1 state for each crime (!!! -> RELATIVE TO POPULATION)

## Example End Result: 

CSV file

- state
- rank
- crime
- percentage of total
- number of type of cime
    
```
Oklahoma, #1, Rape, 30%, 1000
Alaska, #1, Car Theft, 12%, 
```

## How to calculate rank?




## Resources and Documentation

- **read_csv** - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- **Dataframe.query** - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html
