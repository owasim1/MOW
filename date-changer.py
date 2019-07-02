# Desc: File used to remove invalid dates and change the year of dates from a
#       two digit number to a four digit number.
#
# Written in Python 3.4
# Last updated: 2/25/2017

import csv

datafile = "mow-data.csv" # the raw data

# Open read files and create csv reader
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=",")

# Loop through every row in csv, perform needed actions
for row in reader:
    # Changing "00-Jan-00" to blank
    row.replace("00-Jan-00", "")

    # Changing dates to 4 digit format
    # Not yet implemented, may not need

# Closing the files
readFile.close()
### END OF FILE
