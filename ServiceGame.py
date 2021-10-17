from CsvUtils import sendcsv
import csv
import pandas as pd
import json

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


class ServiceGame:

    escolha = input('P1 para Plataforma ou P2 para Publisher: ')
    if escolha == 'P1':
        tipo1 = input('Digite a plataforma desejada: ')
        save1 = platz(tipo1)
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(save1)

    elif escolha == 'P2':
        tipo2 = input('Digite a publicadora desejada: ')
        save2 = plubz(tipo2)
        with open("output.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(save2)
    pass
