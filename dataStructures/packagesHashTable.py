#This class is a template for hash table

class HashTable:

    initilal_capacity = 40;

    #Constructor (dunder method)
    def __init__(self, initilal_capacity):
        
          # initialaize size of table
        self.initialCapacity = initilal_capacity;

        # initialaize with empty list that has capacity number of buckets
        self.table = [[] for _ in range(initilal_capacity)]


    # Calculate hash for the table key using build-in hash()
    def _hashKey_(self, key):
        return hash(key) % self.initilal_capacity


    # Inserting data into table
    def insert(self, packageData):
        
        #define key
        key = packageData.packageId;
        #hash key
        hash_key = self._hashKey_(key);
        #add to table
        self.table[hash_key].append(packageData);


    #print data (TEST)
    def printTable(self):
        for tableBucket in self.table:
            for item in tableBucket:
                print("Key:", item.packageId)
                print("Value:", item.address)

    

