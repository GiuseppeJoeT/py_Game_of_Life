import unittest

from game_of_life import *


class TestGameOfLife(unittest.TestCase):
    def test_next_generation_of_empty_pattern_is_empty(self):
        self.assertEquals(next([]), [])

    def test_a_sigle_cell_dies(self):
        self.assertEquals(next([(0, 0)]), [])

    def test_a_single_cell_dies(self):
        self.assertEquals(next([0, 0]), [])
