# Компилятор: Python 3.13.2
from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    freq = Counter(arr)
    min_freq = min(freq.values())
    
    for num, cnt in freq.items():
        if cnt == min_freq:
            print(num)
            return

if __name__ == "__main__":
    solve()
