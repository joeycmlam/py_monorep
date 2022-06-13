from abc import ABC

class DataSource(ABC):

    def getInstance(self):
        pass

    def getData(self, sql):
        pass

    def __init__(self, database, user, password, host, port):
        pass