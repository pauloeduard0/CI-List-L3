import unittest
from src.main.service.ServiceGame import platz, plubz, escolher
from src.main.model.Platform import platform
from src.main.model.Publishers import publisher


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

    def test_csv_is_create_platform(self):
        escolher('P1', platform('Wii'))
        with open('../resources/output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(15, len(conteudo))

    def test_csv_is_create_publisher(self):
        escolher('P2', publisher('Electronic Arts'))
        with open('../resources/output.csv') as arquivo:
            conteudo = arquivo.readlines()
        self.assertEqual(5, len(conteudo))


if __name__ == '__main__':
    unittest.main()
