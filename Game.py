from ServiceGame import escolher
import csv


class Game:
    escolha = input('P1 para Plataforma ou P2 para Publisher: ')
    if escolha == 'P1':
        tipo = input('Digite a plataforma desejada: ')
        escolher(escolha, tipo)
    elif escolha == 'P2':
        tipo = input('Digite a publicadora desejada: ')
        escolher(escolha, tipo)
    arquivo = open('output.csv')

    linhas = csv.reader(arquivo)

    for linha in linhas:
        print(linha)
