# Student: Ulada Haranina
# StudentID: 011020337

import dataStructures.packagesHashTable;
import deliveryHandling
import datetime
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
        print(f"\nTotal trucks milage: {packagesTable[1]} miles\n")
        packageId = input('To view package data, type the package id below (Type 02 for exit): \nID:')

        while(packageId != '02'):
            if packageId.isdigit():
                searchedPack = packagesTable[0].search(int(packageId))
                #Display all data of selected package
                if(searchedPack != None):
                    print("Current package data:\n")
                    print(f"Package ID: {searchedPack.packageId}\nAddress:{searchedPack.address}\nDeadline:{searchedPack.deadline}\nCity:{searchedPack.city}\nState:{searchedPack.state}\nZip Code: {searchedPack.zipCode}\nWeight:{searchedPack.weight}\nNotes:{searchedPack.notes}\nStatus:{searchedPack.status}\nHistory:{searchedPack.statusHistory}")
                    packageId = input('To view another package data, type the package id below (Type 02 for exit): \nID:')
            else:
                print('Wrong Package Id')
                packageId = input('To view package data, type the package id below (Type 02 for exit): \nID:')
   


    elif(selection == '2'):

        packagesTable = deliveryHandling.startDelivery()
        print(f"Total trucks milages {packagesTable[1]}")

        time = input("Type  time, format 15:20\nSelected Time:")
        isValid = False
        while(time != '02'):

            #Try to convert string to time
            try:
                datetime.datetime.strptime(time, '%H:%M').time()
                isValid = True

            except ValueError:
                isValid = False
            
            if (isValid):
                packagesTable[0].displayPackagesHistory(time)
                time = input("Type another time or type '02' to exit, format 15:20\nSelected Time:")

            else:
                print("Worng time format, should be '15:00'")
                time = input("Type  time or type '02' to exit:\nSelected Time:")

       
    elif(selection == '3'):
        print("Closing program..")
        sys.exit() 




#launch App
main()


    
