# Компилятор: Python 3.13.2
import sys

def main():
    # Быстрое чтение всех входных данных
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    # Читаем размеры сетки
    n, m = map(int, input_data[0].split())
    
    # Считываем саму сетку в виде списка списков символов
    grid = [list(line) for line in input_data[1:n+1]]
    
    colony_count = 0
    max_colony_size = 0
    
    # Направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '#':
                # Нашли новую колонию
                colony_count += 1
                current_size = 0
                
                # Инициализируем BFS-очередь (храним координаты клеток)
                queue = [(r, c)]
                grid[r][c] = '.'  # Помечаем стартовую клетку как посещенную
                
                head = 0
                while head < len(queue):
                    curr_r, curr_c = queue[head]
                    head += 1
                    current_size += 1
                    
                    # Проверяем всех 4-х соседей
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # Проверка границ сетки и наличия бактерии
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '#':
                            grid[nr][nc] = '.'  # Помечаем сразу при добавлении в очередь
                            queue.append((nr, nc))
                
                # Обновляем размер самой большой колонии
                if current_size > max_colony_size:
                    max_colony_size = current_size
                    
    # Вывод результатов
    print(colony_count)
    print(max_colony_size)

if __name__ == '__main__':
    main()
