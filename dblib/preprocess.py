import pandas as pd
from get_sql_table import querydb_df


def preprocess():
    df = querydb_df()
    print(df)

if __name__ == "__main__":
    preprocess()