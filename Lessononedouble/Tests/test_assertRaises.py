import unittest
from quadratic_equation_solver import solve  # импортируем из родительской папки

class TestQuadraticEquationSolver(unittest.TestCase):
    # ... (другие тесты)

    def test_zero_coefficient_a(self):
        """Проверяет, что для a = 0 функция solve() выбрасывает исключение."""
        with self.assertRaises(ValueError):
            solve(0.0, 2.0, 1.0)

if __name__ == '__main__':
    unittest.main()
