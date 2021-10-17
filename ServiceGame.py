from CsvUtils import sendcsv
import csv

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


def escolher(escolhido, tipo):
    if escolhido == 'P1':
        save1 = platz(tipo)
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(save1)

    elif escolhido == 'P2':
        save2 = plubz(tipo)
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(save2)

