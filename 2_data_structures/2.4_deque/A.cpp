// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <queue>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса под 10^6 запросов
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int q;
    if (!(cin >> q)) return 0;
    
    queue<int> q_elements;
    
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int x;
            cin >> x;
            q_elements.push(x);
        } else if (type == 2) {
            q_elements.pop();
        }
        
        // После любого запроса выводим элемент из начала очереди или -1
        if (q_elements.empty()) {
            cout << -1 << "\n";
        } else {
            cout << q_elements.front() << "\n";
        }
    }
    
    return 0;
}
