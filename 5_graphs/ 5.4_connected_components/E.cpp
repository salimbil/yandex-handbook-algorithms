// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

// 8 направлений движения (включая диагонали)
const int dr[] = {-1, -1, -1,  0, 0,  1, 1, 1};
const int dc[] = {-1,  0,  1, -1, 1, -1, 0, 1};

int main() {
    // Максимальное ускорение ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    bool global_has_portal = false;

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        if (!global_has_portal) {
            for (char ch : grid[i]) {
                if (ch == '@') {
                    global_has_portal = true;
                }
            }
        }
    }

    int components_with_towns_and_portal = 0;
    int components_with_towns_no_portal = 0;
    int total_towns = 0;

    queue<int> q;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            // Если клетка — город, дорога или портал, запускаем BFS
            if (grid[r][c] == '#' || grid[r][c] == 'X' || grid[r][c] == '@') {
                bool has_town = false;
                bool has_portal = false;

                if (grid[r][c] == 'X') has_town = true;
                if (grid[r][c] == '@') has_portal = true;

                grid[r][c] = '.'; // Помечаем как посещенную
                q.push(r * m + c);

                while (!q.empty()) {
                    int encoded = q.front();
                    q.pop();

                    int curr_r = encoded / m;
                    int curr_c = encoded % m;

                    for (int i = 0; i < 8; ++i) {
                        int nr = curr_r + dr[i];
                        int nc = curr_c + dc[i];

                        if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                            char cell = grid[nr][nc];
                            if (cell == '#' || cell == 'X' || cell == '@') {
                                if (cell == 'X') has_town = true;
                                if (cell == '@') has_portal = true;
                                
                                grid[nr][nc] = '.'; // Стираем клетку
                                q.push(nr * m + nc);
                            }
                        }
                    }
                }

                // Учитываем только компоненты, в которых реально есть города
                if (has_town) {
                    total_towns++;
                    if (has_portal) {
                        components_with_towns_and_portal++;
                    } else {
                        components_with_towns_no_portal++;
                    }
                }
            }
        }
    }

    // Если городов нет, они "связаны" автоматически
    if (total_towns == 0) {
        cout << "YES\n";
        return 0;
    }

    // Общее количество изолированных друг от друга групп городов
    int total_components_with_towns = components_with_towns_and_portal + components_with_towns_no_portal;

    // СЛУЧАЙ 1: Все города оказались в одной единственной связной группе
    // Порталы вообще не нужны (даже если их изначально не было в этой группе)
    if (total_components_with_towns == 1 && components_with_towns_no_portal == 1) {
        cout << "YES\n";
        return 0;
    }

    // СЛУЧАЙ 2: Все группы городов уже имеют внутри себя хотя бы по одному порталу
    // Они все автоматически связаны через глобальную портальную сеть
    if (components_with_towns_no_portal == 0) {
        cout << "YES\n";
        return 0;
    }

    // СЛУЧАЙ 3: Города не связаны, считаем минимальное число новых порталов (k)
    int k = 0;
    if (global_has_portal) {
        // Если в мире уже есть порталы (в других компонентах без городов или в части компонент с городами),
        // то каждую "закрытую" компоненту нужно просто подключить к этой сети: +1 портал на каждую.
        k = components_with_towns_no_portal;
    } else {
        // Если порталов в мире вообще не было:
        // Нам нужно поставить по одному порталу в КАЖДУЮ компоненту с городами,
        // чтобы они с нуля образовали единую общую сеть.
        k = total_components_with_towns;
    }

    cout << "NO " << k << "\n";

    return 0;
}
