# Компилятор: Python 3.13.2
import sys

def main():
    input = sys.stdin.read().split()
    index = 0
    n = int(input[index])
    M = int(input[index + 1])
    index += 2

    sensors = []
    for _ in range(n):
        b = int(input[index])
        m = int(input[index + 1])
        index += 2
        sensors.append((b, m))

    # Сортируем по убыванию удельной пользы
    sensors.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_memory = 0
    total_benefit = 0

    for benefit, memory in sensors:
        if total_memory + memory <= M:
            total_memory += memory
            total_benefit += benefit

    print(total_benefit)

if __name__ == "__main__":
    main()
