# Компилятор: Python 3.13.2
import sys

def max_weight_purchase(n, items, S):
    # Создаём список с информацией о товарах: (weight, cost, efficiency)
    goods = []

    for w, c in items:
        efficiency = w / c
        goods.append((w, c, efficiency))

    # Сортируем по убыванию эффективности
    goods.sort(key=lambda x: x[2], reverse=True)

    total_weight = 0
    spent = 0

    for w, c, _ in goods:
        # Сколько упаковок этого товара можно купить на оставшиеся деньги
        remaining_budget = S - spent
        if remaining_budget <= 0:
            break

        count = remaining_budget // c
        if count > 0:
            total_weight += count * w
            spent += count * c

    return total_weight

def main():
    input = sys.stdin.read().splitlines()
    n = int(input[0])
    items = []

    for i in range(1, n + 1):
        w, c = map(int, input[i].split())
        items.append((w, c))

    S = int(input[n + 1])

    result = max_weight_purchase(n, items, S)
    print(result)

if __name__ == "__main__":
    main()
