import pytds
from DataSource import DataSource

class MSDBConn(DataSource):
    _instance = None
    _conn = None
    _database = None

    @staticmethod
    def getInstance(self):
        if PGDBConn._instance == None:
            PGDBConn()
        return MSDBConn._instance

    def __init__(self):
        PGDBConn._instance = self

    def __init__(self, database, user, password, host, port):
        if MSDBConn._instance == None:
            self._database = database
            self._conn = pytds.connect(host, database, user, password)
            MSDBConn._instance = self

    def getDatabase(self):
        return self._database

    def getData(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def close(self):
        self._conn.close()


if __name__ == "__main__":
    s = MSDBConn("mysys", "sa", "DBadmin1234", "127.0.0.1", "1433")
    data = s.getData("select @@version")
    print (data)
    s.close()
