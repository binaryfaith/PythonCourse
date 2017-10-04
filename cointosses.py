import random
def scores_grades():
    xy = 0
    xx = 0  
    for count in range(5001):
        random_num = random.randint(0,1)
        if random_num ==0:
            xx +=1
            print "Attempt #{}: Throwing a coin... Its a head! ... Got {} head(s) so far and {}tail(s) so far".format(count,xx,xy)
        if random_num ==1:
            xy +=1
            print "Attempt #{}: Throwing a coin... Its a tail! ... Got {} head(s) so far and {}tail(s) so far".format(count,xx,xy)        
scores_grades()
