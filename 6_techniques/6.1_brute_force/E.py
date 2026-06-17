# Компилятор: Python 3.11
from itertools import combinations

N, P, K = map(int, input().split())
w = list(map(int, input().split()))

# Списки совместимости клиентов
clients = []
for _ in range(P):
    data = list(map(int, input().split()))
    t = data[0]
    servers = [x - 1 for x in data[1:]]
    clients.append(servers)

best_sum = float('inf')
best_combo = None

# Перебираем все сочетания из K серверов
for combo in combinations(range(N), K):
    # Проверяем, что каждый клиент совместим хотя бы с одним сервером
    ok = True
    for client_servers in clients:
        if not any(s in combo for s in client_servers):
            ok = False
            break
    
    if ok:
        total_delay = sum(w[i] for i in combo)
        if total_delay < best_sum:
            best_sum = total_delay
            best_combo = combo

if best_combo is None:
    print("No solutions")
else:
    print(best_sum)
    print(' '.join(str(x + 1) for x in best_combo))
