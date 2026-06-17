# Компилятор: Python 3.11
import heapq
from collections import defaultdict

def solve():
    n, m, K = map(int, input().split())
    
    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    
    INF = float('inf')
    
    def dijkstra(start):
        dist = [INF] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, v = heapq.heappop(pq)
            if d > dist[v]:
                continue
            for to, w in graph[v]:
                if dist[v] + w < dist[to]:
                    dist[to] = dist[v] + w
                    heapq.heappush(pq, (dist[to], to))
        return dist
    
    distX = dijkstra(X)
    distY = dijkstra(Y)
    
    shortest_path = distX[Y]
    
    if shortest_path == INF:
        print(-1)
        return
    
    # Находим минимальный цикл, доступный на кратчайшем пути
    min_cycle = INF
    for u, v, w in edges:
        # Цикл через ребро (u,v) с возвратом
        if distX[u] != INF and distY[v] != INF:
            cycle_len = distX[u] + w + distY[v] - shortest_path
            if cycle_len > 0 and cycle_len < min_cycle:
                min_cycle = cycle_len
        if distX[v] != INF and distY[u] != INF:
            cycle_len = distX[v] + w + distY[u] - shortest_path
            if cycle_len > 0 and cycle_len < min_cycle:
                min_cycle = cycle_len
    
    # Также ищем циклы в одной вершине (петли через соседей)
    for v in range(n):
        if distX[v] != INF and distY[v] != INF and distX[v] + distY[v] == shortest_path:
            # v на кратчайшем пути
            for to, w in graph[v]:
                if distX[to] != INF and distY[to] != INF:
                    cycle_len = w * 2  # v -> to -> v
                    if cycle_len < min_cycle:
                        min_cycle = cycle_len
    
    if shortest_path >= K:
        # Путь уже подходит, восстанавливаем кратчайший
        path = restore_path(X, Y, distX, graph)
        print(len(path))
        print(' '.join(str(v+1) for v in path))
        return
    
    if min_cycle == INF:
        print(-1)
        return
    
    # Сколько раз нужно пройти цикл
    need = K - shortest_path
    times = (need + min_cycle - 1) // min_cycle
    
    # Теперь нужно построить путь
    # Находим вершину и ребро для цикла
    cycle_vertex = -1
    cycle_neighbor = -1
    cycle_weight = -1
    
    for u, v, w in edges:
        if distX[u] != INF and distY[v] != INF:
            cycle_len = distX[u] + w + distY[v] - shortest_path
            if cycle_len == min_cycle:
                cycle_vertex = u
                cycle_neighbor = v
                cycle_weight = w
                break
        if distX[v] != INF and distY[u] != INF:
            cycle_len = distX[v] + w + distY[u] - shortest_path
            if cycle_len == min_cycle:
                cycle_vertex = v
                cycle_neighbor = u
                cycle_weight = w
                break
    
    if cycle_vertex == -1:
        # Ищем цикл v -> to -> v
        for v in range(n):
            if distX[v] != INF and distY[v] != INF and distX[v] + distY[v] == shortest_path:
                for to, w in graph[v]:
                    if 2 * w == min_cycle:
                        cycle_vertex = v
                        cycle_neighbor = to
                        cycle_weight = w
                        break
                if cycle_vertex != -1:
                    break
    
    # Восстанавливаем путь
    # 1. Путь от X до cycle_vertex
    path_to_cycle = []
    curr = cycle_vertex
    while curr != X:
        path_to_cycle.append(curr)
        for prev, w in graph[curr]:
            if distX[prev] + w == distX[curr]:
                curr = prev
                break
    path_to_cycle.append(X)
    path_to_cycle.reverse()
    
    # 2. Путь от cycle_vertex до Y
    path_from_cycle = []
    curr = cycle_vertex
    while curr != Y:
        for next_v, w in graph[curr]:
            if distY[curr] == w + distY[next_v]:
                path_from_cycle.append(curr)
                curr = next_v
                break
    path_from_cycle.append(Y)
    
    # 3. Собираем полный путь с циклами
    full_path = path_to_cycle.copy()
    cycle = [cycle_vertex, cycle_neighbor, cycle_vertex]
    
    for _ in range(times):
        full_path.extend(cycle[1:])  # добавляем cycle_neighbor, cycle_vertex
    
    full_path.extend(path_from_cycle[1:])  # пропускаем cycle_vertex, он уже есть
    
    print(len(full_path))
    print(' '.join(str(v+1) for v in full_path))

def restore_path(X, Y, dist, graph):
    path = []
    curr = Y
    while curr != X:
        path.append(curr)
        for prev, w in graph[curr]:
            if dist[prev] + w == dist[curr]:
                curr = prev
                break
    path.append(X)
    path.reverse()
    return path

solve()
