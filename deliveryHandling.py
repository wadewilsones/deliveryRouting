import fileHandler.getInput;
import dataStructures.packagesHashTable;
import dataStructures.distanceGraph;
import dataStructures.Truck;
import datetime
import re
import sys


#This file contains all delivery and truck manipulations 

# __init__.py
def startDelivery():

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

                    
            for package in eodPackages:
                            
                if(len(firstTruckLoad) < 9):
                    if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and not re.search(r"2", str(package.notes), re.IGNORECASE):
                        firstTruckLoad.append(package)
                            
                elif(len(secondTruckLoad) < 16 and (package not in firstTruckLoad)):

                    if not re.search(r"delayed", str(package.notes), re.IGNORECASE) and package.packageId != 9:
                        secondTruckLoad.append(package)

            #Update status to "en route"
            for pack in firstTruckLoad:
                newTable.assignStatus(pack, time)

            #Update status to "en route" for second truck
            for pack in secondTruckLoad:
                newTable.assignStatus(pack, time)                      
                
        initialLoad()




        #  Load trucks with selected packages
        firstTruck = dataStructures.Truck.Truck(16, 18, firstTruckLoad, 0, time)
        secondTruck = dataStructures.Truck.Truck(16, 18, secondTruckLoad, 0, time)

        def deliver(package, distance, startTime, speed, truck):

            #Set new time when truck will be at the address
            deliveredTime = truck.estimatedTimeofDelivery(speed, distance, startTime)
            #Increase milage
            truck.milage = truck.milage + distance

            #Test is there any other package at the same address
            for pack in truck.packages:
                if(package.address == pack.address and package.packageId != pack.packageId):
                    truck.packages.remove(pack)
                    # update in hashtable
                    newTable.assignStatus(pack, deliveredTime)
                    pack.status = 'Delivered'              
                             
            #Remove package from truck
            truck.packages.remove(package)
            #Update status to Deliver
            newTable.assignStatus(package, deliveredTime)          
              


            return deliveredTime
        

        totalMilages = 0
               
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
                #print(f"Package {currentPackageinDelivery.packageId} from {startPoint} to {currentPackageinDelivery.address} leaving at {timeInFirstPoint} will be delivered at {deliveryTime}")    
                timeInFirstPoint = deliver(currentPackageinDelivery, minimalDistance, timeInFirstPoint, truck.speed, truck)
                startPoint = currentPackageinDelivery.address
                
            

            #Go back to hub and get time of arival
            hubIndex = newGraph.getIndexOfVertex("4001 South 700 East")
            currentAddress = newGraph.getIndexOfVertex(startPoint)
            distanceToHub = newGraph.get_distanceOfVertexes(currentAddress, hubIndex)

            #Set new time when truck will be at the address
            timeToGetToDestination = distance / truck.speed
            timeAtHub = timeInFirstPoint + datetime.timedelta(hours=timeToGetToDestination)
            nonlocal totalMilages
            totalMilages += truck.milage
            return timeAtHub 
                            

        firstTruckRoute = createRoute(firstTruck, time)
        secondTruckRoute = createRoute(secondTruck, time)


        #Create a second load

        newLoad = []

        def secondLoad(truck, time):
            packagesLeft = 0
            for bucket in newTable.table:
                for packages in bucket:                    
                    if(packages.status == "at the hub"):
                        # Add entry to status history
                        newLoad.append(packages)
                        packagesLeft += 1
                        
            truck =  dataStructures.Truck.Truck(packagesLeft, 18, newLoad, truck.milage, time)

            #Update status
            for pack in newLoad:
                newTable.assignStatus(pack, time)       

            return truck        

        if(firstTruckRoute > secondTruckRoute):

            #Load and send second truck
            selectedTruck = secondLoad(secondTruck, secondTruckRoute)
            createRoute(selectedTruck, secondTruckRoute)
        else:
            #Load and send first truck
            selectedTruck = secondLoad(firstTruck, firstTruckRoute)
            createRoute(selectedTruck, firstTruckRoute)

  
        return newTable, totalMilages