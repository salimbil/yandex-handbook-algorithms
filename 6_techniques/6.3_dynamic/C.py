# Компилятор: Python 3.13.2
MOD = 10**9 + 7

def matmul(A, B):
    K = len(A)
    C = [[0]*K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            s = 0
            for k in range(K):
                s = (s + A[i][k] * B[k][j]) % MOD
            C[i][j] = s
    return C

def matpow(M, power):
    K = len(M)
    result = [[int(i == j) for j in range(K)] for i in range(K)]
    while power:
        if power & 1:
            result = matmul(result, M)
        M = matmul(M, M)
        power >>= 1
    return result

def solve():
    N = int(input().strip())
    if N == 0:
        print(0)
        return
    if N == 1:
        print(1)
        return
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    
    # Матрица перехода 4x4
    T = [
        [1, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]
    
    # Вектор начальных состояний: [f(4), f(3), f(2), f(1)]
    # f(4) = f(3)+f(1)+f(0) = 2+1+0 = 3
    init = [3, 2, 1, 1]
    
    power = N - 4
    Tn = matpow(T, power)
    
    # Результат: первая компонента
    res = 0
    for i in range(4):
        res = (res + Tn[0][i] * init[i]) % MOD
    print(res)

if __name__ == "__main__":
    solve()
