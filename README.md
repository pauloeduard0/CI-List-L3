# CI-List-L3

# Projeto desenvolvido para realização de testes automatizados

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Python 3.0+
IDE Pycharm ou não
```

### 🔧 Instalação

Devemos instalar a biblioteca Pandas para criarmos um Data Frame:

```
pip install pandas
```

## ⚙️ Executando os testes

Para executar os testes automatizados você precisa acessar os arquivos test_ e rodar a classe TestServiceGame.

### 🔩 Analise os testes de ponta a ponta

Esses testes mostram a geração da lista desejada pela plataforma ou publicadora escolhida, selecionando apenas os dados buscados.
```
78,FIFA 16,PS4,2015,Electronic Arts,8.49
83,FIFA Soccer 13,PS3,2012,Electronic Arts,8.24
84,The Sims 3,PC,2009,Electronic Arts,8.11
93,Star Wars Battlefront (2015),PS4,2015,Electronic Arts,7.67
100,Battlefield 3,X360,2011,Electronic Arts,7.34
```

### ⌨️ E testes de estilo de codificação

Este exemplo de teste compara se uma lista criada a partir da seleção da plataforma 'Wii' tem mesmo a quantidade correta de 15 dados.

```
    def test_csv_is_create_platform(self):
        escolher('P1', platform('Wii'))
        with open('../resources/output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(15, len(conteudo))
```

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [PyCharm](https://www.jetbrains.com/pt-br/pycharm/) - IDE usada

## ✒️ Autor

[Paulo Eduardo Rocha Silveira](https://github.com/pauloeduard0)
