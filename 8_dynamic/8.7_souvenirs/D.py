# Компилятор: Python 3.13.2
n = int(input())
v = list(map(int, input().split()))
total = sum(v)

states = {(0, 0)}
for x in v:
    new_states = set()
    for s1, s2 in states:
        if s1 + x <= total:
            new_states.add((s1 + x, s2))
        if s2 + x <= total:
            new_states.add((s1, s2 + x))
        # третья группа получится сама
        new_states.add((s1, s2))
    states = new_states

best = total
for s1, s2 in states:
    s3 = total - s1 - s2
    diff = max(s1, s2, s3) - min(s1, s2, s3)
    if diff < best:
        best = diff
        if best == 0:
            break

print(best)
