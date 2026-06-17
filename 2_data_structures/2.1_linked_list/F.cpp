// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    int max_val = -1;
    int last_max_idx = -1;
    
    // Считываем массив и ищем САМЫЙ ПРАВЫЙ максимум
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        // Используем >= чтобы сместить индекс к самому правому вхождению при равенстве
        if (a[i] >= max_val) {
            max_val = a[i];
            last_max_idx = i;
        }
    }
    
    // Выводим все элементы через пробел, пропуская последний максимум
    bool first = true;
    for (int i = 0; i < n; ++i) {
        if (i == last_max_idx) {
            continue;
        }
        if (!first) {
            cout << " ";
        }
        cout << a[i];
        first = false;
    }
    cout << "\n";
    
    return 0;
}
