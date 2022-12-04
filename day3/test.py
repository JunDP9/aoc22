import unittest

from day3 import solution_part_two


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(solution_part_two(
            ["vJrwpWtwJgWrhcsFMMfFFhFp",
             "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
             "PmmdzqPrVvPwwTWBwg"]), 18)  # add assertion here


if __name__ == '__main__':
    unittest.main()
