l = ['magical unicorns',19,'hello',98.98,'world']
sum = 0

if all(isinstance(i, int) for i in l) == True:
    print "The list you entered is of integer type"
    for i in l:
        sum += i
    print "Sum: {}".format(sum)

elif all(isinstance(i, str) for i in l) == True:
    "".join(l)
    print "The list you entered is of string type"
    print "String: " + " ".join(l)

elif all(isinstance(i, int) for i in l) == False:
    print "The list you entered is of mixed type"
    new = []
    for j in l:
        if isinstance(j, str) == True:
            new.append(j)
    print "String: " + " ".join(new)

    for i in l:
        if isinstance(i, str) == True:
            l.remove(i)
    for k in l:
        sum += k
    print "Sum: {}".format(sum)
