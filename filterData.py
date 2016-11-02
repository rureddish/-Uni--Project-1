# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:06:19 2016
BACTERIA-PROJECT FILTER DATA FUNCTION
@author: Jacob
"""

import numpy as np

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
    
#Test Zone
"""
test = np.array([ [40,0.5,1],[30,0.4,2],[59,0.1,3],[12,0.9,4],[35,0.6,2] ])
print(test)

test = filterData(test,"All",0,100)
print(test)
"""