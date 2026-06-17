# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == q:
            print(mid)
            return
        elif arr[mid] < q:
            l = mid + 1
        else:
            r = mid - 1
    print(-1)

if __name__ == "__main__":
    solve()
