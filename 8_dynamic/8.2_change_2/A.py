# Компилятор: Python 3.13.2
import sys

def min_coins(money):
    # Инициализируем массив dp большими значениями
    dp = [float('inf')] * (money + 1)
    # Базовый случай
    dp[0] = 0

    # Номиналы монет
    coins = [1, 3, 4]

    # Заполняем массив dp для всех сумм от 1 до money
    for i in range(1, money + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]

def main():
    money = int(sys.stdin.readline())
    print(min_coins(money))

if __name__ == "__main__":
    main()
