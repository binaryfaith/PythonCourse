import itertools
def make_dict(arr1, arr2):
    new_dict = dict(zip(arr1,arr2))
    print new_dict
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]    
make_dict(name,favorite_animal)

#hacker challenge#
def make_dict2(arr1, arr2):
    new_dict = dict(itertools.izip(arr1,arr2))                                                          #itertools.izip combines lists into dict that uses shorter list for keys#
    print new_dict
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas","pakaderms"]    
make_dict(name,favorite_animal)

