# Student: Ulada Haranina
# StudentID: 011020337

import dataStructures.packagesHashTable;
import deliveryHandling
import sys

def main():


    #Welcome user
    print("Package tracker application \n")
   
    #Print options
    selection = input("Select one of the following options (type number): \n 1. View package information \n 2. Exit \nSelection:")

    while(selection != '1' and selection != '2'):
        print("Wrong selection")
        selection = input("Select one of the following options (type number): \n 1. View package information \n 2. Exit \nSelection:")

    if(selection == '1'):
        
        packagesTable =  deliveryHandling.startDelivery()
        packageId = input('To view package data, type the package id below: \nID:')
        searchedPack = packagesTable.search(int(packageId))
        #Display all data of selected package
        if(searchedPack != None):
            print("Package Data:\n")
            print(f"Package ID: {searchedPack.packageId}\nAddress:{searchedPack.address}\nDeadline:{searchedPack.deadline}\nCity:{searchedPack.city}\nState:{searchedPack.state}\nZip Code: {searchedPack.zipCode}\nWeight:{searchedPack.weight}\nNotes:{searchedPack.notes}\nStatus:{searchedPack.status}\n")
        else:
            print("Wrong package ID")
     
    elif(selection == '2'):
        print("Closing program..")
        sys.exit() 

#launch App
main();


    
