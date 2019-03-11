import unittest

from varianter_cit import Cit


class Basic(unittest.TestCase):

    def test_interface(self):
        input_data = [2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 2,
                      2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        t_value = 2
        constraints = ['0 != 1 || 1 != 0',
                       '4 != 4 || 5 != 1',
                       '4 != 5 || 5 != 1',
                       '0 != 1 || 1 != 0',
                       '3 != 0 || 4 != 4',
                       '3 != 1 || 4 != 5',
                       '1 != 0 || 4 != 0',
                       '0 != 1 || 3 != 0',
                       '1 != 1 || 4 != 3',
                       '1 != 1 || 2 != 0',
                       '3 != 0 || 5 != 0',
                       '3 != 1 || 5 != 0',
                       '3 != 0 || 5 != 0',
                       '0 != 0 || 4 != 2 || 5 != 1',
                       '0 != 1 || 1 != 0 || 3 != 1']
        program = Cit.Cit(input_data, t_value, constraints)
        result = program.compute()
        self.assertIsNotNone(result)
