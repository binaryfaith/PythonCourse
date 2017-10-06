class Call(object):
    def __init__(self, idNum, name, phNumber, time, reason):
        self.idNum = idNum
        self.name = name
        self.phNumber = phNumber
        self.time = time
        self.reason = reason

    def display(self):
        print "Call ID#: ", self.idNum
        print "Caller Name: ", self.name
        print "Phone Number: ", self.phNumber
        print "Time of call: ", self.reason
        print "Reason for call: ", self.reason

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = len(self.calls)

    def add(self, call):
        if isinstance(call, list):
            for num in range(0, len(call)):
                self.calls.append(call[num])
        else:
            self.calls.append(call)

        self.queueSize = len(self.calls)
        return self

    def remove(self):
        del calls[0]
        return self

    def remove(self, pNum):
        for call in self.calls:
            if call.phNumber == pNum:
                self.calls.remove(call)

    def info(self):
        for call in self.calls:
            print "{} ({}) --Queue Length: {}".format(call.name, call.phNumber, self.queueSize)
        print ""

caller0 = Call(1,"Jason","4152151466","5","Programming induced insanity")
caller1 = Call(2,"David","5102151466","6","Programming induced coma")
caller2 = Call(3,"George","3252151466","6","Programming induced diarrhea")
caller3 = Call(4,"Riccardo","9222151466","6","Programming induced murder")

cCenter1 = CallCenter()
cCenter1.add([caller0, caller1, caller2, caller3])
caller0.display()
cCenter1.info()
cCenter1.remove("4152151466")
cCenter1.info()