# Компилятор: Python 3.13.2
def solve():
    n = int(input().strip())

    powers = []
    pos = 0
    while n > 0:
        if n & 1:  # если младший бит равен 1
            powers.append(pos)
        n >>= 1  # сдвигаем вправо (делим на 2)
        pos += 1

    print(len(powers))
    print(' '.join(map(str, powers)))


if __name__ == "__main__":
    solve()
