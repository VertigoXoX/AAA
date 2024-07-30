import unittest
from quadratic_equation_solver import solve  # импортируем из родительской папки

class TestQuadraticEquationSolver(unittest.TestCase):
    # ... (другие тесты)

    def test_two_distinct_roots(self):
        """Проверяет, что для уравнения x^2 - 1 = 0 есть два корня кратности 1 (x1=1, x2=-1)."""
        roots = solve(1, 0, -1)
        self.assertEqual(roots, [1.0, -1.0])

if __name__ == '__main__':
    unittest.main()
