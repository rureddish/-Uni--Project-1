# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:39:03 2016

@author: Jacob
"""

import numpy as np
import matplotlib.pyplot as plt

def bubbleSortPlotData(xVals,yVals): #xVals and yVals must have the same length
    x_y = []    
    for i in range( len(xVals) ):
        x_y.append(xVals)
        x_y.append(yVals)
    
    #Bubble Sort functionality
    i = 0
    for i in range( len(xvals) - 1 ):
        k = 0
        for k in range( len(x_y) ):
            if( x_y[k] > x_y[ k+2 ] ):
                hold = x_y[ (k+2):(k+4) ]
                x_y[ (k+2):(k+4) ] = x_y[ k:(k+2) ]
                x_y[ k:(k+2) ] = hold
                k + 2
        
    
    return x_y

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
    
    plt.plot(bac1_T,bac1_Gr,"rp")
    plt.plot(bac2_T,bac2_Gr,"b-")
    plt.plot(bac3_T,bac3_Gr,"g-")
    plt.plot(bac4_T,bac4_Gr,"y-")
    plt.xlim(10,60)
    plt.ylim(0,1)
    plt.show()
    
    
    return
