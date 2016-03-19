import unittest

from game_of_life import *

class test_game_of_life(unittest.TestCase):

    def test_a_sigle_cell_dies(self):
        self.assertEquals(next([(0,0)]), [])

