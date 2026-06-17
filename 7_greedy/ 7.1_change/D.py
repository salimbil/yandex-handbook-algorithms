# Компилятор: Python 3.13.2
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    
    coins = []
    for _ in range(n):
        c = int(data[idx]); idx += 1
        f = int(data[idx]); idx += 1
        coins.append((c, f))
    
    S = int(data[idx]); idx += 1
    
    # Сортируем по убыванию эффективности c/f
    # Чтобы избежать деления, сравниваем a.c * b.f > b.c * a.f
    coins.sort(key=lambda x: (-(x[0] * 1.0 / x[1]), x[0]))
    # Второй ключ для стабильности, но необязателен,
    # так как номиналы разные, эффективности одинаковой быть не может
    
    remaining = S
    total_fee = 0
    
    for c, f in coins:
        if remaining == 0:
            break
        # Сколько монет этого типа можно взять
        cnt = remaining // c
        if cnt > 0:
            remaining -= cnt * c
            total_fee += cnt * f
    
    if remaining > 0:
        print(-1)
    else:
        print(total_fee)

if __name__ == "__main__":
    solve()
