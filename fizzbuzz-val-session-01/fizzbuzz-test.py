import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_return_1_when_1(self):
        self.assertEqual(FizzBuzz.call(1), '1')

    def test_return_2_when_2(self):
        self.assertEqual(FizzBuzz.call(2), '2')
    
    def test_return_fizz_when_3(self):
        self.assertEqual(FizzBuzz.call(3), 'FIZZ')
            
    def test_return_fizz_when_multiple_of_3(self):
        self.assertEqual(FizzBuzz.call(3 * 4), 'FIZZ')
    
    def test_return_buzz_when_5(self):
        self.assertEqual(FizzBuzz.call(5), 'BUZZ')
            
    def test_return_buzz_when_multiple_of_5(self):
        self.assertEqual(FizzBuzz.call(5 * 2), 'BUZZ')

    def test_return_fizzbuzz_when_multiple_of_3_and_5(self):
        self.assertEqual(FizzBuzz.call(3 * 5), 'FIZZBUZZ')

# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()