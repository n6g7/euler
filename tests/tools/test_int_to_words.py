from tools.int_to_words import int2word
import unittest


class TestIntToWord(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(int2word(1), 'one')
        self.assertEqual(int2word(10), 'ten')
        self.assertEqual(int2word(100), 'one hundred')
        self.assertEqual(int2word(512), 'five hundred and twelve')
