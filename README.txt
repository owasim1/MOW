The most recently updated file that we are using for analysis currently is: mow-data-final-ageadded.csv

NOTE: We used so many different files instead of appending data to one file to express the steps we took with further clarity.

FILES:
mow-data.csv -- the raw data
mow-data-clean.csv -- the final cleaned list of current Meals on Wheels clients
mow-data-current.csv -- uncleaned list of the currect Meals On Wheels clients
mow-data-terminated.csv -- uncleaned list of terminated clients
mow-data-povlevel-filled.csv -- cleaned list, with povlevel filled in
mow-data-final.csv -- the final, cleaned data we are using
mow-data-final-ageadded.csv -- the final data with each persons age added in

data-splitter.py -- splits single data file into two separate files, based on whether the person has been terminated from the program or not.
date-changer.py -- removes invalid dates and change the year of dates from a two digit number to a four digit number(2 digit to 4 digit feature not yet implemented).
pov-changer.py -- goes through povlevel column only and fills null spaces with "0%" and replaces "ABOVE" with "1000%"
city-checker.py -- reads through list of cities and prints out all the unique names so that user can look through and find similarities
city-changer.py -- custom file to replace targeted mistakes
age-calculate.py -- calculates a persons age as of 4/20/2017 from birthdate and sticks it in a new column

NOTE: we reverted the change from ABOVE to 1000% in mow-data-final.csv manually. It is now changed back to reading ABOVE.