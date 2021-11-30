import count_vowels
import unittest

class CountVowelsTests(unittest.TestCase):

    # Test usual string.
    def test_usual_string(self):
        input = 'Hello, World!'
        result = count_vowels.get_res(input)
        self.assertEqual(result, 3)

    # Test symbols in a string.
    def test_word_with_symbols(self):
        input = 'H24*ello)_ WORL!!d&'
        result = count_vowels.get_res(input)
        self.assertEqual(result, 3)

    # Test an empty string.
    def test_zero_input(self):
        input = ''
        result = count_vowels.get_res(input)
        self.assertEqual(result, 0)

if __name__=='__main__':
    unittest.main()
