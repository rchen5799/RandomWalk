import random
#Note: to run this program, xlwt package has to be installed from pip
#import xlwt

#Creates the excel sheet
wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet 1')

#Number of coins flipped per trial; Can be changed
timesTossed = 10
#Number of Trials; Can be changed
Trial = 1000000

#This keeps track of how many times each value occurs. Don't change
dict = {-10: 0, -9: 0, -8: 0, -7: 0, -6: 0, -5: 0, -4: 0, -3: 0, -2: 0, -1: 0, 0: 0, 1: 0,
        2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

#Runs through the trials
for i in range(Trial):
    timesAcc = 0
    for j in range(timesTossed):
        add = random.choice([-1,1])
        timesAcc += add
    dict[timesAcc] = dict[timesAcc]+1

#Adding/Modifying the excel sheet
xCol = 0
y1 = 0
y2 = 1
for i in range(len(dict)):
    replace = -10+i
    sheet1.write(xCol, y1, replace)
    sheet1.write(xCol, y2, dict[replace])
    xCol += 1

#Will save the finished excel sheet (Named "RandomWalk.xls") onto the desktop; Can change the filename to be something else
wb.save('RandomWalk.xls')
