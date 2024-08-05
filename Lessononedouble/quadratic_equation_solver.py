import cmath

def solve(a, b, c, eps=1e-6):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    Args:
        a: Коэффициент a.
        b: Коэффициент b.
        c: Коэффициент c.
        eps: Порог для сравнения дискриминанта с нулем (по умолчанию 1e-6).

    Returns:
        Список корней уравнения. Если уравнение не имеет действительных корней,
        возвращается список из двух комплексных корней.
    """
    # Проверяем, является ли уравнение квадратным
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен 0.")

    # Проверяем, являются ли коэффициенты числами
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Коэффициенты должны быть числами.")

    # Проверяем, не являются ли коэффициенты NaN, Infinity, -Infinity
    if any(not x or not isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("Коэффициенты не могут быть NaN, Infinity или -Infinity.")

    # Вычисляем дискриминант
    discriminant = b*2 - 4 * a * c

    # Сравниваем дискриминант с epsilon
    if abs(discriminant) < eps:
        # Если дискриминант очень близок к нулю, то у уравнения есть два одинаковых корня
        x = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return [x, x]
    elif discriminant < -eps:
        # Если дискриминант отрицателен, то у уравнения есть комплексные решения
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    else:
        # Если дискриминант неотрицателен, то у уравнения есть действительные решения
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return [x1, x2]

if __name__ == "__main__":
    # Примеры использования
    roots1 = solve(1, -5, 6)
    print("Корни уравнения x^2 - 5x + 6 = 0:")
    for root in roots1:
        print(root)

    roots2 = solve(2, 4, -6)
    print("\nКорни уравнения 2x^2 + 4x - 6 = 0:")
    for root in roots2:
        print(root)

    roots3 = solve(1, 2, 1)
    print("\nКорни уравнения x^2 + 2x + 1 = 0:")
    for root in roots3:
        print(root)
