#This class descriibe truck data
class Truck:

  #constructor

  def __init__(self, capacity, speed, packages, address, milage, timeLeavingtHub ):

    self.capacity = capacity;
    self.speed = speed;
    self.packages = packages;
    self.address = address;
    self.milage = milage;
    self.timeLeavingtHub = timeLeavingtHub;

    # Display truck data

    def __displayTruckData__ (self, capacity, speed, packages, address, milage, timeLeavingtHub ):
        trackData = [capacity, speed, packages, address, milage, timeLeavingtHub];
        return trackData;
