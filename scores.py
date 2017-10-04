import random
def scores_grades():
    for count in range(10):
        random_num = random.randint(60,100)
        #print random_num
        if random_num >= 60 and random_num <= 70:
            print "Score: {}; Your grade is D".format(random_num)
        if random_num >= 70 and random_num <= 80:
            print "Score: {}; Your grade is C".format(random_num)
        if random_num >= 80 and random_num <= 90:
            print "Score: {}; Your grade is B".format(random_num)
        if random_num >= 90 and random_num <= 100:
            print "Score: {}; Your grade is A".format(random_num)
scores_grades()





    
