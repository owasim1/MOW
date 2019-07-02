# Desc: Calculates a persons age as of 4/20/2017 and sticks it in a new column.
#       This code is tailored to only be used for the Meals on Wheels data and surely
#       would not work if used on a different dataset. This is because it picks
#       apart the string literals used in the original db.
#
# Written in Python 3.4
# Last updated: 4/20/2017

import csv

datafile = "mow-data-final.csv" # the input data
writefilename = "mow-data-final-ageadded.csv" # output filename

# Open read and write files and create csv reader and writer
readFile = open(datafile, 'r')
reader = csv.reader(readFile, delimiter=',')

writeFile = open(writefilename, 'w', newline='')
writer = csv.writer(writeFile, delimiter=',')

# Method that receives a month and returns true if it before April
def monthTester(x):
    return {
        'Jan': True,
        'Feb': True,
        'Mar': True,
    }.get(x, False)

# Loop through every row in csv, calculate age, add it to new column
header = True
for row in reader:
    if(not header):
        # Grabbing the birth year
        birthyear = 0  #default
        if(len(row[5]) == 9):
            birthyear = int(row[5][7:])
        elif(len(row[5]) == 8):
            birthyear = int(row[5][6:])
        
        # Grabbing the birth month
        birthmonth = "nil" #default
        if(len(row[5]) == 9):
            birthmonth = row[5][3:6]
        elif(len(row[5]) == 8):
            birthmonth = row[5][2:5]
        
        # Grabbing the birth day
        birthday = 0 #default
        if(len(row[5]) == 9):
            birthday = int(row[5][:2])
        elif(len(row[5]) == 8):
            birthday = int(row[5][:1])
            
        #check if before todays date
        beforeToday = False #default
        if(birthmonth == "Apr"):
            if(birthday < 20):
                beforeToday = True
        elif(monthTester(birthmonth)):
            beforeToday = True
            
        if(beforeToday):
            calculatedAge = 2017-(1900+birthyear)-1
        else:
            calculatedAge = 2017-(1900+birthyear)
            
        row.append(calculatedAge)
        writer.writerow(row)
        
    else:
        row.append('Age')
        header = False
        writer.writerow(row)

       

# Closing the files
readFile.close()
writeFile.close()

### END OF FILE
