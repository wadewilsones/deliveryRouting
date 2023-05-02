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
    time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=8, minute = 0));
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

    def deliver(package, distance, startTime, speed, truck):

        additionalPackages = []

        #Set new time when truck will be at the address
        timeToGetToDestination = distance / speed
        deliveredTime = startTime + datetime.timedelta(hours=timeToGetToDestination)
        #Increase milage
        truck.milage = truck.milage + distance

        #Test is there any other package at the same address
        for pack in truck.packages:
            if(package.address == pack.address and package.packageId != pack.packageId):
                print(f"Matching {package.packageId} and {pack.packageId}")
                truck.packages.remove(pack)

        #Change package status
        package.status = f'Delivered at {deliveredTime}'
        #Remove package from truck
        truck.packages.remove(package)
        return deliveredTime
      

    #Start route (nearest neighbor)
    def createRoute(truck, startTime):

        #Start route
        startPoint = "4001 South 700 East"
        listOfVertexes = newGraph.convertToString()
        timeInFirstPoint = startTime

        #While we still have packages
        while len(truck.packages) > 0:

            currentPackageinDelivery = None
            minimalDistance = 140
         
            print(len(truck.packages))
            #For each package determine the best address and deliver it
            for package in truck.packages:
              
                if package.status != "Delivered":
                    #Update packages status
                    package.status = 'en route'

                    #Get indices of start and end points
                    startPointIndex = newGraph.getIndexOfVertex(startPoint)
                    possibleDestinationIndex = newGraph.getIndexOfVertex(package.address)
                
                    #Get distance between current point and possible one
                    distance = newGraph.get_distanceOfVertexes(startPointIndex, possibleDestinationIndex)

                    #Find the shortest distance
                    if distance < minimalDistance:

                        minimalDistance = distance
                        currentPackageinDelivery = package
            print(f"Package will be delivered to {currentPackageinDelivery.address} from {startPoint} with distance {minimalDistance}")
            timeInFirstPoint = deliver(currentPackageinDelivery, minimalDistance, timeInFirstPoint, truck.speed, truck)
            startPoint = currentPackageinDelivery.address
            
          
     
                        



    createRoute(firstTruck, time)


#launch App
main();


    
