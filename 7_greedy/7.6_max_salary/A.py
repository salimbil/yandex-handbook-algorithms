# Компилятор: Python 3.13.2
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

n = int(input())
numbers = input().split()

# Сортируем с помощью нашего компаратора
numbers.sort(key=cmp_to_key(compare))

# Собираем результат
result = ''.join(numbers)

# Если результат состоит только из нулей, выводим один ноль
if result[0] == '0':
    print('0')
else:
    print(result)
