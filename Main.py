# Student: Ulada Haranina
# StudentID: 011020337


import fileHandler.getInput;
import dataStructures.packagesHashTable;
import dataStructures.distanceGraph;
import dataStructures.Truck;
import datetime
import re


#
def main():

    #Define a new HashTable
    newTable = dataStructures.packagesHashTable.HashTable(40)

    #Add data from Excel to the package and to created Table
    fileHandler.getInput.insertData(newTable, "package")


    #Create a new graph and insert addresses and distance
    newGraph = dataStructures.distanceGraph.distanceGraph(27)
    fileHandler.getInput.insertData(newGraph, "addresses")
    fileHandler.getInput.insertData(newGraph, "distance")


    # Start loading track and add time
    globalTime = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=8));
    delayedTime = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=9, minute=5))

    #Lists for first load
    firstTruckLoad = []
    secondTruckLoad = []

    #Determine what packages should be delivered first
    priorityPackages = [pack for bucket in newTable.table for pack in bucket if pack.deadline !="EOD" or pack.packageId == 19]
    eodPackages = [pack for bucket in newTable.table for pack in bucket if pack.deadline == "EOD" and pack not in firstTruckLoad]

    
    def loadToTruck():

        #Get time first
        if(globalTime < delayedTime):
            #Upload only packages that have not been delayed

             #truck is first
                        for package in priorityPackages:
                            if(len(firstTruckLoad) < 16):
                                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) or package.packageId == 19:
                                    firstTruckLoad.append(package)
                        for package in eodPackages:
                            if(len(firstTruckLoad) < 16):
                                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and not re.search(r"2", str(package.notes), re.IGNORECASE):
                                    firstTruckLoad.append(package)        
                        
                
    loadToTruck();
  
    #TEST
    for package in firstTruckLoad:
        print(f"Packages in first truck {package.packageId}")

            #TEST
    for package in secondTruckLoad:
        print(f"Packages in second truck {package.packageId}")

   # newTable.printTable()

    # Send first truch to first point
    #firstTruck = dataStructures.Truck(16, 18, 16, address, 0, shiftStart)



#launch App
main();


    
