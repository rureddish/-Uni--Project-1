# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:37:21 2016

@author: Jacob
"""

import numpy as np
import math
from dataStatistics import dataStatistics

"""
def dataStatistics(data,statistic):
    
    result = 0 #Default
    if( statistic == "Mean temperature"):
        result = np.mean( data[:,0] )
    elif( statistic == "Mean Growth Rate"):
        result = np.mean( data[:,1] )
    elif( statistic == "Std Temperature"):
        result = math.sqrt( np.mean( data[:,0] - np.mean(data[:,0]) )**2 )
    elif( statistic == "Std Growth Rate"):
        result = math.sqrt( np.mean( data[:,1] - np.mean(data[:,1]) )**2 )
    elif( statistic == "Rows"):
        result = len(data) #Returns number of rows in a matrix!!!
    elif( statistic == "Mean Cold Growth Rate"):
        growthSum = 0
        count = 0
        for i in range( len(data) ):
            if( data[i,0] < 20):
                growthSum += data[i,1]
                count += 1
        result = growthSum / count        
    elif( statistic == "Mean Hot Growth Rate"):
        growthSum = 0
        count = 0
        for i in range( len(data) ):
            if( data[i,0] > 50):
                growthSum += data[i,1]
                count += 1
        result = growthSum / count 

    return result

def filterData(data,bacteria,lowerBound,upperBound):
    #Translate string bacteria-input to bacCtr variable
    bacCtr = 0    
    if( bacteria == "All"):
        bacCtr = 0    
    elif(bacteria == "Salmonella enterica" or bacteria == "1"):
        bacCtr = 1
    elif(bacteria == "Bacillus cereus" or bacteria == "2"):
        bacCtr = 2
    elif(bacteria == "Listeria" or bacteria == "3"):
        bacCtr = 3
    elif(bacteria == "Brochothrix thermosphacta" or bacteria == "4"):
        bacCtr = 4

    #If bacteria filter
    if( bacCtr != 0):    
        filteredData = []
        filteredData = np.reshape(filteredData,[0,3])
        for i in range( len(data)): #Test for bacteria and range conditions
            if(data[i,2] == bacCtr and ((data[i,1] > lowerBound) or (data[i,1] < upperBound)) ):
                filteredData = np.vstack([filteredData,data[i,:]])
    else: #No Bacteria Filter
        filteredData = []
        filteredData = np.reshape(filteredData,[0,3])
        for i in range( len(data)): #Test for range conditions
            if( (data[i,1] > lowerBound) and (data[i,1] < upperBound) ):
                filteredData = np.vstack([filteredData,data[i,:]])
 
    return filteredData
"""

def displayStatistics(data,statistic,bacteria,lowerBound,upperBound,filteredData):
    #I made this funcion inherit filteredData
    #fData = filterData(data,bacteria,lowerBound,upperBound) -- It conflicted with Main

    fData = filteredData

    if( statistic == "Mean temperature"):
        print("Mean Temperature is {}.".format(dataStatistics(fData,statistic) ) )
    elif( statistic == "Mean Growth Rate"):
        print("Mean Growth Rate is {}.".format(dataStatistics(fData,statistic) ) )
    elif( statistic == "Std Temperature"):
        print("Standard deviation of Temperature is {}.".format(dataStatistics(fData,statistic) ) )
    elif( statistic == "Std Growth Rate"):
        print("Standard deviation of Growth Rate is {}.".format(dataStatistics(fData,statistic) ) )
    elif( statistic == "Rows"):
        print("There are {} rows in the data.".format(dataStatistics(fData,statistic) ) ) 
    elif( statistic == "Mean Cold Growth Rate"):
        print("Mean Cold Growth Rate is {}.".format(dataStatistics(fData,statistic) ) )
    elif( statistic == "Mean  Hot Growth Rate"):
        print("Mean Hot Growth Rate is {}.".format(dataStatistics(fData,statistic) ) )

    return


#TestZone
"""
test = np.array([ [40,0.5,1],[30,0.4,2],[59,0.1,3],[12,0.9,4],[35,0.6,2] ])
print(test)

#test = filterData(test,"2",0,100)
#print(test)
print(dataStatistics(test,"Rows"))   
displayStatistics(test,"Std Temperature","All",0,100)
"""