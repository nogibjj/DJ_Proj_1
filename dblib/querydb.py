from databricks import sql
import os


def querydb(query="SELECT * FROM default.premier_league_player_stats_2_csv LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_HOST_NAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

if __name__ == "__main__":
    querydb()