import psycopg2

class PGDBConn(object):
    _instance = None
    _conn = None
    _database = None

    @staticmethod
    def getInstance():
        if PGDBConn._instance == None:
            PGDBConn()
        return PGDBConn._instance

    def __init__(self, database, user, password, host, port):
        if PGDBConn._instance == None:
            self._database = database
            self._conn = psycopg2.connect(database=database, user=user, password=password, host=host,
                                    port=port)
            PGDBConn._instance = self

    def getDatabase(self):
        return self._database

    def getData(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def close(self):
        self._conn.close()


if __name__ == "__main__":
    s = PGDBConn("mysys")
    print (s.getDatabase())
    data = s.getData("select version()")
    print (data)