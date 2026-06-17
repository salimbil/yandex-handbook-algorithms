# Компилятор: Python 3.13.2
def solve():
    import sys
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    
    items = []
    for _ in range(n):
        t = int(data[idx]); idx += 1
        c = int(data[idx]); idx += 1
        items.append((t, c))
    
    T = int(data[idx]); idx += 1
    
    # Сортируем по "эффективности" c/t
    items.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else float('inf'), reverse=True)
    
    total_profit = 0
    remaining_time = T
    
    for t, c in items:
        if t <= remaining_time:
            total_profit += c
            remaining_time -= t
    
    print(total_profit)

if __name__ == "__main__":
    solve()
