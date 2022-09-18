from databricks import sql
import os
import pandas as pd


def querydb_df(query="SELECT * FROM default.football_player_stats_2020_2021"): # LIMIT 2
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_HOST_NAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result)
            df.columns=[x[0] for x in cursor.description ]

    return df

if __name__ == "__main__":
    querydb()