import datetime
#This class descriibe truck data
class Truck:

  #constructor

  def __init__(self, capacity, speed, packages, milage, timeLeavingtHub ):

    self.capacity = capacity;
    self.speed = speed;
    self.packages = packages;
    self.milage = milage;
    self.timeLeavingtHub = timeLeavingtHub;

    # Display truck data

  def __displayTruckData__ (self, capacity, speed, packages,  milage, timeLeavingtHub ):
    trackData = [capacity, speed, packages, milage, timeLeavingtHub];
    return trackData;


    #Calculate estimated time of delivery    

  def estimatedTimeofDelivery(self, speed, distance, currentTime):
    #Set new time when truck will be at the address
    timeToGetToDestination = distance / speed
    estimatedTime = currentTime + datetime.timedelta(hours=timeToGetToDestination)
    return estimatedTime