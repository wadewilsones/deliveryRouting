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

    #Total miles

    milesTotal = 0

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
            if(len(firstTruckLoad) < 10):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE):
                    firstTruckLoad.append(package)
                    #Remove the package from hashtable and assign a new status
                    newTable.remove(package)
                   
        for package in eodPackages:
                          
            if(len(firstTruckLoad) < 9):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and not re.search(r"2", str(package.notes), re.IGNORECASE):
                    firstTruckLoad.append(package)
                    newTable.remove(package)
                 
                          
            elif(len(secondTruckLoad) < 16 and (package not in firstTruckLoad)):
                if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and package.packageId != 9:
                    secondTruckLoad.append(package)
                    newTable.remove(package)

    initialLoad()

    #  Load trucks with selected packages
    firstTruck = dataStructures.Truck.Truck(16, 18, firstTruckLoad, 0, time)
    secondTruck = dataStructures.Truck.Truck(16, 18, secondTruckLoad, 0, time)

    def deliver(package, distance, startTime, speed, truck):

        #Set new time when truck will be at the address
        timeToGetToDestination = distance / speed
        deliveredTime = startTime + datetime.timedelta(hours=timeToGetToDestination)
        #Increase milage
        truck.milage = truck.milage + distance

         #Test is there any other package at the same address
        for pack in truck.packages:
            if(package.address == pack.address and package.packageId != pack.packageId):
                package.status = f'Delivered at {deliveredTime}'
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
         
            #For each package determine the best address and deliver it
            for package in truck.packages:
                if package.status != "Delivered":
                    #Update packages status
                    package.status = f'en route at {timeInFirstPoint}'
                    #Get indices of start and end points
                    startPointIndex = newGraph.getIndexOfVertex(startPoint)
                    possibleDestinationIndex = newGraph.getIndexOfVertex(package.address)
                    #Get distance between current point and possible one
                    distance = newGraph.get_distanceOfVertexes(startPointIndex, possibleDestinationIndex)

                    #Change address of package 9 after 10:20
                    if package.packageId == 9 and timeInFirstPoint > datetime.datetime.combine(datetime.date.today(), datetime.time(hour=10, minute = 20)):
                        package.address = "410 S State St"
                    
                    if package.deadline != "EOD" and timeInFirstPoint > datetime.datetime.combine(datetime.date.today(), datetime.time(hour=10, minute = 0)):
                        minimalDistance = distance
                        currentPackageinDelivery = package
                        break

                    #Find the shortest distance
                    if distance < minimalDistance:
                            minimalDistance = distance
                            currentPackageinDelivery = package

            deliveryTime = truck.estimatedTimeofDelivery(truck.speed, minimalDistance, timeInFirstPoint)
            print(f"Package {currentPackageinDelivery.packageId} from {startPoint} to  with deadline {currentPackageinDelivery.address} {currentPackageinDelivery.deadline} delivered at {deliveryTime}")
            timeInFirstPoint = deliver(currentPackageinDelivery, minimalDistance, timeInFirstPoint, truck.speed, truck)
            startPoint = currentPackageinDelivery.address
            
        
            
        #Go back to hub and get time of arival
        hubIndex = newGraph.getIndexOfVertex("4001 South 700 East")
        currentAddress = newGraph.getIndexOfVertex(startPoint)
        distanceToHub = newGraph.get_distanceOfVertexes(currentAddress, hubIndex)

        #Set new time when truck will be at the address
        timeToGetToDestination = distance / truck.speed
        timeAtHub = timeInFirstPoint + datetime.timedelta(hours=timeToGetToDestination)
        #Increase milage
        truck.milage = truck.milage + distanceToHub
        return timeAtHub 
                        

    firstTruckRoute = createRoute(firstTruck, time)
    secondTruckRoute = createRoute(secondTruck, time)



    #Create a second load

    newLoad = []

    def secondLoad(truck, time):

        packagesLeft = 0
        for bucket in newTable.table:
            for packages in bucket:
                newLoad.append(packages)
                packagesLeft += 1

        truck =  dataStructures.Truck.Truck(packagesLeft, 18, newLoad, truck.milage, time)       
        return truck        

    if(firstTruckRoute > secondTruckRoute):

        #Load and send second truck
        selectedTruck = secondLoad(secondTruck, secondTruckRoute)
        createRoute(selectedTruck, secondTruckRoute)
    else:
        print("Third load")
        #Load and send first truck
        selectedTruck = secondLoad(firstTruck, firstTruckRoute)
        createRoute(selectedTruck, firstTruckRoute)



#launch App
main();


    
