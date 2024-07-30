import unittest
from quadratic_equation_solver import solve

class TestSolve(unittest.TestCase):

    # ... другие тесты

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            solve("a", 1.0, 1.0)  # Передаем "a" как строку

        with self.assertRaises(TypeError):
            solve(1.0, "b", 1.0)  # Передаем "b" как строку

        with self.assertRaises(TypeError):
            solve(1.0, 1.0, "c")  # Передаем "c" как строку
