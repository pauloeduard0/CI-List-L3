import unittest
from CsvUtils import sendcsv


class TestCsvutils(unittest.TestCase):

    def test_number_of_lines(self):
        numlines = len(sendcsv())
        self.assertEqual(100, numlines)


if __name__ == '__main__':
    unittest.main()
