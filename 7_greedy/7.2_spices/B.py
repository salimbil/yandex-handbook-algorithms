# Компилятор: Python 3.13.2
import sys

def max_souvenirs(n, S, prices):
    # Сортируем цены по возрастанию
    prices.sort()

    count = 0
    spent = 0

    for price in prices:
        # Если можем купить этот сувенир, покупаем его
        if spent + price <= S:
            count += 1
            spent += price
        else:
            # Дальше цены только больше, смысла продолжать нет
            break

    return count

def main():
    input = sys.stdin.read().splitlines()
    n, S = map(int, input[0].split())
    prices = []

    for i in range(1, n + 1):
        prices.append(int(input[i]))

    result = max_souvenirs(n, S, prices)
    print(result)

if __name__ == "__main__":
    main()
