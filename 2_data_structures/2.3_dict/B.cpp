// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Размер массива счетчиков (a_i <= 10^5)
const int MAX_VAL = 100005;
int counts[MAX_VAL];

int main() {
    // Ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    for (int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        if (val < MAX_VAL) {
            counts[val]++; // Считаем частоту каждого числа
        }
    }
    
    int max_freq = -1;
    int best_val = -1;
    
    // Идем по значениям от 1 до 10^5.
    // Так как мы идем по возрастанию чисел, условие "выбрать наименьший при равной частоте"
    // выполнится автоматически, если использовать строгое сравнение (>)
    for (int i = 1; i < MAX_VAL; ++i) {
        if (counts[i] > max_freq) {
            max_freq = counts[i];
            best_val = i;
        }
    }
    
    // Выводим самый частый элемент
    cout << best_val << "\n";
    
    return 0;
}
