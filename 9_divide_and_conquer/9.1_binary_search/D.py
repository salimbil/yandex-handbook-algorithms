# Компилятор: Python 3.13.2
def can_cover(points, k, L):
    count = 1
    cover_until = points[0] + L
    for p in points:
        if p > cover_until:
            count += 1
            cover_until = p + L
            if count > k:
                return False
    return True

def solve():
    n, k = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort()
    
    if k >= n:
        print(0)
        return
    
    l, r = 0, points[-1] - points[0]
    while l < r:
        mid = (l + r) // 2
        if can_cover(points, k, mid):
            r = mid
        else:
            l = mid + 1
    print(l)

if __name__ == "__main__":
    solve()
