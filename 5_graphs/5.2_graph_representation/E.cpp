// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    if (!(std::cin >> n)) return 0;

    // Считываем матрицу смежности (она же будет начальной матрицей достижимости)
    std::vector<std::vector<int>> R(n, std::vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> R[i][j];
        }
    }

    // Алгоритм Уоршелла для поиска путей через промежуточную вершину k
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                // Если пути напрямую нет, проверяем путь через вершину k
                if (R[i][j] == 0) {
                    if (R[i][k] == 1 && R[k][j] == 1) {
                        R[i][j] = 1;
                    }
                }
            }
        }
    }

    // Вывод матрицы достижимости
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << R[i][j] << (j == n - 1 ? "" : " ");
        }
        std::cout << "\n";
    }

    return 0;
}
