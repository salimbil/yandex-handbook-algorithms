# Компилятор: Python 3.13.2
import sys

def main():
    # Быстрое чтение всех входных данных из стандартного ввода
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Строим список смежности для существующих мостов
    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
        
    # Массив для отслеживания посещенных островов
    visited = [False] * (n + 1)
    
    # Сюда будем сохранять по одному острову-представителю от каждой компоненты
    representatives = []
    
    # Обходим все острова от 1 до n
    for island in range(1, n + 1):
        if not visited[island]:
            # Нашли новую изолированную группу, сохраняем её представителя
            representatives.append(island)
            
            # Запускаем BFS, чтобы пометить всю компоненту как посещенную
            queue = [island]
            visited[island] = True
            head = 0
            
            while head < len(queue):
                current = queue[head]
                head += 1
                
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
    # Количество необходимых мостов равно (число компонент - 1)
    k = len(representatives) - 1
    print(k)
    
    # Выводим новые мосты, соединяя представителей «цепочкой»
    for i in range(k):
        print(f"{representatives[i]} {representatives[i+1]}")

if __name__ == '__main__':
    main()
