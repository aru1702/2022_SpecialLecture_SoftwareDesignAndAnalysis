import unittest
from CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(6, len(l))