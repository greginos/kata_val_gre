import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_return_1_when_1(self):
        self.assertEqual(FizzBuzz.call(1), '1')
    def test_return_2_when_2(self):
        self.assertEqual(FizzBuzz.call(2), '2')
    def test_return_FIZZ_when_3(self):
        self.assertEqual(FizzBuzz.call(3), 'FIZZ')
    def test_return_BUZZ_when_5(self):
        self.assertEqual(FizzBuzz.call(5), 'BUZZ')
    def test_return_FIZZ_when_6(self):
        self.assertEqual(FizzBuzz.call(6), 'FIZZ')
    def test_return_BUZZ_when_10(self):
        self.assertEqual(FizzBuzz.call(10), 'BUZZ')
    def test_return_FIZZBUZZ_when_15(self):
        self.assertEqual(FizzBuzz.call(15), 'FIZZBUZZ')
    def test_return_WIZZ_when_7(self):
        self.assertEqual(FizzBuzz.call(7), 'WIZZ')
    def test_return_WIZZ_when_14(self):
        self.assertEqual(FizzBuzz.call(14), 'WIZZ')
    def test_return_FIZZWIZZ_when_21(self):
        self.assertEqual(FizzBuzz.call(21), 'FIZZWIZZ')
    def test_return_BUZZWIZZ_when_35(self):
        self.assertEqual(FizzBuzz.call(35), 'BUZZWIZZ')
    def test_return_FIZZBUZZWIZZ_when_105(self):
        self.assertEqual(FizzBuzz.call(105), 'FIZZBUZZWIZZ')

# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()