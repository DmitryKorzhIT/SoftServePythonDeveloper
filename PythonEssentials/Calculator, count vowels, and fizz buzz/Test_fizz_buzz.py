import unittest
import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

    # Test divided only on 3.
    def test_fizz(self):
        number=6
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'Fizz')

    # Test divided only on 5.
    def test_buzz(self):
        number=845
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'Buzz')

    # Test divided both on 3 and on 5.
    def test_fizzbuzz(self):
        number = 45
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'FizzBuzz')

    # Test not expected characters.
    def test_symbol(self):
        number = 'qw'
        result = fizz_buzz.get_reply(number)
        self.assertEqual(result, 'Please change your input on an integer number.')

if __name__=='__main__':
    unittest.main()