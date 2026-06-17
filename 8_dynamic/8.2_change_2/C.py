# Компилятор: Python 3.13.2
import sys

MOD = 10**9 + 7

def count_coin_ways(n, S, coins):
    # dp[sum] — количество способов разменять сумму sum
    dp = [0] * (S + 1)
    dp[0] = 1  # один способ получить сумму 0

    # Обрабатываем каждый номинал монеты
    for coin in coins:
        # Перебираем суммы от coin до S (прямой порядок)
        for current_sum in range(coin, S + 1):
            # Обновляем количество способов
            dp[current_sum] = (dp[current_sum] + dp[current_sum - coin]) % MOD

    return dp[S]

def main():
    input = sys.stdin.read().split()
    index = 0
    n = int(input[index])
    S = int(input[index + 1])
    index += 2

    coins = list(map(int, input[index:index + n]))

    result = count_coin_ways(n, S, coins)
    print(result)

if __name__ == "__main__":
    main()
