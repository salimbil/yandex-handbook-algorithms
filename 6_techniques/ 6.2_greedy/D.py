# Компилятор: Python 3.11
N, M = map(int, input().split())

# Для каждой комнаты массив занятости по минутам (True = занято)
rooms = [[False] * 601 for _ in range(N)]
rejected = 0

for _ in range(M):
    start, duration = map(int, input().split())
    end = start + duration
    
    found = False
    for i in range(N):
        # Проверяем, свободна ли комната i в интервале [start, end)
        free = True
        for t in range(start, end):
            if rooms[i][t]:
                free = False
                break
        
        if free:
            # Бронируем
            for t in range(start, end):
                rooms[i][t] = True
            found = True
            break
    
    if not found:
        rejected += 1

print(rejected)
