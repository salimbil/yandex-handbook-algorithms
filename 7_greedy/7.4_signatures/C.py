# Компилятор: Python 3.13.2
def solve():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    points = list(map(int, data[2:2 + n]))

    if k >= n:
        print(0)
        return

    points.sort()

    # Вычисляем разницы между соседними точками
    diffs = [points[i + 1] - points[i] for i in range(n - 1)]

    # Сортируем разницы по убыванию
    diffs.sort(reverse=True)

    # Суммарная длина при 1 отрезке
    total_length = points[-1] - points[0]

    # Пропускаем k-1 самых больших промежутков
    # (потому что k отрезков создают k-1 промежутков между группами)
    for i in range(min(k - 1, len(diffs))):
        total_length -= diffs[i]

    print(total_length)


if __name__ == "__main__":
    solve()
