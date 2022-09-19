import pandas as pd
from dblib.preprocess import preprocess_x, preprocess_y 
from dblib.get_sql_table import querydb_df
from dblib.knn_predict import KNN

def predict_impact(player_name):
    # pull processed df
    db_df = querydb_df()
    train_x = preprocess_x(db_df)
    train_y = preprocess_y(db_df)

    # initialize knn alg
    knn = KNN(k=30)
    # fit knn with training data
    knn.fit(train_x, train_y)

    # get player stats
    player_stats = db_df[db_df['Player'] == player_name]
    player_stats = preprocess_x(player_stats)
    #print(player_stats)

    prediction = knn.predict(player_stats)

    #print(prediction)
    if prediction == 1:
        return "{} is expected to score and assist over 20 goals this season".format(player_name)
    else:
        return "{} is expected to score and assist under 20 goals this season".format(player_name)

