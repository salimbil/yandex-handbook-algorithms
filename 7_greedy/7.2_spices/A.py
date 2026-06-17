# Компилятор: Python 3.13.2
import sys

def max_spice_value(n, W, spices):
    # Вычисляем удельную стоимость и сортируем по убыванию
    spices_with_value = []
    for c, w in spices:
        value_per_pound = c / w
        spices_with_value.append((value_per_pound, c, w))

    # Сортируем по убыванию удельной стоимости
    spices_with_value.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    current_weight = 0

    for value_per_pound, c, w in spices_with_value:
        if current_weight >= W:
            break

        # Сколько можем взять этой специи
        available = w
        remaining_capacity = W - current_weight
        take = min(available, remaining_capacity)

        # Добавляем ценность взятой части
        total_value += take * value_per_pound
        current_weight += take

    return total_value

def main():
    input = sys.stdin.read().splitlines()
    n, W = map(int, input[0].split())
    spices = []

    for i in range(1, n + 1):
        c, w = map(int, input[i].split())
        spices.append((c, w))

    result = max_spice_value(n, W, spices)
    print(f"{result:.4f}")

if __name__ == "__main__":
    main()
