// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    if (!(std::cin >> n >> m)) return 0;

    std::vector<std::string> grid(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> grid[i];
    }

    int r, c;
    std::cin >> r >> c;
    r--; c--; // Перевод к 0-индексации

    int q;
    std::cin >> q;
    std::string commands;
    std::cin >> commands;

    // Массивы смещений для направлений: 0 - Вверх, 1 - Вправо, 2 - Вниз, 3 - Влево
    // Порядок по часовой стрелке упрощает повороты
    int dr[] = {-1, 0, 1, 0};
    int dc[] = {0, 1, 0, -1};
    int dir = 0; // Изначально робот повернут вверх

    // Матрица для отслеживания посещенных клеток
    std::vector<std::vector<bool>> visited(n, std::vector<bool>(m, false));
    
    // Отмечаем стартовую клетку
    visited[r][c] = true;
    int unique_visited_count = 1;

    for (char cmd : commands) {
        if (cmd == 'R') {
            dir = (dir + 1) % 4;
        } else if (cmd == 'L') {
            dir = (dir + 3) % 4; // Эквивалентно (dir - 1 + 4) % 4
        } else if (cmd == 'M') {
            int next_r = r + dr[dir];
            int next_c = c + dc[dir];

            // Проверяем, что следующая клетка внутри поля и не является препятствием
            if (next_r >= 0 && next_r < n && next_c >= 0 && next_c < m && grid[next_r][next_c] != '#') {
                r = next_r;
                c = next_c;
                // Если клетка еще не была посещена, учитываем её
                if (!visited[r][c]) {
                    visited[r][c] = true;
                    unique_visited_count++;
                }
            }
        }
    }

    std::cout << unique_visited_count << "\n";

    return 0;
}
