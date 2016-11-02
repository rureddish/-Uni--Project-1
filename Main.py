#TODO What are the standard values for upper and Lower
#TODO filtered data variable
#TODO inheritance for data variables for 3 and 4
#TODO Put functions in official files
#TODO Remember to import 3 main functions in all 3 files
#TODO Integrate Bilal's check

import numpy as np
import matplotlib.pyplot as plt
import math
from dataPlot import dataPlot
from displayMenu import displayMenu
from displayStatistics import displayStatistics
from filterData import filterData
from dataLoad import dataLoad

def main():
    bacteria = "All"
    upperBound = 30
    lowerBound = 1
    data = []
    dataLoaded = 0
    dataFiltered = 0

    userInput = "."

    while (userInput != "5"):

        displayMenu(bacteria, lowerBound, upperBound, dataLoaded)

        userInput = input("What do you want to do? : ")

        print("#######################\n")

        if userInput == "3" and dataLoaded == 0:

            print("!! Data is not loaded and you cannot Generate plots or Display statistics !!\n")

        if userInput == "4"  and dataLoaded == 0:

            print("!! Data is not loaded and you cannot Generate plots or Display statistics !!\n")

        ########## Load Data #####################################################

        if userInput == "1":

            dataLoaded = 1

            filename = input("Enter file name: ")

            data = dataLoad(filename)

            filteredData = filterData(data, bacteria, lowerBound, upperBound)

        ########## Filter Data #####################################################

        elif userInput == "2":

            print ("""Bacteria options: 1 Salmonella enterica
                2 Bacillus cereus
                3 Listeria
                4 Brochothrix thermosphacta""")

            bacteria = input("Bacteria: ")

            while True:
                try:
                    upperBound = float(input("Maximum growth rate: "))
                except ValueError:
                    print("That is not a float number!")
                else:
                    break

            while True:
                try:
                    lowerBound = float(input("Minimum growth rate: "))
                except ValueError:
                    print("That is not a float number!")
                else:
                    break

            filteredData = filterData(data, bacteria, lowerBound, upperBound)
            print("Data has been filtered!")
            dataFiltered = 1

        ########## Data Statistics #####################################################

        elif userInput == "3" and dataLoaded == 1:

            print("""Statistics options:
            ’Mean Temperature’ Mean (average) Temperature.
            ’Mean Growth rate’ Mean (average) Growth rate.
            ’Std Temperature’ Standard deviation of Temperature.
            ’Std Growth rate’ Standard deviation of Growth rate.
            ’Rows’ The total number of rows in the data.
            ’Mean Cold Growth rate’ Mean (average) Growth rate when Temperature is less than 20 degrees.
            ’Mean Hot Growth rate’ Mean (average) Growth rate when Temperature is greater than 50 degrees""")

            while True:

                statistic = input("Which statistic do you want to show: ")

                if statistic in ['Mean Temperature','Mean Growth rate','Std Growth rate','Rows','Mean Cold Growth rate','Std Temperature','Mean Hot Growth rate'] :
                    displayStatistics(data, statistic, bacteria, lowerBound, upperBound, filteredData)
                    break
                else:
                    print("This is not an option. Try again")


        ########## Data Plot #####################################################

        elif userInput == "4" and dataLoaded == 1:

            dataPlot(data)

        else:
            if userInput == "3" and dataLoaded == 0:
                pass

            elif userInput == "4" and dataLoaded == 0:
                pass

            else:
                print("You must select one of the options above. Try again\n")

        print("#######################\n")

        ###############################################################


main()