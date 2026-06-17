# Компилятор: Python 3.11
from itertools import permutations

N, M = map(int, input().split())
digits = list(map(int, input().split()))

# Перебираем все перестановки в лексикографическом порядке
for perm in permutations(sorted(digits)):
    # Составляем число из цифр
    num = 0
    for d in perm:
        num = num * 10 + d
    
    if num % M == 0:
        print(''.join(map(str, perm)))
        break
else:
    print("No solutions")
