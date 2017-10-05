class animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 20
        
    def walk(self):
        if self.health > 0:
            self.health -= 1
        return self
    def run(self):
        if self.health >= 5:
            self.health -= 5
        return self

    def display_all(self):
        print "Name:", self.name, "Health:", self.health

#Instance walks 3 times and runs twice displays health has changed to 7 from 20#
ninja = animal("Didi")
ninja.walk().walk().walk().run().run().display_all()

#creation of dog class#
class dog(animal):
    def __init__(self,name):
        super(dog,self).__init__(name)
        self.health = 150  

    def pet(self):
        self.health += 5
        return self    
        
#Instance walks 3 times and runs twice displays health has changed to 137 from 150#
spike = dog("Spike").walk().walk().walk().run().run().display_all()
#below confirms that dog cannot fly: AttributeError: 'dog' object has no attribute 'fly'#
spike = dog("Spike").fly.display_all()

#creation of dragon class#
class dragon(animal):
    def __init__(self,name):
        super(dragon,self).__init__(name)
        self.health = 170  

    def fly(self):
        self.health -= 10
        return self 

    def display_drag(self):
        print "I am a Dragon:", self.health   
        
#Display health prints the above and decrements health. Does not inherit anything from dog#
draco = dragon("draco").fly().display_drag()

#New Animal#
newanimal = animal("newanimal").display_all()