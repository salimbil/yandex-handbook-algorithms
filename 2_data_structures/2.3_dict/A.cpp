// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    if (!(cin >> q)) return 0;
    
    unordered_map<int, int> dict;
    
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int x, y;
            cin >> x >> y;
            // Записываем или обновляем значение y по ключу x
            dict[x] = y;
        } else if (type == 2) {
            int x;
            cin >> x;
            // Ищем ключ в словаре
            auto it = dict.find(x);
            if (it != dict.end()) {
                // Если ключ найден, выводим соответствующее число
                cout << it->second << "\n";
            } else {
                // Если ключа в словаре нет, выводим -1 по условию
                cout << -1 << "\n";
            }
        }
    }
    
    return 0;
}
