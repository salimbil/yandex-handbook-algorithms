# Компилятор: Python 3.13.2
def solve():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    total = n * m
    candidate = None
    count = 0
    
    for i in range(n):
        for j in range(m):
            x = matrix[i][j]
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1
    
    # Проверка
    freq = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == candidate:
                freq += 1
    
    if freq > total // 2:
        print(candidate)
    else:
        print(-1)

if __name__ == "__main__":
    solve()
