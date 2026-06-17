# Компилятор: Python 3.13.2
import sys

def max_ad_profit(n, k, w, advertisers):
    # Сортируем рекламодателей по убыванию стоимости за неделю
    advertisers.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0
    slots_available = n * w  # Общее количество слотов (билборды × недели)

    for c, max_weeks in advertisers:
        if slots_available <= 0:
            break

        # Берём минимальное из: сколько хочет рекламодатель и сколько осталось слотов
        weeks_to_use = min(max_weeks, slots_available)
        total_profit += weeks_to_use * c
        slots_available -= weeks_to_use

    return total_profit

def main():
    input = sys.stdin.read().splitlines()
    n, k, w = map(int, input[0].split())
    advertisers = []

    for i in range(1, k + 1):
        c, max_weeks = map(int, input[i].split())
        advertisers.append((c, max_weeks))

    result = max_ad_profit(n, k, w, advertisers)
    print(result)

if __name__ == "__main__":
    main()
