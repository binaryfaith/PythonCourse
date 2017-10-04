class car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = 0
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
        
    def display_all(self):
        print "Price:", self.price, "Speed:", self.speed, "Fuel:", self.fuel, "Mileage:", self.mileage, "Tax:", self.tax
        return self
        
mustang = car(12000,10,10,10)
impala = car(9000,100,50,90)
toyota = car(15000,67,56,134)
ferrari = car(19000,34,76,34)
ford = car(9000,134,134,15)
bus = car(50000,134,67,76)
mustang.display_all()
impala.display_all()
toyota.display_all()
ferrari.display_all()
ford.display_all()
bus.display_all()