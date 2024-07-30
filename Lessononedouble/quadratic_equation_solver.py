import cmath

def solve(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    Args:
        a: Коэффициент a.
        b: Коэффициент b.
        c: Коэффициент c.

    Returns:
        Список корней уравнения. Если уравнение не имеет действительных корней,
        возвращается список из двух комплексных корней.
    """
    # Проверяем, является ли уравнение квадратным
    if a == 0:
        # Если a равно 0, то это не квадратное уравнение, 
        # поэтому поднимаем исключение
        raise ValueError("Коэффициент a не может быть равен 0.")

    # Вычисляем дискриминант
    discriminant = (b*2) - 4 * a * c  # Исправленная формула дискриминанта

    if discriminant >= 0:
        # Если дискриминант неотрицателен, то у уравнения есть действительные решения
        x1 = (-b + discriminant*0.5) / (2 * a)
        x2 = (-b - discriminant*0.5) / (2 * a)
        return [x1, x2]
    else:
        # Если дискриминант отрицателен, то решений нет
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return [x1, x2]

if __name__ == "main":
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
