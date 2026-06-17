# Компилятор: Python 3.13.2
def solve():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    dp = [False] * (W + 1)
    dp[0] = True
    prev = [-1] * (W + 1)
    
    for i, w in enumerate(weights):
        if w == 0:
            continue
        for s in range(W, w - 1, -1):
            if dp[s - w] and not dp[s]:
                dp[s] = True
                prev[s] = i  # запоминаем индекс слитка
    
    # Находим максимальный вес
    best_weight = 0
    for s in range(W, -1, -1):
        if dp[s]:
            best_weight = s
            break
    
    # Восстанавливаем ответ
    chosen = []
    cur = best_weight
    while cur > 0:
        idx = prev[cur]
        chosen.append(idx + 1)  # +1 для 1-индексации
        cur -= weights[idx]
    
    # Выводим результат
    print(best_weight)
    if chosen:
        print(' '.join(map(str, sorted(chosen))))
    else:
        print()

if __name__ == "__main__":
    solve()
