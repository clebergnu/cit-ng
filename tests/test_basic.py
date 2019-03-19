import unittest

from varianter_cit.Cit import Cit
from varianter_cit.Parser import Parser


class Basic(unittest.TestCase):

    def test_interface(self):
        with open("./data_file_example.txt") as input_file:
            parameters, constraints = Parser.parse(input_file)
        t_value = 2
        input_data = [parameter.get_size() for parameter in parameters]
        program = Cit(input_data, t_value, constraints)
        result = program.compute()
        self.assertIsNotNone(result)
