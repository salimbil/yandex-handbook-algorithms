# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    vals = list(map(int, input().split()))
    total = sum(vals)
    
    if total % 7 != 0:
        print(0)
        return
    
    k = total // 7
    target1, target2, target3 = k, 2*k, 4*k
    
    for mask in range(3**n):
        s1 = s2 = s3 = 0
        x = mask
        for i in range(n):
            g = x % 3
            x //= 3
            if g == 0:
                s1 += vals[i]
            elif g == 1:
                s2 += vals[i]
            else:
                s3 += vals[i]
        
        if s1 == target1 and s2 == target2 and s3 == target3:
            print(1)
            return
    
    print(0)

if __name__ == "__main__":
    solve()
