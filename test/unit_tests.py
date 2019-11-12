"""unit_tests.

Contains the unit tests for the heatrapy modules
"""

import unittest
import sys
sys.path.append('../')
import heatrapy as ht


class SingleObjects(unittest.TestCase):
    """Test all single_objects components."""

    def implicit_k(self):
        """Test single_object with the implicit_k(k) solver."""
        solution = 278
        example = ht.single_object(boundaries=[0, 200])
        self.assertEqual(int(round(example.compute(10)[5])), solution)


if __name__ == '__main__':
    unittest.main()
