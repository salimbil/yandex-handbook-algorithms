# Компилятор: Python 3.13.2
def can_partition_three(values, target):
    """Проверяет, можно ли разбить values на три подмножества с суммой target"""
    if not values:
        return False

    # Сортируем по убыванию для оптимизации
    values.sort(reverse=True)
    if values[0] > target:
        return False

    # Три корзины
    bins = [0, 0, 0]

    def backtrack(idx):
        if idx == len(values):
            return bins[0] == bins[1] == bins[2] == target

        for i in range(3):
            if bins[i] + values[idx] <= target:
                bins[i] += values[idx]
                if backtrack(idx + 1):
                    return True
                bins[i] -= values[idx]
            # Оптимизация: если корзина пустая, не пробуем другие пустые
            if bins[i] == 0:
                break
        return False

    return backtrack(0)

def min_discarded(n, values):
    best_kept = -1  # максимальное число сохранённых сувениров

    # Перебираем все подмножества через битовые маски
    for mask in range(1, 1 << n):  # начинаем с 1 (непустое подмножество)
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(values[i])

        total = sum(subset)
        if total % 3 != 0:
            continue

        target = total // 3
        if can_partition_three(subset[:], target):  # передаём копию
            best_kept = max(best_kept, len(subset))

    if best_kept == -1:
        return -1
    else:
        return n - best_kept

def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    values = list(map(int, input[1:n + 1]))

    result = min_discarded(n, values)
    print(result)

if __name__ == "__main__":
    main()
