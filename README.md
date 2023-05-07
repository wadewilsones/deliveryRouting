# WGUPS ROUTING PROGRAM

### This application is implementing a greedy algorithm to determine the optimal way to deliver 40 packages in time.


## Rubric 
### <b>A. Used algoirthm:</b> The nearest neighbor greedy algorithm  was used to create the program logic for delivery packages
### <b>B. Program overview:</b> 

The purpose of this program is to create an algorithm that will deliver all 40 packages before the deadline and truck mileages below 140 miles.


### 1. Pseudocode of algorithm logic:

    <i>
    FUNCTION createRoute(selected truck, start time)
        startPoint = "4001 South 700 East"
        listOfVertexes = newGraph.convertToString()
        timeInFirstPoint = startTime

        WHILE truck.packages is not empty DO

        currentPackageinDelivery = null
        minimalDistance = 140

            FOR EACH package in truck.packages DO
                IF package.status is not "Delivered" THEN
                startPointIndex = newGraph.getIndexOfVertex(startPoint)
                possibleDestinationIndex = newGraph.getIndexOfVertex(package.address)
                
                distance = newGraph.get_distanceOfVertexes(startPointIndex, possibleDestinationIndex)
                
                IF package.packageId is 9 AND timeInFirstPoint is greater than 10:20 THEN
                    package.address = "410 S State St"
                
                IF package.deadline is not "EOD" AND timeInFirstPoint is greater than 10:00 THEN
                    minimalDistance = distance
                    currentPackageinDelivery = package
                    BREAK
                    
                IF distance is  than minimalDistance THEN
                    minimalDistance = distance
                    currentPackageinDelivery = package
        
        deliveryTime = truck.estimatedTimeofDelivery(truck.speed, minimalDistance, timeInFirstPoint)
        timeInFirstPoint = deliver(currentPackageinDelivery, minimalDistance, timeInFirstPoint, truck.speed, truck)
        startPoint = currentPackageinDelivery.address
    
        END WHILE
    
        END FUNCTION
    </i>

## 2. Programming environment: 
    - Visual Studio Code editor, vesrion: 1.74.3; 
    - Python Version: 3.10.6;
    - Installed libraries: <i>openpyfxl, </i>


## 3. Space-time complexity:

    - function getInput() has overall complexity of: O(n^2) 
    - function startDelivery():
        - dataStructures.packagesHashTable.HashTable() : O(1)
        - newGraph = dataStructures.distanceGraph.distanceGraph(27) : O(n^2)
        - firstTruck/second truck : O(1)
        - initialLoad() : O(n)
        - deliver() : O(n)
        - createRoute() : O(n^2)


     startDelivery() has overall complexity of: O(n^2) 

    
## 4. Capability to adapt 

The complexity of the algorithm will always stay as O(n^2) not depending on the input. The code relies on iterating through lists with limited items in it (truck constraints), so the packages always are separated. In the future possible to spread packages between more trucks. Mostly because of the linearity of provided code,  it is easier to adapt and scale.

## 5. Maintainance

This code is easier to maintain since the code is adopted the modularity principle (each functionality is described on a separate file and functions are used), so it is more readable and has fewer scrolling and lines. We don't need to touch code if we want to add, edit, or remove data need, because the program read the data automatically from the spreadsheet. 

## 6. Strengths and weaknesses of the self-adjusting data structures 

An example of a self-adjusting data structure is hash tables. Its main strength of it is a fast search. The index used in search allows one to perform the task much faster and easier. The fact that this data structure can be adjusted is very valuable since it allows us to work with data that is dynamically changed. As a weakness can be mentioned the possibility of collisions, that necessary to be addressed by certain techniques (such as chaining). (Hash table. Programiz.) Also, hash tables can be hard to implement. 


## D. 
 ### 1. Relationship between the stored data points
 This program has 2 main data structures which are hash table and graph. So all package addresses are kept as values in a hashtable so we have quick access to them when needed, using the key, which is equal to the package ID.  

The data that contain a list of all possible addresses and the distance between them are contained in a graph, vertices keep addresses and edges distance between them. 

 So, when the algorithm is selecting the next delivery point it compares all vertices addresses that are in the current list and their distance that is kept in edges, selecting the minimal distance between points.


## I. Core algorithm 

1. Strengths: 
    - Can be easily scaled up or down, since it design to adapt to changes. 
    - It is easy to implement, so fewer errors can be made. 
    - The algorithm is including packages priority that makes recourse utilization more efficient

2.  The algorithm total mileage is less than 140, all 40 packages are delivered before their deadline, and trucks have no more than 16 packages per truck 

3.  One of the algorithms that would also meet these requirements is divided and conquer could be implemented by separate packages into 2-3 groups based on delivery deadlines.  And the second one is a dynamic programming algorithm also could meet this requirement, especially if the list packages and addresses would dynamically change during the day (Dynamic Programming. Programiz.)

4. 
    The main difference between the divided and conquer algorithm and implemented nearest neighbor one is that the nearest neighbor is just simply selected as the shortest path, while divide and conquer just recursively would solve the subproblems. Possibly less efficient.

    Between dynamic programming and nearest neighbor, the difference is the last algorithm can be not the optimal one, while dynamic programming will make the solution more optimized.

## J. 

If I would have to do this project again I would create a graphic user interface, instead of a console one.  

## K

1. A created Hash table is meeting all requirements, it is created without a dictionary and has key-value pairs, where the key is represented as a package Id and the value is the package object. It also has an insert, and search function, that allows one to look for an item fast using the key.

    a. The search time is not affected by package numbers because the hash map mapped the key to the bucket that holds the package. The search time is constant.

    b. The search time is not affected by a number of trucks or cities because the hash map mapped the key to the bucket that holds the package. The search time is still constant.

2. 
    A binary search tree could be another data structure that could be used to meet requirements. The root would start from, the middle of package IDs.

    Priority queue where each package has an attached deadline to it,  can be a second data structure that could meet the provided requirements. Packages are sorted, so the closer deadline - the higher the package in the queue, so it can be easily retrieved. 

    a. The difference between a hash table and a binary tree is that tree elements are sorted, and the root is starting in the middle. While hash table just has a key and value pair. They have different complexity, and while the hash table element search has constant time, the binary tree search takes n times, so it depends on input size.

    The hash table and priority queue are also pretty different, the queue is sorted and elements are going from the top of the queue, while the hash table has access to all elements. 



## Sources

1. Hash table. Programiz. (n.d.). Retrieved May 4, 2023, from https://www.programiz.com/dsa/hash-table 
2. Dynamic Programming. Programiz. (n.d.). Retrieved May 4, 2023, from https://www.programiz.com/dsa/dynamic-programming 