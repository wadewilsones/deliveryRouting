# Student: Ulada Haranina
# StudentID: 011020337


import fileHandler.getInput;
import dataStructures.packagesHashTable;
import dataStructures.distanceGraph;


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
    #Add GUI




#launch App
main();


    
