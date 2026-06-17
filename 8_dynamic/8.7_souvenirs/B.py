# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    vals = list(map(int, input().split()))
    total = sum(vals)
    
    if total % 3 != 0:
        print("0 0 0")
        print()
        print()
        print()
        return
    
    target = total // 3
    
    # Перебираем маски для первой группы
    for mask1 in range(1 << n):
        sum1 = 0
        for i in range(n):
            if mask1 >> i & 1:
                sum1 += vals[i]
        if sum1 != target:
            continue
        
        # Оставшиеся предметы
        remaining = []
        for i in range(n):
            if not (mask1 >> i & 1):
                remaining.append(i)
        
        m = len(remaining)
        # Перебираем маски для второй группы среди оставшихся
        for mask2 in range(1 << m):
            sum2 = 0
            for j in range(m):
                if mask2 >> j & 1:
                    sum2 += vals[remaining[j]]
            if sum2 != target:
                continue
            
            # Нашли разбиение
            group1 = [i+1 for i in range(n) if mask1 >> i & 1]
            group2 = [remaining[j]+1 for j in range(m) if mask2 >> j & 1]
            group3 = [i+1 for i in range(n) if not (mask1 >> i & 1) and i not in set(remaining[j] for j in range(m) if mask2 >> j & 1)]
            
            print(len(group1), len(group2), len(group3))
            print(' '.join(map(str, group1)))
            print(' '.join(map(str, group2)))
            print(' '.join(map(str, group3)))
            return
    
    # Если не нашли
    print("0 0 0")
    print()
    print()
    print()

if __name__ == "__main__":
    solve()
