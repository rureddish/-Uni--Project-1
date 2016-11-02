def displayMenu (bacteria, lowerBound, upperBound, dataLoaded):

    # Load
    if dataLoaded == 0:
        print("1.Load Data [NOT LOADED]")
    else:
        print("1.Load Data [LOADED]")



    # Filter

    print("2.Filter Data")
    print("[Active filters]")
    print("  Bacteria selected: ", "[", bacteria, "]")
    print("  Minimum growth rate: ", "[", lowerBound, "]")
    print("  maximum growth rate: ", "[" , upperBound, "]")

    #Statistics

    print("3.Display Statistics")

    # Graph

    print("4.Generate Plots")

    # Quit

    print("5.Quit")



