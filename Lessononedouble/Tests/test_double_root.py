import unittest
from quadratic_equation_solver import solve  # импортируем из родительской папки

class TestQuadraticEquationSolver(unittest.TestCase):
    # ... (другие тесты)

    def test_double_root(self):
        """Проверяет, что для уравнения x^2 + 2x + 1 = 0 есть один корень кратности 2 (x1 = x2 = -1)."""
        roots = solve(1, 2, 1)
        self.assertEqual(roots, [-1.0, -1.0])

if __name__ == '__main__':
    unittest.main()
