# Компилятор: Python 3.11
import heapq

n = int(input())
L, F = map(int, input().split())

stations = []
for _ in range(n):
    x, a = map(int, input().split())
    stations.append((x, a))

# Сортируем по координате
stations.sort()

# Добавляем финальную точку как заправку с 0 топлива
stations.append((L, 0))

current_fuel = F
prev_pos = 0
stops = 0
heap = []  # max-heap (храним отрицательные значения для max)

for pos, fuel in stations:
    # Расстояние, которое нужно проехать до этой заправки
    distance = pos - prev_pos
    current_fuel -= distance
    
    # Пока топлива не хватает, берём максимум из пройденных заправок
    while current_fuel < 0 and heap:
        current_fuel += -heapq.heappop(heap)
        stops += 1
    
    # Если после всех заправок топлива не хватает — невозможно
    if current_fuel < 0:
        print(-1)
        break
    
    # Добавляем текущую заправку в кучу
    heapq.heappush(heap, -fuel)
    prev_pos = pos
else:
    print(stops)
