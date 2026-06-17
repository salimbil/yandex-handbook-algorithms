# Компилятор: Python 3.13.2
def solve():
    import sys
    import bisect

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    L = int(next(it))

    houses = [int(next(it)) for _ in range(n)]
    sensors = [int(next(it)) for _ in range(m)]

    houses.sort()
    sensors.sort()

    i = 0  # индекс текущего непокрытого дома
    j = 0  # индекс датчика
    count = 0

    while i < n:
        # Ищем датчик, который может покрыть houses[i]
        # Датчик должен быть в [houses[i] - L, houses[i] + L]
        # Пропускаем датчики, которые расположены слишком далеко слева
        while j < m and sensors[j] < houses[i] - L:
            j += 1

        if j >= m or sensors[j] > houses[i] + L:
            # Нет подходящего датчика
            print(-1)
            return

        # Среди всех датчиков, покрывающих houses[i], выбираем самый правый
        best_index = j
        while j + 1 < m and sensors[j + 1] <= houses[i] + L:
            j += 1
            best_index = j

        # Выбран датчик sensors[best_index]
        count += 1
        cover_until = sensors[best_index] + L

        # Перемещаем i на первый непокрытый дом
        while i < n and houses[i] <= cover_until:
            i += 1

        # j увеличивать не нужно, так как мы уже на позиции последнего рассмотренного датчика
        # но при следующей итерации while j < m and sensors[j] < houses[i] - L сделает коррекцию

    print(count)


if __name__ == "__main__":
    solve()
