import unittest
from quadratic_equation_solver import solve

class TestSolve(unittest.TestCase):

    def test_zero_coefficient_a(self):
        with self.assertRaises(ValueError):
            solve(0.0, 1.0, 1.0)  # Передаем "a" как 0.0 (double)

    # ... другие тесты
