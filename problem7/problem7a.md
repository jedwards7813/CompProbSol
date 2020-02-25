# Problem 7a "Using pandas"
## Outcomes
- Familiarize yourself with the `pandas` module 
- Manipulate several dataframes in Python

## Problem 

Recall that in Problem 4b, you saved a table containing 
- year
- `fossil fuel and industry` emissions
- `land-use change emissions`
- the cumulative sum of carbon emissions
- the average global temperature
- the lower and upper bounds of the 95% confidence interval of the combined effects

in `climate.txt` (and `climate.mat`, but we won't be using that one today). In this problem, I would like you to use `pandas` to import the data in `climate.txt` and add a new column containing the amount of carbon added every year. Use this to determine:
1. The hottest 10 years
1. The 10 years with the most carbon emitted
1. The relationship between these two sets of years (if there is any - don't need to get too technical with this)

In addition, I would like you to import `GlobalTempbyMonth.txt` and list the top 20 hottest months and check if there is overlap with any of the hottest years (DO NOT do this manually, write code to check this).

Finally, write the data in `climate.txt` to an excel sheet called `climate`, the data in `GlobalTempbyMonth.txt` to a sheet called `Monthly Temps`, and a list of years sorted by global average temperature, highest to lowest in a sheet called `records`. Write these three sheets to an excel file called 'climate.xlsx'
**Each task should be written as a generalized python function in a `.py` file. You should then use a Jupyter notebook to execute the code.**
