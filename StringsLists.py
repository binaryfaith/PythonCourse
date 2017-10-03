#Find and Replace#
words = "It's Thanksgiving day. It's my birthday, too!"
print words.find("day")
print (words.replace('day','month',1))

#Min and Max#
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last#
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
new = []
new.append(x[0] + x[-1])
print new

#New List#
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort()
print x
A = x[:len(x)/2]
print A
x = x[len(x)/2:]
x.insert(0,A)
print x
