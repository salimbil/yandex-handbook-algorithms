# Компилятор: Python 3.13.2
import sys

def main():
    # Быстрое чтение всех входных данных
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Строим список смежности для представления дорог
    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
        
    # Массив для отслеживания посещенных городов
    visited = [False] * (n + 1)
    
    island_count = 0      # Всего островов
    max_island_size = 0   # Максимальный размер острова
    
    # Проходим по всем городам от 1 до n
    for city in range(1, n + 1):
        if not visited[city]:
            # Нашли новый остров
            island_count += 1
            current_island_size = 0
            
            # Запускаем BFS для подсчета размера текущего острова
            queue = [city]
            visited[city] = True
            head = 0
            
            while head < len(queue):
                current = queue[head]
                head += 1
                current_island_size += 1
                
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            # Обновляем максимальный размер острова
            if current_island_size > max_island_size:
                max_island_size = current_island_size
                
    # Выводим результат
    print(island_count)
    print(max_island_size)

if __name__ == '__main__':
    main()
