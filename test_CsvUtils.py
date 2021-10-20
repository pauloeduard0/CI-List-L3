import unittest
from CsvUtils import sendcsv


class TestCsvUtils(unittest.TestCase):

    def test_number_of_lines(self):
        csv = sendcsv()
        numlines = len(csv)
        self.assertEqual(100, numlines)


if __name__ == '__main__':
    unittest.main()