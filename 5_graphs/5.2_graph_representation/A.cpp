// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

int main() {
    // Ускорение ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    if (!(std::cin >> n >> m)) return 0;

    // Инициализируем две матрицы смежности нулями
    // Используем vector<vector<int>> или vector<vector<bool>>, int надежнее для вывода
    std::vector<std::vector<int>> graph1(n, std::vector<int>(n, 0));
    std::vector<std::vector<int>> graph2(n, std::vector<int>(n, 0));

    for (int i = 0; i < m; ++i) {
        int k;
        std::cin >> k;
        std::vector<int> route(k);
        for (int j = 0; j < k; ++j) {
            std::cin >> route[j];
            route[j]--; // Переходим к 0-индексации
        }

        // Заполняем первый граф (соседние остановки)
        for (int j = 0; j < k - 1; ++j) {
            int u = route[j];
            int v = route[j + 1];
            graph1[u][v] = 1;
            graph1[v][u] = 1;
        }

        // Заполняем второй граф (любые пары на одном маршруте)
        for (int j = 0; j < k; ++j) {
            for (int l = j + 1; l < k; ++l) {
                int u = route[j];
                int v = route[l];
                graph2[u][v] = 1;
                graph2[v][u] = 1;
            }
        }
    }

    // Выводим матрицу смежности первого графа
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << graph1[i][j] << (j == n - 1 ? "" : " ");
        }
        std::cout << "\n";
    }

    // Выводим матрицу смежности второго графа
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << graph2[i][j] << (j == n - 1 ? "" : " ");
        }
        std::cout << "\n";
    }

    return 0;
}
