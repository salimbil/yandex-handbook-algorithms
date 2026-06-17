# Компилятор: Python 3.13.2
import sys
import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    m = random.choice(arr)
    small = [x for x in arr if x < m]
    equal = [x for x in arr if x == m]
    large = [x for x in arr if x > m]
    
    return randomized_quick_sort(small) + equal + randomized_quick_sort(large)

def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    sorted_arr = randomized_quick_sort(arr)
    print(' '.join(map(str, sorted_arr)))

if __name__ == "__main__":
    solve()
