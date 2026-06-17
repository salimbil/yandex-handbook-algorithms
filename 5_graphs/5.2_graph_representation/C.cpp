// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int g;
    if (!(std::cin >> g)) return 0;

    // Так как n <= 100, заведем матрицу с запасом (105 x 105), заполненную нулями
    std::vector<std::vector<int>> adj(105, std::vector<int>(105, 0));
    int max_n = 0; // Для поиска максимального идентификатора (размера графа n)

    for (int i = 0; i < g; ++i) {
        int k;
        std::cin >> k;
        std::vector<int> group(k);
        for (int j = 0; j < k; ++j) {
            std::cin >> group[j];
            if (group[j] > max_n) {
                max_n = group[j]; // Обновляем максимальный ID человека
            }
        }

        // Связываем каждого с каждым внутри текущей группы
        for (int j = 0; j < k; ++j) {
            for (int l = j + 1; l < k; ++l) {
                int u = group[j];
                int v = group[l];
                adj[u][v] = 1;
                adj[v][u] = 1;
            }
        }
    }

    // Выводим размер графа n
    std::cout << max_n << "\n";

    // Выводим матрицу смежности размера max_n x max_n (используем 1-индексацию)
    for (int i = 1; i <= max_n; ++i) {
        for (int j = 1; j <= max_n; ++j) {
            std::cout << adj[i][j] << (j == max_n ? "" : " ");
        }
        std::cout << "\n";
    }

    return 0;
}
