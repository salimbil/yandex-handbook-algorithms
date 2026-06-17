# Python 3.11 (PyPy 7.3.19)
n = int(input())
a = list(map(int, input().split()))

stack = []
res = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    if stack:
        res.append(str(i - stack[-1] - 1))
    else:
        res.append(str(i))
    stack.append(i)

print(' '.join(res))
