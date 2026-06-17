# Компилятор: Python 3.13.2
def solve():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    T = int(next(it))

    processes = []
    for _ in range(n):
        w = int(next(it))
        c = int(next(it))
        processes.append((w, c))

    # Сортируем по убыванию плотности прибыли (c / w)
    processes.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0.0
    remaining_time = T

    for w, c in processes:
        if remaining_time <= 0:
            break
        if w <= remaining_time:
            # Берём процесс целиком
            total_profit += c
            remaining_time -= w
        else:
            # Берём только часть процесса
            fraction = remaining_time / w
            total_profit += c * fraction
            remaining_time = 0

    # Выводим с нужной точностью
    print(f"{total_profit:.6f}")

if __name__ == "__main__":
    solve()
