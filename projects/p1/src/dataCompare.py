import logging
import datacompy
import pandas as pd
from PGDBConn import PGDBConn
# from DataSource import DataSource


def getDatafromDB(db, sql):
    data = []
    try:
        data = db.getData(sql)
        return data
    except Exception as ex:
        logging.error(ex)
        raise Exception (ex)

def main():
    try:
        logging.info("main")
        db = PGDBConn("mysys", "dbadmin", "dbadmin1234", "127.0.0.1", "5432")
        df1 = pd.read_excel("../data/nav-s1.xlsx", sheet_name='Sheet1',converters={'fnd_id':str,'fnd_ver':str})
        df2 = pd.DataFrame( getDatafromDB(db, "select * from mydb.t2;"), columns=["fnd_id", "fnd_ver", "nav_price"])
        compare = datacompy.Compare(df1, df2, join_columns=["fnd_id", "fnd_ver"])
        logging.info(compare.report())
    except Exception as ex:
        logging.error(ex)
        raise Exception(ex)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s :%(levelname)s: %(name)s: %(message)s")
    try:
        main()
        SystemExit(0)
    except:
        SystemExit(-1)