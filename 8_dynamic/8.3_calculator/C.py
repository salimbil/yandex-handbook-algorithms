# Компилятор: Python 3.13.2
import sys
from collections import deque

def min_operations_and_paths(a, b):
    # Ограничиваем верхний предел для оптимизации
    MAX_VAL = b + 3

    # dist[x] — минимальное количество операций для x
    # count[x] — количество оптимальных путей для x
    dist = {}
    count = {}

    # Инициализация
    dist[a] = 0
    count[a] = 1

    queue = deque([a])

    while queue:
        current = queue.popleft()

        # Если достигли цели, можно завершить (все оптимальные пути уже найдены)
        if current == b:
            break

        # Генерируем все возможные следующие числа
        next_values = [
            current + 1,
            current + 2,
            current + 3,
            current * 2,
            current * 3
        ]

        for next_val in next_values:
            # Пропускаем числа вне допустимого диапазона
            if next_val < 1 or next_val > MAX_VAL:
                continue

            # Если это первое посещение next_val
            if next_val not in dist:
                dist[next_val] = dist[current] + 1
                count[next_val] = count[current]
                queue.append(next_val)
            # Если нашли другой путь с тем же количеством операций
            elif dist[next_val] == dist[current] + 1:
                count[next_val] += count[current]

    return dist.get(b, -1), count.get(b, 0)

def main():
    a, b = map(int, sys.stdin.readline().split())
    min_ops, num_paths = min_operations_and_paths(a, b)
    print(min_ops, num_paths)

if __name__ == "__main__":
    main()
