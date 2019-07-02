# Desc: Custom file to fix city mispelling
#
# Written in Python 3.4
# Last updated: 3/26/2017

import csv

datafile = "mow-data-povlevel-filled.csv" # the input data
writefilename = "mow-data-final.csv" # output filename

# Open read and write files and create csv reader and writer
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=',')

writeFile = open(writefilename, 'w', newline='')
writer = csv.writer(writeFile, delimiter=',')

# Loop through every row in csv, read and replace targeted string
for row in reader:
    if(row[2] == 'ST JOHN'):
        row[2] = 'ST. JOHN'
        writer.writerow(row)
    else:
        writer.writerow(row)


# Closing the files
readFile.close()
writeFile.close()

### END OF FILE
