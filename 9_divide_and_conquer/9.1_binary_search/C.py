# Компилятор: Python 3.13.2
import sys
import bisect

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]; idx += n
    m = int(data[idx]); idx += 1
    queries = [int(data[idx + i]) for i in range(m)]; idx += m
    
    result = []
    for q in queries:
        left = bisect.bisect_left(arr, q)
        right = bisect.bisect_right(arr, q)
        result.append(right - left)
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
