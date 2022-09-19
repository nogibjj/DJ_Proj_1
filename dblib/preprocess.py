import pandas as pd



def preprocess_x(df):
    #df = querydb_df()
    df['goals_assists'] = df['Goals'] + df['Assists']
    df['G_A_over_20'] = df['goals_assists'] >= .20
    df['G_A_over_20'] = df['G_A_over_20'].astype(int)
    #print(df[['Goals', 'Assists', 'goals_assists', 'G_A_over_20']])
    df_x = df[['Age', 'Starts', 'Min', 'SoT', 'G/Sh', 'G/SoT', 'ShoDist', 
    'PasTotCmp', 'PasTotAtt', 'PasTotDist', 'PasLonCmp', 'PasLonAtt', 'PasLonCmp%', 'PasAss', 'PasCrs']]
    return df_x

def preprocess_y(df):
    df = df[['G_A_over_20']]
    df['G_A_over_20'] = df['G_A_over_20'].astype(int)
    df_y = df

    return df_y





if __name__ == "__main__":
    preprocess()