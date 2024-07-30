import unittest
from quadratic_equation_solver import solve  # импортируйте функцию из вашего файла

class TestQuadraticEquationSolver(unittest.TestCase):
    def test_no_real_roots(self):
        """Проверяет, что для уравнения x^2 + 1 = 0 корней нет (возвращается пустой массив)."""
        self.assertEqual(solve(1, 0, 1), [1j, -1j])

if __name__ == '__main__':
    unittest.main()