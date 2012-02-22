import csv
from numpy import *
from pylab import *
#import pylab


datafile = open('rnaonly.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

    
data_arr = array(data)
year     = data_arr[1:,0]
yearly   = data_arr[1:,1]
yearlyfit = polyfit(year, yearly, 1)


#pylab.plot(year, yearly,'o')
plot(year, yearly,'o')
plot(year, yearlyfit,'b-')
#plot(year, yearly,'b-')
title('RNA Structures in PDB per Year')
xlabel('Year')
ylabel('Number of Yearly Added RNA Structures')


show()
