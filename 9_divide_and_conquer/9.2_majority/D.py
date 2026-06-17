# Компилятор: Python 3.13.2
from collections import Counter

def majority_element(arr):
    # Алгоритм Бойера-Мура для поиска кандидата
    candidate = None
    count = 0
    for x in arr:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    # Проверяем, действительно ли кандидат — мода
    freq = Counter(arr)
    max_count = max(freq.values())
    for num, cnt in freq.items():
        if cnt == max_count:
            return num

n = int(input())
a = list(map(int, input().split()))
print(majority_element(a))
