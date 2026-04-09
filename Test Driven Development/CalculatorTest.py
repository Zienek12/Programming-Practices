import unittest
from Calculator import Add

class TestCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_add_single_number(self):
        self.assertEqual(Add("1"), 1)

    def test_add_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)

    def test_add_multiple_numbers(self):
        self.assertEqual(Add("1,2,3,4"), 10)

    def test_add_invalid_input_value_error(self):
        with self.assertRaises(ValueError):
            Add("1,a")

    def test_add_trailing_comma(self):
        with self.assertRaises(ValueError):
            Add("1,2,")

    def test_add_newline_seperator(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_newline_sequence(self):
        with self.assertRaises(ValueError):
            Add("1,\n2")
            
    def test_multiple_newline_seperators(self):
        self.assertEqual(Add("1\n2\n3"), 6)
        
if __name__ == '__main__':
    unittest.main()