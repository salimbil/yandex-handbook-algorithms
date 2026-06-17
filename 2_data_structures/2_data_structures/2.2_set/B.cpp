// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

// Поскольку максимальное значение x равно 10^6, создаем массив для отметок
// Размер берем с небольшим запасом
const int MAX_VAL = 1000005;
bool visited[MAX_VAL];

int main() {
    // Ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    int unique_count = 0;
    
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        for (int j = 0; j < k; ++j) {
            int x;
            cin >> x;
            // Если мы это число еще не встречали ни в одном множестве
            if (!visited[x]) {
                visited[x] = true;
                unique_count++; // Увеличиваем счетчик уникальных элементов
            }
        }
    }
    
    // Выводим итоговый размер объединения множеств
    cout << unique_count << "\n";
    
    return 0;
}
