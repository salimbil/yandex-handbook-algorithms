// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<int> lst;
    
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int x, y;
            cin >> x >> y;
            // Вставка после x-го элемента (индекс x)
            lst.insert(lst.begin() + x, y);
        } else if (type == 2) {
            int x;
            cin >> x;
            // Вывод x-го элемента (индекс x - 1)
            cout << lst[x - 1] << "\n";
        } else if (type == 3) {
            int x;
            cin >> x;
            // Удаление x-го элемента (индекс x - 1)
            lst.erase(lst.begin() + (x - 1));
        }
    }
    
    return 0;
}
