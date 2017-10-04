def names ():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    for i in students:
        print i["first_name"] + " " + i["last_name"]
names()

def part_two ():
    users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
]
}
    count = 0
    counttwo = 0
    print "Students"
    for i in users["Students"]:
            count += 1
            print count," - "+i["first_name"]+" "+i["last_name"]+" - ",len(i["first_name"]+i["last_name"])
    print "Instructors"
    for i in users["Instructors"]:
            counttwo += 1
            print counttwo," - "+i["first_name"]+" "+i["last_name"]+" - ",len(i["first_name"]+i["last_name"])
part_two()