class bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price " + str(self.price) + "$"
        print "Riding " + str(self.max_speed) 
        print "Reversing " + str(self.miles)
        return self
    def Ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles>=5:
            self.miles -= 5
        return self
bike1 = bike(10,100,10)
bike2 = bike(10,100,20)
bike3 = bike(10,100,30)
bike1.displayInfo().Ride().reverse()
bike1.displayInfo().Ride().reverse()
bike1.displayInfo().Ride().reverse()
bike2.displayInfo().Ride().reverse()
bike2.displayInfo().Ride().reverse()
bike2.displayInfo().Ride().reverse()
bike3.displayInfo().Ride().reverse()
bike3.displayInfo().Ride().reverse()
bike3.displayInfo().Ride().reverse()




        
        
