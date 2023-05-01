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
    time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=8));
    delayedTime = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=9, minute=5))

    hub = str(newGraph.vertices[0]);

    #Lists for first load
    firstTruckLoad = []
    secondTruckLoad = []

    #Determine what packages should be delivered first
    priorityPackages = [pack for bucket in newTable.table for pack in bucket if pack.deadline !="EOD" or pack.packageId == 19]
    eodPackages = [pack for bucket in newTable.table for pack in bucket if pack.deadline == "EOD" and pack not in firstTruckLoad and pack.packageId != 19]

    #Determine which packages will go to truck
    def initialLoad():

        #Upload only packages that have not been delayed
        for package in priorityPackages:
            if(len(firstTruckLoad) < 16):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE):
                    firstTruckLoad.append(package)

        for package in eodPackages:
                          
            if(len(firstTruckLoad) < 16):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and not re.search(r"2", str(package.notes), re.IGNORECASE):
                    firstTruckLoad.append(package)
                          
            elif(len(secondTruckLoad) < 16):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and package.packageId != 9:
                    secondTruckLoad.append(package)

    initialLoad()

    #  Load trucks with selected packages
    firstTruck = dataStructures.Truck.Truck(16, 18, firstTruckLoad, hub, 0, time)
    secondTruck = dataStructures.Truck.Truck(16, 18, secondTruckLoad, hub, 0, time)

    #Start route (nearest neighbor)
    def createRoute(truck):

        #Start route
        startPoint = "4001 South 700 East"
        destination = ""
        minimalDistance = 140

        listOfVertexes = newGraph.convertToString()
        indexOfStartPoint = newGraph.getIndexOfVertex(startPoint)

        #Get all addresses from packages
        for packages in firstTruck.packages:
            for vertics in listOfVertexes:
                # get distance from all of them compared with first distination
                if(packages.address == vertics):
                    secondIndex = newGraph.getIndexOfVertex(packages.address)
                    distance = newGraph.get_distanceOfVertexes(indexOfStartPoint, secondIndex)
                    #print(f"The distance between {startPoint} and {packages.address} is {distance}")
                    if(distance < minimalDistance):
                        minimalDistance = distance
                        destination = packages.address
                        #print(f" Current point {startPoint} -  Destination: {packages.address} that is {distance} miles away")
                        #Deliver a package

        print(f"From {startPoint} to {destination} in {minimalDistance} miles")
        
    createRoute(firstTruck)

#launch App
main();


    
