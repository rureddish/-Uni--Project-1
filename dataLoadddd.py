# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:03:39 2016

@author: Jacob
"""

#THE GREAT QUESTION IS IF THERE IS A BETTER WAY TO CONVERT STRINGS INTO FLOATS!
import numpy as np
import os
import math

def dataLoad(filename):
    
    #Load Data functionality
    #Loads the data from the space-separated data-file into a string and splits the string to an array 
    #which is reshaped into a matrix with N rows. If the size of the array is not divisible by the amount
    #of columns the function prints and error message and returns 0.
    filein = open(filename,"r")
    lines = filein.readlines()
    text = "".join(lines)

    columns = 3 #Assign number of columns in data set
    rawData = text.split()   
    
    for i in range( np.size(rawData) ): #CONVERT IDIVIDUAL STRINGS INTO FLOATS FOR ALL ELEMENTS IN RAWDATA 
        rawData[i] = round(float(rawData[i]),2)
        
    if( (np.size(rawData) % columns) == 0 ):
        rows = (np.size(rawData) / columns) #Determine number of rows in data set
    else:
        print("Invalid data input")
        return
    rawData = np.reshape(rawData,[ int(rows) , columns ])
    
    #Sort data and error handling functionality
    #After checking whether the raw data is correct by dataCtr, it is transfered to the data-matrix and
    #the raw data was invalid an error-message is printed.
    data = []
    data = np.reshape(data,[0,3])
    for i in range( int(rows) ):
        dataCtr = 111
        if( ( float(rawData[i,0]) < 10 or float(rawData[i,0]) > 60) ):
            dataCtr = dataCtr - 100
        if( float(rawData[i,1]) < 0 ):
            dataCtr = dataCtr - 10
        if( rawData[i,2] != 1 and rawData[i,2] != 2 and rawData[i,2] != 3 and rawData[i,2] != 4):
            dataCtr = dataCtr - 1
        if(dataCtr == 111):
            data = np.vstack( [ data,rawData[i, : ] ] )
        else: #Switch-Case statement depending on dataCtr
            dict = {"11":"Invalid temperature in row {}".format(i), "101":"Invalid growth rate in row {}".format(i),"110":"Invalid bacteria in row {}".format(i),"1":"Temperature and Growth rate invalid in row {}".format(i),"10":"Temperature and bacteria invalid in row {}".format(i),"100":"Growth rate and bacteria invalid in row {}".format(i),"0":"All data invalid in row {}".format(i)}
            dataCtr_string = str(dataCtr)
            print( dict[ dataCtr_string ] )
           
    return data

def dataStatistics(data,statistic):
    
    result = 0 #Default
    if( statistic == "Mean Temperature"):
        result = np.mean( data[:,0] )
    elif( statistic == "Mean Growth Rate"):
        result = np.mean( data[:,1] )
    elif( statistic == "Std Temperature"):
        result = math.sqrt( np.mean( (data[:,0] - np.mean(data[:,0]))**2 ) )
    elif( statistic == "Std Growth Rate"):
        result = math.sqrt( np.mean( (data[:,1] - np.mean(data[:,1]))**2 ) )
    elif( statistic == "Rows"):
        result = len(data) #Returns number of rows in a matrix!!!
    elif( statistic == "Mean Cold Growth Rate"):
        growthSum = 0
        count = 0
        for i in range( len(data) ):
            if( data[i,0] < 20):
                growthSum += data[i,1]
                count += 1
        if( count != 0):
            result = growthSum / count               
    elif( statistic == "Mean Hot Growth Rate"):
        growthSum = 0
        count = 0
        for i in range( len(data) ):
            if( data[i,0] > 50):
                growthSum += data[i,1]
                count += 1
        if(count != 0):
            result = growthSum / count 

    return result

#TEST ZONE
"""
d = dataLoad("test.txt")
a = np.array([ [1,2,3],[4,5,6],[5,4,7] ])
print( a )
print( d )
#print("This is a trial {} hello".format("test"))
print( dataStatistics(d, "Mean Hot Growth Rate") )
"""

import matplotlib.pyplot as plt

"""
def bubbleSortPlotData(xVals,yVals): #xVals and yVals must have the same length
    x_y = []    
    for i in range( len(xVals) ):
        x_y.append(xVals)
        x_y.append(yVals)
    
    #Bubble Sort functionality
    i = 0
    for i in range( len(xVals) - 1 ):
        k = 0
        for k in range( len(x_y)-4 ):
            if( x_y[k] > x_y[ k+2 ] ):
                hold = x_y[ (k+2):(k+4) ]
                x_y[ (k+2):(k+4) ] = x_y[ k:(k+2) ]
                x_y[ k:(k+2) ] = hold
                k + 2
        
    return x_y
"""


def dataPlot(data):
    #Histogram plot
    plt.hist( data[:,2] , bins=[1,2,3,4,5])
    plt.title("Bacteria Type Frequency")
    plt.ylim(0,30)
    plt.ylabel("Frequency")
    plt.xlabel("Bacteria Type")
    plt.show()    
    
        #Growth Rate by Temperature
    bac1_T = [] #Generate data containers
    bac2_T = []
    bac3_T = []
    bac4_T = []
    bac1_Gr = []
    bac2_Gr = []
    bac3_Gr = []
    bac4_Gr = []
    for i in range(len(data)):
        if( data[i,2] == 1):
            bac1_T.append( data[i,0] )
            bac1_Gr.append( data[i,1] )
        elif( data[i,2] == 2):
            bac2_T.append( data[i,0] )
            bac2_Gr.append( data[i,1] )
        elif( data[i,2] == 3):
            bac3_T.append( data[i,0] )
            bac3_Gr.append( data[i,1] )
        elif( data[i,2] == 4):
            bac4_T.append( data[i,0] )
            bac4_Gr.append( data[i,1] )
    
    print(bac1_T)
    print(bac1_Gr)
    
    plt.plot(bac1_T,bac1_Gr,"rp")
    plt.plot(bac2_T,bac2_Gr,"b-")
    plt.plot(bac3_T,bac3_Gr,"g-")
    plt.plot(bac4_T,bac4_Gr,"y-")
    plt.xlim(10,60)
    plt.ylim(0,1)
    plt.show()

    return
"""Experiment + bubbleSort   
    bac1 = bubbleSortPlotData(bac1_T,bac1_Gr)
    bac1t = []
    bac1gr = []
    for i in range(len(bac1) ):
        if( i % 2 == 0):
            bac1t = bac1[i]
        elif( i % 2 == 1):
            bac1gr = bac1[i]
   print(bac1t)
   print(bac1_T)"""    

"""
dataPlot(d)
"""