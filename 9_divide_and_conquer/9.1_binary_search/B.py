# Компилятор: Python 3.13.2
def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def solve():
    n = int(input())
    K = list(map(int, input().split()))
    m = int(input())
    Q = list(map(int, input().split()))
    
    for q in Q:
        print(binary_search(K, q))

if __name__ == "__main__":
    solve()
