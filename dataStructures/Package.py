# This class describes package
class Package:

    #members
    packageId = -1;
    address = ""; 
    deadline = ""; 
    city = "";
    state = "";  
    zipCode = "";
    weight = -1; 
    status = "";

    #Constructor
    def __init__(self, id, address, deadline, city, state, zipCode,weight,status):

        self.packageId = id;
        self.address = address;
        self.deadline = deadline;
        self.city = city;
        self.state = state;
        self.zipCode = zipCode;
        self.weight = weight;
        self.status = status;

