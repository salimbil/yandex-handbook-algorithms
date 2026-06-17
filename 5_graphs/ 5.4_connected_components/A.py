# Компилятор: Python 3.13.2
import sys

# Увеличиваем лимит рекурсии на случай использования DFS (для BFS это необязательно, но полезно)
sys.setrecursionlimit(300000)

def main():
    # Быстрый ввод данных
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    
    # Если город всего один, склад всегда можно открыть
    if n == 1:
        print("YES")
        return

    # Строим список смежности для графа
    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2

    # Булев массив для отслеживания посещенных городов
    visited = [False] * (n + 1)
    
    # Запускаем обход (BFS) из первого города
    queue = [1]
    visited[1] = True
    visited_count = 1
    
    head = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                visited_count += 1

    # Если мы смогли посетить все n городов, значит граф связный
    if visited_count == n:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
