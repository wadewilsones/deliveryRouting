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
                    package = dataStructures.Package.Package(*columns, "in Dispatch")
                    #Add package to HashTable
                    newTable.insert(package)


            #Add data to graph vertex
            elif(type == "addresses"):
                index = 0
                for row in excelSheet.iter_rows(values_only=True):
                    column = row[:1]
                    if None in column:
                        continue  # skip row with None values
                    newTable.updateVertex(index, column)
                    index += 1
               
                        
            
            #Add data to graph edge
            elif(type == "distance"):
                
                addressColumn = 0
                index = 1
                counter = 0;

                # We will read all data per columns
                for column in excelSheet.iter_cols(min_col=1, max_col=28, values_only = 'True'):
                        for cell in column:
                        #Add cell into vertex if the distance not null
                            if index < 27:

                                if cell is not None and cell != 0:                           
                                    newTable.updateEdge(addressColumn, index, cell)
                                    index += 1

                            else:
                                counter = counter + 1;
                                index = 1+counter
                                addressColumn += 1







   


