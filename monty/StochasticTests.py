import unittest
import monty.StochasticModeler as modeler
import numpy as np


class StochasticTests(unittest.TestCase):

    def setUp(self):
        self.data = np.array([[1, 2, 0.0], [2, 3, 0.0], [3, 4, 0.0]])

    def test_pdr(self):
        modeler.set_pdr(self.data)
        self.assertAlmostEqual(0.40546510, self.data[1, 2])
        self.assertAlmostEqual(0.28768207, self.data[2, 2])

        mean_pdr = modeler.calc_mean_pdr(self.data)
        self.assertAlmostEqual(0.34657359, mean_pdr)

        pdr_variance = modeler.calc_pdr_variance(self.data)
        self.assertAlmostEqual(0.003468210, pdr_variance)

        pdr_std_dev = modeler.calc_std_dev(self.data)
        self.assertAlmostEqual(0.058891517, pdr_std_dev)
