# Компилятор: Python 3.13.2
def solve():
    n, k = map(int, input().split())

    q = n // k
    r = n % k

    result = [q + 1] * r + [q] * (k - r)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()
