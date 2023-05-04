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
    selection = input("Select one of the following options (type number):\n1. View package information using ID\n2. Display truck mileage and packages data during certain hours\n3. Exit \nSelection:")

    while(selection != '1' and selection != '2' and selection != '3'):
        print("Wrong selection")
        selection = input("Select one of the following options (type number):\n1. View package information using ID\n2. Display truck mileage and packages data during certain hours\n3. Exit \nSelection:")

    if(selection == '1'):
        packagesTable =  deliveryHandling.startDelivery()
        #Display total truck milage
        print(f"Total trucks milage: {packagesTable[1]} miles")
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

        packagesTable = deliveryHandling.startDelivery()
        print(f"Total trucks milages {packagesTable[1]}")
        time = input("Type  time, format 08:00\nSelected Time:")
        packagesTable[0].displayPackagesHistory(time)


       
    elif(selection == '3'):
        print("Closing program..")
        sys.exit() 

#launch App
main()


    
