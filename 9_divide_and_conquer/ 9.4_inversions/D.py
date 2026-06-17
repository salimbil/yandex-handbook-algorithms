# Компилятор: Python 3.13.2
def count_inversions(arr):
    # arr — массив значений, нужно посчитать инверсии стандартным mergesort
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = merge_sort(a[:mid])
        right, inv_r = merge_sort(a[mid:])
        merged = []
        i = j = 0
        inv = inv_l + inv_r
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv
    
    _, inv = merge_sort(arr)
    return inv

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i, val in enumerate(p):
        pos[val] = i  # 0-индексация
    
    # Считаем инверсии между p и [1..n] (это просто инверсии в p)
    inv0 = count_inversions(p)
    
    best = inv0
    
    # Переход от target[x] к target[x+1]
    # inv[x+1] = inv[x] + (n - 1 - pos[x]) - pos[x]
    # потому что x переезжает из pos[x] в конец (индекс n-1)
    inv = inv0
    for x in range(1, n):
        # из target[x] → target[x+1]
        inv = inv + (n - 1 - pos[x]) - pos[x]
        if inv < best:
            best = inv
    
    print(best)

if __name__ == "__main__":
    solve()
