import unittest
import Travel_assistant as TA


class MyTestCase(unittest.TestCase):
    def setUp(self):
        t = TA.travel_assistant("India","Canada")
        self.src = t.source_details()
        self.dst = t.dest_details()

    def test_src_name(self):
        self.assertEqual(self.src[0]['name'], "India")

    def test_src_capital(self):
        self.assertEqual(self.src[0]['capital'], "New Delhi")

    def test_dest_name(self):
        self.assertEqual(self.dst[0]['name'], "Canada")

    def test_dest_a3code(self):
        self.assertEqual(self.dst[0]['alpha3Code'], "CAN")


if __name__ == '__main__':
    unittest.main()
