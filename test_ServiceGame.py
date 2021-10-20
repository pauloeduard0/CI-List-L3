import unittest
import ServiceGame
from model.Platform import platform
from model.Publishers import publisher


class TestServiceGame(unittest.TestCase):

    def test_games_Wii(self):
        wiigames = ServiceGame.platz(platform('Wii'))
        self.assertEqual(15, len(wiigames))

    def test_games_PC(self):
        pc = ServiceGame.platz(platform('PC'))
        self.assertEqual(1, len(pc))

    def test_games_SquareSoft(self):
        squaresoft = ServiceGame.plubz(publisher('SquareSoft'))
        self.assertNotEqual(0, len(squaresoft))

    def test_games_ElectronicArts(self):
        electronicarts = ServiceGame.plubz(publisher('Electronic Arts'))
        self.assertEqual(5, len(electronicarts))

    def test_csv_is_create_platform(self):
        ServiceGame.escolher('P1', platform('Wii'))
        with open('output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(15, len(conteudo))

    def test_csv_is_create_publisher(self):
        ServiceGame.escolher('P2', publisher('Electronic Arts'))
        with open('output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(5, len(conteudo))


if __name__ == '__main__':
    unittest.main()
