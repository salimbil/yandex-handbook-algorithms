# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    candidate = None
    count = 0
    
    for x in arr:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    
    # Проверка
    if arr.count(candidate) > n // 2:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()
