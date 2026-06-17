# Компилятор: Python 3.11
n = int(input())

def generate(remaining, max_val, current):
    if remaining == 0:
        print('+'.join(map(str, current)))
        return
    
    for i in range(min(max_val, remaining), 0, -1):
        generate(remaining - i, i, current + [i])

generate(n, n, [])
