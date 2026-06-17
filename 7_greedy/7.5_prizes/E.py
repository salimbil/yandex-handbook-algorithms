# Компилятор: Python 3.13.2
def solve():
    n, D = map(int, input().split())

    if D == 0:
        print(n)
        return

    # Бинарный поиск по k
    lo, hi = 1, n + 1  # грубая верхняя граница
    while lo <= hi:
        mid = (lo + hi) // 2
        # минимальная сумма для mid элементов
        min_sum = mid + D * mid * (mid - 1) // 2
        if min_sum <= n:
            lo = mid + 1
        else:
            hi = mid - 1

    print(hi)


if __name__ == "__main__":
    solve()
