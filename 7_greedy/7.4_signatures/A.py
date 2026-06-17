# Компилятор: Python 3.13.2
def solve():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    segments = []
    for _ in range(n):
        l = int(next(it))
        r = int(next(it))
        segments.append((l, r))

    # Сортируем по правому концу
    segments.sort(key=lambda x: x[1])

    points = []
    last_point = -1

    for l, r in segments:
        # Если последняя выбранная точка не покрывает текущий отрезок
        if last_point < l:
            # Выбираем правый конец текущего отрезка
            last_point = r
            points.append(last_point)

    # Вывод
    print(len(points))
    print(' '.join(map(str, points)))


if __name__ == "__main__":
    solve()
