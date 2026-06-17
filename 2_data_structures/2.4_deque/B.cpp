// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <deque>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    if (!(cin >> q)) return 0;
    
    deque<int> dq;
    
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int x;
            cin >> x;
            dq.push_front(x);
        } else if (type == 2) {
            int x;
            cin >> x;
            dq.push_back(x);
        } else if (type == 3) {
            if (!dq.empty()) {
                dq.pop_front();
            }
        } else if (type == 4) {
            if (!dq.empty()) {
                dq.pop_back();
            }
        }
        
        // Выводим состояние дека после выполнения команды
        if (dq.empty()) {
            cout << -1 << "\n";
        } else {
            cout << dq.front() << " " << dq.back() << "\n";
        }
    }
    
    return 0;
}
