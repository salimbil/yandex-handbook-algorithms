// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    if (!(cin >> q)) return 0;
    
    unordered_set<int> elements;
    
    for (int i = 0; i < q; ++i) {
        int type, x;
        cin >> type >> x;
        
        if (type == 1) {
            // Добавляем число во множество
            elements.insert(x);
        } else if (type == 2) {
            // Проверяем, есть ли число во множестве
            if (elements.count(x)) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        }
    }
    
    return 0;
}
