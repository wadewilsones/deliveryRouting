#This class is a template for hash table
import datetime

class HashTable:

    initialCapacity = 0

    #Constructor (dunder method)
    def __init__(self, initilal_capacity):
        
          # initialaize size of table
        self.initialCapacity = initilal_capacity

        # initialaize with empty list that has capacity number of buckets
        self.table = [[] for _ in range(initilal_capacity)]


    # Calculate hash for the table key using build-in hash()
    def _hashKey_(self, key):
        return hash(key) % self.initialCapacity


    # Inserting data into table
    def insert(self, packageData):
        
        #define key
        key = packageData.packageId;
        #hash key
        hash_key = self._hashKey_(key);
        #add to table
        self.table[hash_key].append(packageData);


    # Searching for data
    def search(self, key):
        #get hash version of a key        
        hash_key = self._hashKey_(key);
        #get value that is assign to this hashkey
        values = self.table[hash_key];
        #Make sure that if package Id doesnt exist null will be returned
        for value in values:
            if(value.packageId == key):
                return value


    def assignStatus(self, package, time):
     
        #Update current status to "en route" if it was in a hub
        if self.search(package.packageId).status == "at the hub":
            self.search(package.packageId).status = "en route"
            self.search(package.packageId).statusHistory[1][1] = time


        #Update if package was delivered
        elif self.search(package.packageId).status == "en route":
            self.search(package.packageId).status = f"Delivered at {time}"
            self.search(package.packageId).statusHistory[2][1] = time

        
    def displayPackagesHistory(self, time):
        
        #Convert string to time
        time = datetime.datetime.strptime(time, "%H:%M")
                   
        for bucket in self.table:
            for package in bucket:
                    #if still in a hub

                    if(time.time() <= package.statusHistory[0][1].time()):
                        print(f"Package {package.packageId} is {package.statusHistory[0][0]}")
                    #if still in a route
                    elif(time.time() <= package.statusHistory[1][1].time() and time.time() > package.statusHistory[0][1].time()):
                        print(f"Package {package.packageId} is {package.statusHistory[1][0]}")
                    #if delivered
                    elif(time.time() >= package.statusHistory[2][1].time()):
                        print(f"Package {package.packageId} is {package.statusHistory[2][0]}")

                        
                    
                   
                    








               
