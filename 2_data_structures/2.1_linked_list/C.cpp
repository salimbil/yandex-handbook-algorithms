// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

// Создаем массив для хранения позиций чисел.
// Максимальное значение a_i и x_i равно 10^5, берем размер с запасом
const int MAX_VAL = 100005;
int first_pos[MAX_VAL];

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    // Инициализируем массив позиций значениями -1 (означает, что число еще не встречалось)
    for (int i = 0; i < MAX_VAL; ++i) {
        first_pos[i] = -1;
    }
    
    // Считываем массив и запоминаем только ПЕРВОЕ (самое левое) вхождение каждого числа
    for (int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        // Если число встретилось впервые, сохраняем его 1-базовый индекс
        if (first_pos[val] == -1) {
            first_pos[val] = i + 1;
        }
    }
    
    // Отвечаем на запросы за O(1) каждый
    for (int i = 0; i < q; ++i) {
        int x;
        cin >> x;
        // Если запрашиваемое число больше нашего максимума, его точно нет
        if (x >= MAX_VAL) {
            cout << -1 << "\n";
        } else {
            cout << first_pos[x] << "\n";
        }
    }
    
    return 0;
}
