#This file contains handling data import from excel and adding it to HashTable
import openpyxl;
import dataStructures.Package;
import dataStructures.packagesHashTable;

# __init__.py


def insertData(newTable, type):


        #open file with data
            excelData = openpyxl.load_workbook(f'./fileHandler/{type}.xlsx')
            excelSheet = excelData['Sheet1']

            if(type == "package"):
                #Insert each row into Package object
                for row in excelSheet.iter_rows(values_only=True):

                    # load only first 8 columns with slice
                    columns = row[:8] 

                    #Create a new package with unpacking values
                    package = dataStructures.Package.Package(*columns)

                    #Add package to HashTable
                    newTable.insert(package)


            #Add data to graph vertex
            elif(type == "addresses"):
                index = 0
                for row in excelSheet.iter_rows(values_only=True):
                    column = row[:1]
                    newTable.updateVertex(index, column)
                    index = index+1
                newTable.printVertex()


            #Add data to graph edge
            elif(type == "distance"):
               print("Add distance to edge")        
  



   


