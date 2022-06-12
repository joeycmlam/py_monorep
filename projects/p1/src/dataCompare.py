import logging
import datacompy
import pandas as pd


def main():
    try:
        logging.info("main")
        df1 = pd.read_excel("../data/nav-s1.xlsx")
        df2 = pd.read_excel("../data/nav-s2.xlsx")

        compare = datacompy.Compare(df1, df2, join_columns="fnd_id")
        logging.info(compare)
    except Exception as ex:
        logging.error(ex)
        raise Exception(ex)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s <%(levelname)s: %(message)s")
    main()