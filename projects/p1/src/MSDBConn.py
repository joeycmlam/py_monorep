import psycopg2
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
            self._conn =cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=USXXX00345,67800;"
            "Database=DB02;"
            "UID=Alex;"
            "PWD=Alex123;")
            nxn = pyodbc.connect(cnxn_str)
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
    s = PGDBConn("mysys", "dbadmin", "dbadmin1234", "127.0.0.1", "5432")
    data = s.getData("select version()")
    print (data)
    s.close()
