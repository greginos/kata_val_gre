import unittest
from mastermind import Mastermind

BASIC_SECRET = ['blue', 'yellow', 'red', 'green']

class TestMastermind(unittest.TestCase):
    def test_return_a_list_of_2_elements(self):
        self.assertEqual(len(Mastermind.call(BASIC_SECRET, BASIC_SECRET)), 2)
    def test_return_a_list_of_2_integers(self):
        list_result = Mastermind.call(BASIC_SECRET, BASIC_SECRET)
        self.assertEqual(type(list_result[0]), int)
        self.assertEqual(type(list_result[1]), int)
    def test_return_a_list_of_4_and_0_for_a_perfect_match(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, BASIC_SECRET), [4, 0])
    def test_return_a_list_of_3_and_0_for_one_missing_color(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, ['pink', 'yellow', 'red', 'green']), [3, 0])
    def test_return_a_list_of_2_and_0_for_two_missing_colors(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, ['pink', 'pink', 'red', 'green']), [2, 0])
    def test_return_a_list_of_0_and_0_for_a_completely_wrong_match(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, ['pink', 'pink', 'pink', 'pink']), [0, 0])
    def test_return_a_list_of_0_and_1_for_one_misplaced_color(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, ['pink', 'pink', 'pink', 'blue']), [0, 1])
    def test_return_a_list_of_0_and_4_for_all_misplaced_colors(self):
        self.assertEqual(Mastermind.call(BASIC_SECRET, ['yellow', 'red', 'green', 'blue']), [0, 4])
    # def test_find_a_misplaced_color(self):
    #     self.assertEqual(Mastermind.call(['blue', 'yellow', 'red', 'green'], ['pink', 'blue', 'pink', 'pink']), [0, 1])

# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()