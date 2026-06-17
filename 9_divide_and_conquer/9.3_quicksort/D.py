# Компилятор: Python 3.13.2
import random
import sys

def quickselect(arr, k):
    # k — 1-индексация
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(equal))

def solve():
    data = sys.stdin.read().strip().split()
    n, k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2+n]))
    result = quickselect(arr, k)
    print(result)

if __name__ == "__main__":
    solve()
