import logging
import datacompy
import pandas as pd
import psycopg2
from PGDBConn import PGDBConn

def getdata(sql):
    data = []
    try:
        conn = psycopg2.connect(database="mysys", user='dbadmin', password='dbadmin1234', host='127.0.0.1', port='5432')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        logging.info(data)
        conn.close()

    except Exception as ex:
        logging.error(ex)
        raise Exception (ex)
    finally:
        return data

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
        df1 = pd.DataFrame( getDatafromDB(db.getInstance(), "select * from mydb.t1; "), columns=["fnd_id", "nav_price"])
        df2 = pd.DataFrame( getDatafromDB(db.getInstance(), "select * from mydb.t2; "), columns=["fnd_id", "nav_price"])
        compare = datacompy.Compare(df1, df2, join_columns="fnd_id")
        logging.info(compare.report())
    except Exception as ex:
        logging.error(ex)
        raise Exception(ex)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s :%(levelname)s: %(message)s")
    main()