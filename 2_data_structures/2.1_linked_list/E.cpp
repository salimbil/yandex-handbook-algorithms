// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    // Вектор булевых значений для пометки элементов, которые нужно удалить
    vector<bool> to_remove(n, false);
    
    // Ищем локальные минимумы в исходном массиве
    // В 0-индексации это элементы от 1 до n-2 включительно
    for (int i = 1; i < n - 1; ++i) {
        if (a[i - 1] > a[i] && a[i] < a[i + 1]) {
            to_remove[i] = true;
        }
    }
    
    // Собираем оставшиеся элементы
    vector<int> result;
    for (int i = 0; i < n; ++i) {
        if (!to_remove[i]) {
            result.push_back(a[i]);
        }
    }
    
    // Выводим количество оставшихся элементов
    cout << result.size() << "\n";
    
    // Выводим сами элементы через пробел
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i] << (i + 1 == result.size() ? "" : " ");
    }
    cout << "\n";
    
    return 0;
}
