import logging
import datacompy
import pandas as pd
import psycopg2

def getdata(sql):
    conn = psycopg2.connect( database="mysys", user='dbadmin', password='dbadmin1234', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    logging.info(data)
    conn.close()
    return data

def main():
    try:
        logging.info("main")
        df1 = pd.DataFrame( getdata("select * from mydb.t1; "), columns=["fnd_id", "nav_price"])
        df2 = pd.DataFrame( getdata("select * from mydb.t2; "), columns=["fnd_id", "nav_price"])
        compare = datacompy.Compare(df1, df2, join_columns="fnd_id")
        logging.info(compare.report())
    except Exception as ex:
        logging.error(ex)
        raise Exception(ex)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s :%(levelname)s: %(message)s")
    main()