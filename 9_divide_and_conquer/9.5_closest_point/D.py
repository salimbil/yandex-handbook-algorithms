# Компилятор: Python 3.13.2
def convex_hull(points):
    """Построение выпуклой оболочки методом Грэхэма"""
    if len(points) <= 1:
        return points
    
    # Сортируем точки по x, затем по y
    points = sorted(points, key=lambda p: (p.x, p.y))
    
    # Нижняя оболочка
    lower = []
    for p in points:
        while len(lower) >= 2 and (lower[-1] - lower[-2]).cross(p - lower[-2]) <= 0:
            lower.pop()
        lower.append(p)
    
    # Верхняя оболочка
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and (upper[-1] - upper[-2]).cross(p - upper[-2]) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def max_triangle_area_from_edge(convex_hull, p1, p2):
    """Максимальная площадь треугольника с основанием p1-p2 и вершиной на выпуклой оболочке"""
    max_area = 0.0
    n = len(convex_hull)
    
    # Используем метод двух указателей или тернарный поиск
    # Для простоты - линейный поиск (можно оптимизировать)
    for p3 in convex_hull:
        if p3 is p1 or p3 is p2:
            continue
        area = triangle_area(p1, p2, p3)
        if area > max_area:
            max_area = area
    
    return max_area
