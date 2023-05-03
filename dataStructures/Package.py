import datetime
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
    notes = "";
    status= ""
    statusHistory = []
    #Constructor
    def __init__(self, id, address, city, state, zipCode, deadline, weight, notes, status):

        self.packageId = id;
        self.address = address;
        self.deadline = deadline;
        self.city = city;
        self.state = state;
        self.zipCode = zipCode;
        self.weight = weight;
        self.notes = notes;
        self.status = status
        self.statusHistory = ["at the hub", datetime.datetime.combine(datetime.date.today(), datetime.time(hour=7, minute = 0))], ["en route", None],["Delivered", None]



  