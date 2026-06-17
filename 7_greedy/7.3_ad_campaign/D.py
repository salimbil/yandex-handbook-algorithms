# Компилятор: Python 3.13.2
import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    tasks = []
    max_deadline = 0
    
    for _ in range(n):
        d = int(next(it))
        p = int(next(it))
        tasks.append((d, p))
        max_deadline = max(max_deadline, d)
    
    # Сортируем задачи по убыванию прибыли
    tasks.sort(key=lambda x: x[1], reverse=True)
    
    # DSU для поиска последнего свободного дня
    parent = list(range(max_deadline + 1))  # parent[day] — следующий возможный день
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px = find(x)
        py = find(y)
        if px != py:
            parent[px] = py
    
    total_profit = 0
    taken_days = [False] * (max_deadline + 1)
    
    for deadline, profit in tasks:
        # Находим последний свободный день <= deadline
        day = find(deadline)
        if day > 0 and not taken_days[day]:
            taken_days[day] = True
            total_profit += profit
            # Объединяем день day с day-1
            union(day, day - 1)
    
    print(total_profit)

if __name__ == "__main__":
    solve()
