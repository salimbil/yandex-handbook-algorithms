# Компилятор: Python 3.13.2
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    # Создаём таблицу dp размером (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Инициализируем базовые случаи
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Заполняем таблицу dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # удаление
                dp[i][j - 1] + 1,      # вставка
                dp[i - 1][j - 1] + cost  # замена/совпадение
            )

    return dp[m][n]

def main():
    s1 = input().strip()
    s2 = input().strip()
    result = edit_distance(s1, s2)
    print(result)

if __name__ == "__main__":
    main()
