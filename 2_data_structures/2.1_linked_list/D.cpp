// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    // Ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    int current_min;
    cin >> current_min; // Считываем первый элемент, он же первый минимум
    cout << current_min;
    
    // Считываем оставшиеся n-1 элементов
    for (int i = 1; i < n; ++i) {
        int val;
        cin >> val;
        // Обновляем текущий минимум
        current_min = min(current_min, val);
        // Выводим через пробел
        cout << " " << current_min;
    }
    cout << "\n";
    
    return 0;
}
