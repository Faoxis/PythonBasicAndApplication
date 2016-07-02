import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, obj):
        super(LoggableList, self).append(obj)
        super(LoggableList, self).log(obj)


lst = LoggableList()
lst.append('something1')
lst.append('something2')