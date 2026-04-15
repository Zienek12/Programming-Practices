import unittest
from Calculator import Add

class TestStringCalculator(unittest.TestCase):

    # Punkt 1: Podstawowe przypadki
    def test_add_empty_string_returns_zero(self):
        self.assertEqual(Add(""), 0)

    def test_add_single_number_returns_value(self):
        self.assertEqual(Add("1"), 1)

    def test_add_two_numbers_returns_sum(self):
        self.assertEqual(Add("1,2"), 3)

    # Punkt 3: Wiele liczb
    def test_add_multiple_numbers_returns_sum(self):
        # Sprawdzenie czy funkcja radzi sobie z wiecej niz dwiema liczbami
        self.assertEqual(Add("1,2,3,4"), 10)

    # Punkt 3: Wykrywanie bledu (ValueError)
    def test_add_invalid_input_raises_value_error(self):
        # Sprawdzenie czy funkcja wyrzuci blad przy nieprawidlowych danych
        with self.assertRaises(ValueError):
            Add("1,invalid")

    # Punkt 5: Znaki nowej linii
    def test_add_newline_separator_returns_sum(self):
        # Obsluga znaku \n zamiast przecinka
        self.assertEqual(Add("1\n2,3"), 6)

    def test_add_invalid_newline_format_raises_error(self):
        # Przypadek "1,\n" jest bledny zgodnie z instrukcja
        # Poniewaz instrukcja nie precyzuje typu bledu, uzywamy ValueError
        with self.assertRaises(ValueError):
            Add("1,\n")

if __name__ == "__main__":
    unittest.main()