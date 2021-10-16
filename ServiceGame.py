from CsvUtils import sendcsv

df = sendcsv()


def plubz(result):
    pu = []
    for index, row in df.iterrows():
        if row['publisher'] == result:
            pu.append(row)
    return pu


def platz(result):
    pl = []
    for index, row in df.iterrows():
        if row['platform'] == result:
            pl.append(row)
    return pl


'''
class ServiceGame(sendcsv()):
    # df_games = pd.read_csv('vendas-games.csv', delimiter=',')
    # df_games = pd.DataFrame(df_games.iloc[:, [0, 1, 2, 3, 5, 10]])

    platz()
    plubz()
        for plub in publisher():
        pu = []
        pu.append(df_games.loc[df_games['publisher'] == plub])
        
    import csv
    #with open('vendas-games.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    

    df_games = pd.DataFrame(csv_reader)
    csv_reader.__next__()

    for row in csv_reader:
        print(row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', ' + row[4] + ', ' + row[5])
'''
