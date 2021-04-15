import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    result = ['1','2','FIZZ','4','BUZZ','FIZZ','7','8','FIZZ','BUZZ','11','FIZZ','13','14','FIZZBUZZ']
    def test_return_1_when_1(self):
        self.assertEqual(FizzBuzz.call(1), ''.join(TestFizzBuzz.result[:1]))

    def test_return_12_when_2(self):
        self.assertEqual(FizzBuzz.call(2), ''.join(TestFizzBuzz.result[:2]))

    def test_return_12FIZZ_when_3(self):
        self.assertEqual(FizzBuzz.call(3), ''.join(TestFizzBuzz.result[:3]))

    def test_return_12FIZZ4BUZZ_when_5(self):
        self.assertEqual(FizzBuzz.call(5), ''.join(TestFizzBuzz.result[:5]))
    
    def test_return_12FIZZ4BUZZFIZZ_when_6(self):
        self.assertEqual(FizzBuzz.call(6), ''.join(TestFizzBuzz.result[:6]))

    def test_return_12FIZZ4BUZZFIZZ78FIZZBUZZ_when_10(self):
        self.assertEqual(FizzBuzz.call(10), ''.join(TestFizzBuzz.result[:10]))
    
    def test_return_12FIZZ4BUZZFIZZ78FIZZBUZZ11FIZZ1314FIZZBUZZ_when_15(self):
        self.assertEqual(FizzBuzz.call(15), ''.join(TestFizzBuzz.result[:15]))
# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()