# Desc: File used to split single data file into two separate files, based
#       on whether the person has been terminated from the program or not.
#
# Written in Python 3.4
# Last updated: 2/26/2017

import csv

datafile = "mow-data.csv" # the raw data
fileCurrent = "mow-data-current.csv" # data of people still in the program
fileTerminated = "mow-data-terminated.csv" # data of people no longer in the program

# Open read and write files and create csv reader and writer
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=',')

writeFileCurrent = open(fileCurrent, 'w', newline='')
writeFileTerminated = open(fileTerminated, 'w', newline='')
writerCurr = csv.writer(writeFileCurrent, delimiter=',')
writerTerm = csv.writer(writeFileTerminated, delimiter=',')

# Loop through every row in csv, split depending on terminated null or not null
for row in reader:
    if(not row[10]):
        writerCurr.writerow(row)
    else:
        writerTerm.writerow(row)

# Closing the files
readFile.close()
writeFileCurrent.close()
writeFileTerminated.close()

### END OF FILE
