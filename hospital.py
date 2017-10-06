import random

class Patient(object):
    def __init__(self,identnum,name,allergies, bednum = 'none'):
        self.identnum = identnum
        self.name = name
        self.allergies = allergies
        self.bednum = bednum

    def info(self):
        print self.identnum
        print self.name
        print self.allergies
        print self.bednum

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.name = "Nip Your Butt"
        self.capacity = 5
        
    def admit(self,pat):
        if len(self.patients) >= self.capacity:
            print "No niptuck for you!"
        else:
            self.patients.append(pat)
            pat.bednum = random.randint(1,100)
            print "Welcome to your new face"
        return self
        
    def display(self):
        for i in self.patients:
            i.info()
    def discharge (self,dis):
        self.patients.remove(dis)  
        return self      

patient1 = Patient(1,"Dave","programming")
patient2 = Patient(2,"Riccardo","Border Patrol")
patient3 = Patient(3,"Brian","Bad Viet Food")
patient4 = Patient(4,"Jason","Carbs")
patient5 = Patient(5,"Bret","Sanity")
patient6 = Patient(6,"Cristine","Democratic states")
patient7 = Patient(7,"Kio","Gwen Stefani")

hospital1 = Hospital().admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).admit(patient6).discharge(patient1).display()




