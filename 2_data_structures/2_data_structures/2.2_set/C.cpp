// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

// Размер массива для подсчета вхождений элементов (x <= 10^6)
const int MAX_VAL = 1000005;
int counts[MAX_VAL];

int main() {
    // Ускорение ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // Считываем каждое множество
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        for (int j = 0; j < k; ++j) {
            int x;
            cin >> x;
            if (x < MAX_VAL) {
                counts[x]++; // Увеличиваем счетчик присутствия числа во множествах
            }
        }
    }
    
    // Считаем, сколько элементов встретилось ровно во всех n множествах
    int intersection_size = 0;
    for (int i = 0; i < MAX_VAL; ++i) {
        if (counts[i] == n) {
            intersection_size++;
        }
    }
    
    // Выводим размер пересечения
    cout << intersection_size << "\n";
    
    return 0;
}
