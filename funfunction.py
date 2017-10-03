def odd_even ():
    for count in range(1,2001):
        if count % 2 ==1:                                                   #if number divided by 2 has a remainder then its odd# 
            print "This is {} This is an odd number".format(count)
        else:
            print "This is {} This is an eveb number".format(count)         #for even numbers#
odd_even()

def mulitply(arr,num):
    for x in range(len(arr)):                                             #start at arr[0] run loop for length of arr#
        arr[x] *= num                                                       #multiplies arr and parameter number#
    return arr                                                          #returns value generated#
        
a = [2,4,10,16]                                                           #giving arr argument#
b = mulitply(a,5)                                                         
print b

def layered_multiples(arr):                                             #just dont get this#
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
            new_array.append(val_arr)
            return new_array
x = layered_multiples(multiply([1,3,7],2))
print x                                                     


        
