# Desc: Fills in empty povlevel boxes and changes "ABOVE" to 1000%
#
# Written in Python 3.4
# Last updated: 3/15/2017

import csv

datafile = "mow-data-clean.csv" # the input data
writefilename = "mow-data-povlevel-filled.csv" # output filename

# Open read and write files and create csv reader and writer
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=',')

writeFile = open(writefilename, 'w', newline='')
writer = csv.writer(writeFile, delimiter=',')

# Loop through every row in csv, read and replace targeted strings in column 9, 'povlevel'
for row in reader:
    if(row[8] == ''):
        row[8] = '0%'
        writer.writerow(row)
    elif(row[8] == 'ABOVE'):
        row[8] = '1000%'
        writer.writerow(row)
    else:
        writer.writerow(row)


# Closing the files
readFile.close()
writeFile.close()

### END OF FILE
