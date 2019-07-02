# Desc: Prints out list of all unique city names to check for error
#
# Written in Python 3.4
# Last updated: 3/20/2017

import csv

datafile = "mow-data-final.csv" # the input data
cities = []

# Open read files and create csv reader
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=',')

# Loop through every row in csv, check for unique city name, append if unique
for row in reader:
    if(row[2] not in cities):
        cities = cities + [row[2]]

# Closing the files
readFile.close()

print(cities)

### END OF FILE
