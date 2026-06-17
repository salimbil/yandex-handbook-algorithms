# Компилятор: Python 3.13.2
n = int(input())
a = list(map(int, input().split()))

# кандидаты могут быть только из первых 3 элементов после сокращения
# используем обобщённый алгоритм Бойера-Мура для поиска 3 кандидатов
candidates = []
counts = []

for x in a:
    found = False
    for i in range(len(candidates)):
        if candidates[i] == x:
            counts[i] += 1
            found = True
            break
    if not found and len(candidates) < 3:
        candidates.append(x)
        counts.append(1)
    elif not found:
        for i in range(len(candidates)):
            counts[i] -= 1
            if counts[i] == 0:
                candidates.pop(i)
                counts.pop(i)
                break

# теперь кандидаты — возможные элементы, встречающиеся > n/4 раз
# проверим их реальную частоту
threshold = n // 4
cnt = [0] * len(candidates)
for x in a:
    for i, cand in enumerate(candidates):
        if x == cand:
            cnt[i] += 1

# считаем, сколько кандидатов превышают порог
good = sum(1 for c in cnt if c > threshold)
print(1 if good >= 3 else 0)
