#This file contains handling data import from excel and adding it to HashTable
import openpyxl;
import os;
import dataStructures.Package;
import dataStructures.packagesHashTable;

# __init__.py

# get the current working directory
#current_dir = os.path.dirname(os.path.abspath(__file__))

def insertData():

    #Create a new hashTable
    newTable = dataStructures.packagesHashTable.HashTable(40);

    #open file with packages data
    excelData = openpyxl.load_workbook('./fileHandler/packagesData.xlsx');
    excelSheet = excelData['Sheet1'];

    #Insert each row into Package object
    for row in excelSheet.iter_rows(values_only=True):
        # load only first 8 columns with slice
        columns = row[:8] 
        #Create a new package with unpacking values
        package = dataStructures.Package.Package(*columns);
        print(package.address);
        #Add package to HashTable
        newTable.insert(package);





