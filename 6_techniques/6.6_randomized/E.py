# Компилятор: Python 3.11
import sys

def stoer_wagner(n, graph):
    vertices = list(range(n))
    min_cut = float('inf')
    
    while len(vertices) > 1:
        # Фаза: находим разрез
        added = [False] * n
        weights = [0] * n
        prev = -1
        
        for _ in range(len(vertices)):
            max_w = -1
            v = -1
            for u in vertices:
                if not added[u] and weights[u] > max_w:
                    max_w = weights[u]
                    v = u
            
            if v == -1:
                break
            
            added[v] = True
            
            if _ == len(vertices) - 1:
                # Последняя добавленная вершина — t, предпоследняя — s
                min_cut = min(min_cut, weights[v])
                
                # Объединяем s и t
                s = prev
                t = v
                
                # Обновляем граф
                for u in vertices:
                    if u != t:
                        graph[s][u] += graph[t][u]
                        graph[u][s] += graph[u][t]
                
                vertices.remove(t)
                break
            
            prev = v
            
            # Обновляем веса
            for u in vertices:
                if not added[u]:
                    weights[u] += graph[v][u]
    
    return min_cut

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    graph[u][v] += 1
    graph[v][u] += 1

print(stoer_wagner(n, graph))
