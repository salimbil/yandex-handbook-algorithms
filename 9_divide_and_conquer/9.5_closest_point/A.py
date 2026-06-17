# Компилятор: Python 3.13.2
import math
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    # Чтение количества точек
    n = int(data[0])
    
    # Сохраняем исходный индекс для стабильности сортировки
    points = []
    for i in range(n):
        x = int(data[1 + 2*i])
        y = int(data[2 + 2*i])
        points.append((x, y, i))

    # Сортировка по X, затем по Y для детерминированности
    points.sort(key=lambda p: (p[0], p[1]))

    def dist_sq(p1, p2):
        """Возвращает квадрат евклидова расстояния между двумя точками."""
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return dx*dx + dy*dy

    def brute_force(pts):
        """Находит минимальное расстояние прямым перебором для |pts| <= 3."""
        min_d_sq = float('inf')
        m = len(pts)
        for i in range(m):
            for j in range(i+1, m):
                d_sq = dist_sq(pts[i], pts[j])
                if d_sq < min_d_sq:
                    min_d_sq = d_sq
        return min_d_sq

    def closest_pair_rec(px):
        """
        Рекурсивная функция для поиска ближайшей пары.
        px - список точек, отсортированный по X.
        Возвращает минимальный квадрат расстояния.
        """
        num_points = len(px)
        
        # Базовый случай: 2 или 3 точки
        if num_points <= 3:
            return brute_force(px)

        # Разделение множества на две половины
        mid = num_points // 2
        left_px = px[:mid]
        right_px = px[mid:]
        mid_point = px[mid]
        mid_x = mid_point[0]

        # Поиск минимума в левой и правой частях
        dl = closest_pair_rec(left_px)
        dr = closest_pair_rec(right_px)
        delta_sq = min(dl, dr)

        # Если все точки в одной половине совпадают, дальнейшее деление бессмысленно
        if delta_sq == 0:
            return 0.0

        # Формирование полосы (strip) из точек, близких к разделяющей прямой
        strip = [point for point in px if (point[0] - mid_x)**2 <= delta_sq]

        # Сортировка полосы по координате Y
        strip.sort(key=lambda p: p[1])

        # Проверка точек в полосе
        strip_len = len(strip)
        for i in range(strip_len):
            # Достаточно проверить следующие 7 точек
            for j in range(i+1, min(i+8, strip_len)):
                # Оптимизация: сравниваем квадраты координат Y
                dy = strip[j][1] - strip[i][1]
                if dy*dy > delta_sq:
                    break
                
                d_sq = dist_sq(strip[i], strip[j])
                if d_sq < delta_sq:
                    delta_sq = d_sq

        return delta_sq

    # Запуск рекурсии
    min_dist_sq = closest_pair_rec(points)

    # Вычисление финального расстояния и вывод с точностью 6 знаков
    distance = math.sqrt(min_dist_sq)
    print(f"{distance:.6f}")

if __name__ == "__main__":
    solve()
