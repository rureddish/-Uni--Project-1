# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:47:10 2016

@author: Jacob
"""

import numpy as np
import math

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
    
#TEST ZONE
#print(len(np.array([[0,2,3],[3,3,5],[4,3,4]])))