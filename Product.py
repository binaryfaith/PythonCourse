class product(object):
    def __init__(self,price,item_number,Weight,Brand,Cost,Status):
        self.price = price
        self.item_number = item_number
        self.Weight = Weight
        self.Brand = Brand
        self.Cost = Cost
        self.Status = Status
        
    def Sell(self):
        if self.Status == "buy":
            self.Status = "Sold"
        return self
    def Tax(self):
        self.price = self.price + (self.price * .08)
        return self
    def Return(self):
        if self.Status == "defective":
            self.Status = "defective"
            self.price = 0
        if self.Status == "box":
            self.Status = "For Sale"
        if self.Status == "openbox":
            self.Status = "Used"
            self.price = self.price - (self.price * .2)
        return self

    def display_all(self):
        print "Price:", self.price, "item_number:", self.item_number, "Weight:", self.Weight, "Brand:", self.Brand, "Cost:", self.Cost,"Status",self.Status

nintendo = product(200,"#5","15lbs","Nintendo",100,"buy")

nintendo.Sell().Tax().Return().display_all()