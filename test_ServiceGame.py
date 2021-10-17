import unittest
from ServiceGame import platz, plubz, escolher
from Platform import platform
from Publishers import publisher


class TestServiceGame(unittest.TestCase):

    def test_games_Wii(self):
        wiigames = platz(platform('Wii'))
        self.assertEqual(15, len(wiigames))

    def test_games_PC(self):
        pc = platz(platform('PC'))
        self.assertEqual(1, len(pc))

    def test_games_SquareSoft(self):
        squaresoft = plubz(publisher('SquareSoft'))
        self.assertNotEqual(0, len(squaresoft))

    def test_games_ElectronicArts(self):
        electronicarts = plubz(publisher('Electronic Arts'))
        self.assertEqual(5, len(electronicarts))

    def test_csv_is_create(self):
        escolher('P1', platform('Wii'))
        with open('output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(15, len(conteudo))

    def test_csv_is_create2(self):
        escolher('P2', publisher('Electronic Arts'))
        with open('output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(5, len(conteudo))


if __name__ == '__main__':
    unittest.main()

