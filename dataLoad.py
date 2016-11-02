import numpy as np

def dataLoad(filename):
    # Load Data functionality
    # Loads the data from the space-separated data-file into a string and splits the string to an array
    # which is reshaped into a matrix with N rows. If the size of the array is not divisible by the amount
    # of columns the function prints and error message and returns 0.
    filein = open(filename, "r")
    lines = filein.readlines()
    text = "".join(lines)

    columns = 3  # Assign number of columns in data set
    rawData = text.split()

    for i in range(np.size(rawData)):  # CONVERT IDIVIDUAL STRINGS INTO FLOATS FOR ALL ELEMENTS IN RAWDATA
        rawData[i] = round(float(rawData[i]), 2)

    if ((np.size(rawData) % columns) == 0):
        rows = (np.size(rawData) / columns)  # Determine number of rows in data set
    else:
        print("Invalid data input")
        return
    rawData = np.reshape(rawData, [int(rows), columns])

    # Sort data and error handling functionality
    # After checking whether the raw data is correct by dataCtr, it is transfered to the data-matrix and
    # the raw data was invalid an error-message is printed.
    data = []
    data = np.reshape(data, [0, 3])
    for i in range(int(rows)):
        dataCtr = 111
        if ((float(rawData[i, 0]) < 10 or float(rawData[i, 0]) > 60)):
            dataCtr = dataCtr - 100
        if (float(rawData[i, 1]) < 0):
            dataCtr = dataCtr - 10
        if (rawData[i, 2] != 1 and rawData[i, 2] != 2 and rawData[i, 2] != 3 and rawData[i, 2] != 4):
            dataCtr = dataCtr - 1
        if (dataCtr == 111):
            data = np.vstack([data, rawData[i, :]])
        else:  # Switch-Case statement depending on dataCtr
            dict = {"11": "Invalid temperature in row {}".format(i), "101": "Invalid growth rate in row {}".format(i),
                    "110": "Invalid bacteria in row {}".format(i),
                    "1": "Temperature and Growth rate invalid in row {}".format(i),
                    "10": "Temperature and bacteria invalid in row {}".format(i),
                    "100": "Growth rate and bacteria invalid in row {}".format(i),
                    "0": "All data invalid in row {}".format(i)}
            dataCtr_string = str(dataCtr)
            print(dict[dataCtr_string])

    return data