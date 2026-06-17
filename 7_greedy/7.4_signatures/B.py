# Компилятор: Python 3.13.2
def solve():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    L = int(data[1])
    points = list(map(int, data[2:2 + n]))

    points.sort()

    count = 0
    i = 0
    while i < n:
        count += 1
        cover_until = points[i] + L
        # Пропускаем все точки, попавшие в этот отрезок
        while i < n and points[i] <= cover_until:
            i += 1

    print(count)


if __name__ == "__main__":
    solve()
