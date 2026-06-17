# Компилятор: Python 3.13.2
import sys

def main():
    input = sys.stdin.read().split()
    index = 0
    n = int(input[index])
    T = int(input[index + 1])
    index += 2
    
    experiments = []
    
    for _ in range(n):
        b = int(input[index])
        p = float(input[index + 1])
        t = int(input[index + 2])
        index += 3
        
        expected_benefit = b * p
        unit_benefit = expected_benefit / t if t > 0 else 0
        experiments.append((unit_benefit, expected_benefit, t))
    
    # Сортируем по убыванию удельной пользы
    experiments.sort(key=lambda x: x[0], reverse=True)
    
    total_time = 0
    total_benefit = 0.0
    
    for unit_benefit, exp_benefit, time in experiments:
        if total_time + time <= T:
            total_time += time
            total_benefit += exp_benefit
    
    print("{0:.6f}".format(total_benefit))

if __name__ == "__main__":
    main()
