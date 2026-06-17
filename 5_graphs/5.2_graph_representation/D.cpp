// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // Оптимизация ввода-вывода
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int d;
    if (!(std::cin >> d)) return 0;

    // Так как по условию n <= 100, заведем матрицу с запасом (105 x 105), заполненную нулями
    std::vector<std::vector<int>> adj(105, std::vector<int>(105, 0));
    int max_n = 0; // Для динамического определения общего числа сотрудников n

    for (int i = 0; i < d; ++i) {
        int k, boss;
        std::cin >> k >> boss;
        
        if (boss > max_n) {
            max_n = boss;
        }

        // Считываем k - 1 подчиненных
        for (int j = 0; j < k - 1; ++j) {
            int subordinate;
            std::cin >> subordinate;
            
            if (subordinate > max_n) {
                max_n = subordinate;
            }

            // Устанавливаем связи: 
            // boss -> subordinate равен 1
            // subordinate -> boss равен -1
            adj[boss][subordinate] = 1;
            adj[subordinate][boss] = -1;
        }
    }

    // Выводим матрицу смежности размера max_n x max_n (используем 1-индексацию)
    for (int i = 1; i <= max_n; ++i) {
        for (int j = 1; j <= max_n; ++j) {
            std::cout << adj[i][j] << (j == max_n ? "" : " ");
        }
        std::cout << "\n";
    }

    return 0;
}
