import unittest
from mastermind import Mastermind


class TestMastermind(unittest.TestCase):
    def test_return_a_list_of_2_elements(self):
        self.assertEqual(2, len(Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['blue', 'yellow', 'red', 'green'])))

    def test_return_a_list_of_2_integers(self):
        response = Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['blue', 'yellow', 'red', 'green'])
        self.assertEqual(int, type(response[0]))
        self.assertEqual(int, type(response[1]))

    def test_return_4_0_when_four_well_placed(self):
        self.assertEqual([4, 0], Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['blue', 'yellow', 'red', 'green']))

    def test_return_1_0_when_one_well_placed(self):
        self.assertEqual([1, 0], Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['blue', 'pink', 'pink', 'pink']))

    def test_return_2_0_when_two_well_placed(self):
        self.assertEqual([2, 0], Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['blue', 'yellow', 'pink', 'pink']))

    def test_return_0_4_when_four_colors_misplaced(self):
        self.assertEqual([0, 4], Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['yellow', 'red', 'green', 'blue']))

    def test_return_0_3_when_three_colors_misplaced(self):
        self.assertEqual([0, 3], Mastermind.call(self, ['blue', 'yellow', 'red', 'green'], ['pink', 'red', 'green', 'blue']))

    def test_return_1_1_when_one_same_color_wellplaced_and_misplaced(self):
        self.assertEqual([1, 1], Mastermind.call(self, ['red', 'yellow', 'blue', 'blue'], ['blue', 'pink', 'pink', 'blue']))
# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()