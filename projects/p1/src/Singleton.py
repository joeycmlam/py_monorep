class Singleton(object):
    _intance = None
    _msg = None

    @staticmethod
    def getInstance():
        if Singleton._intance == None:
            Singleton()
        return Singleton._intance

    def __init__(self):
        if Singleton._intance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._intance = self

    def setName(self, msg):
        self._msg = msg

    def getName(self):
        return self._msg


if __name__ == "__main__":
    s = Singleton()
    print (s.getName())
    s.setName("test1")
    print (s.getName())

    s = Singleton.getInstance()
    print (s.getName())
    s.setName("test2")
    s = Singleton.getInstance()
    print (s.getName())
