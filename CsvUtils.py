import pandas as pd


def sendcsv():
    df_games = pd.read_csv('vendas-games.csv', delimiter=',')
    df_games = pd.DataFrame(df_games.iloc[:, [0, 1, 2, 3, 5, 10]])

    return df_games
