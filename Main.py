# Student: Ulada Haranina
# StudentID: 011020337

import dataStructures.packagesHashTable;
import deliveryHandling
from datetime import datetime
import sys

def main():


    #Welcome user
    print("Package tracker application \n")
   
    #Print options
    selection = input("Select one of the following options (type number):\n1. View package information \n2. Get data for packages at selected time\n3. Exit \nSelection:")
    packagesTable =  deliveryHandling.startDelivery()

    while(selection != '1' and selection != '2' and selection != '3'):
        print("Wrong selection")
        selection = input("Select one of the following options (type number):\n1. View current package information \n2. Get data for packages at selected time \n3. Exit \nSelection:")

    if(selection == '1'):
        
        packageId = input('To view package data, type the package id below (Type 02 for exit): \nID:')

        while(packageId != '02' and packageId.isdigit()):

            searchedPack = packagesTable[0].search(int(packageId))
            #Display all data of selected package
            if(searchedPack != None):
                print("Current package data:\n")
                print(f"Package ID: {searchedPack.packageId}\nAddress:{searchedPack.address}\nDeadline:{searchedPack.deadline}\nCity:{searchedPack.city}\nState:{searchedPack.state}\nZip Code: {searchedPack.zipCode}\nWeight:{searchedPack.weight}\nNotes:{searchedPack.notes}\nStatus:{searchedPack.status}\nHistory:{searchedPack.statusHistory}")
                packageId = input('To view another package data, type the package id below (Type 02 for exit): \nID:')
            else:
                print("Wrong package ID")
    
     
    elif(selection == '2'):
        #Display total truck milage
        print(f"Total trucks milage: {packagesTable[1]} miles")


        #packageId = input("\nType package ID\nID: ")
        #timeRangeStart = input("\nStart time range, format '08:00'\nStart: ")
        #timeRangeEnd = input("\nEnd time range, format '15:00'\nEnd: ")

        #Convert time string into datetime object
        #timeRangeStart = datetime.strptime(timeRangeStart, "%H:%M")
        #timeRangeEnd = datetime.strptime(timeRangeEnd, "%H:%M")

        #if(packageId != '02' and timeRangeStart != '02' and timeRangeEnd != '02'):

            #Search for a package with id
            #package = packagesTable[0].search(int(packageId))

            #print(package.printStatus(package, timeRangeStart, timeRangeEnd))

       
    elif(selection == '3'):
        print("Closing program..")
        sys.exit() 

#launch App
main()


    
