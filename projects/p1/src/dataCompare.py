import logging
import datacompy
import pandas as pd
from DataSource import DataSource
from PGDBConn import PGDBConn
from MSDBConn import MSDBConn


class dataCompare:

    def getDatafromDB(self, db, sql):
        data = []
        try:
            data = db.getData(sql)
            return data
        except Exception as ex:
            logging.error(ex)
            raise Exception (ex)

    def sendReport(self, report):
        # logging.info(report.report())
        # The mail addresses and password
        text = report.report()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

    def run(self):
        try:
            logging.info("main")
            df1 = pd.read_excel("../data/nav-s1.xlsx", sheet_name='Sheet1',converters={'fnd_id':str,'fnd_ver':str})
            df2 = pd.DataFrame( self.getDatafromDB(self._datasource, "select * from mydb.t2;"), columns=["fnd_id", "fnd_ver", "nav_price"])
            compare = datacompy.Compare(df1, df2, join_columns=["fnd_id", "fnd_ver"])
            self.sendReport(compare)
        except Exception as ex:
            logging.error(ex)
            raise Exception(ex)

    def __init__(self, db: DataSource):
        self._datasource = db

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s :%(levelname)s: %(name)s: %(message)s")
    try:
        db = PGDBConn("mysys", "dbadmin", "dbadmin1234", "127.0.0.1", "5432")
        # db = MSDBConn("mysys", "sa", "DBadmin1234", "127.0.0.1", "1433")
        app = dataCompare(db)
        app.run()
        SystemExit(0)
    except Exception as ex:
        logging.error(ex)
        SystemExit(-1)