// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Оптимизация ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    // Переменные для МИНИМАЛЬНОГО перепада (a_i - a_j -> min)
    long long min_diff = 2e18; // Инициализируем заведомо большим числом
    int ans_i1 = -1, ans_j1 = -1;
    int best_min_i = 0; // Индекс минимального элемента слева
    
    // Переменные для МАКСИМАЛЬНОГО перепада (a_i - a_j -> max)
    long long max_diff = -2e18; // Инициализируем заведомо маленьким числом
    int ans_i2 = -1, ans_j2 = -1;
    int best_max_i = 0; // Индекс максимального элемента слева
    
    // Идем по j от 1 до n-1, фиксируя второй элемент в паре
    for (int j = 1; j < n; ++j) {
        
        // 1. Считаем текущие разности с лучшими индексами слева
        long long cur_min_diff = (long long)a[best_min_i] - a[j];
        long long cur_max_diff = (long long)a[best_max_i] - a[j];
        
        // Проверка для МИНИМУМА
        if (cur_min_diff < min_diff) {
            min_diff = cur_min_diff;
            ans_i1 = best_min_i + 1; // Переводим в 1-индексацию
            ans_j1 = j + 1;
        } else if (cur_min_diff == min_diff) {
            int cur_i = best_min_i + 1;
            int cur_j = j + 1;
            if (cur_i < ans_i1 || (cur_i == ans_i1 && cur_j < ans_j1)) {
                ans_i1 = cur_i;
                ans_j1 = cur_j;
            }
        }
        
        // Проверка для МАКСИМУМА
        if (cur_max_diff > max_diff) {
            max_diff = cur_max_diff;
            ans_i2 = best_max_i + 1; // Переводим в 1-индексацию
            ans_j2 = j + 1;
        } else if (cur_max_diff == max_diff) {
            int cur_i = best_max_i + 1;
            int cur_j = j + 1;
            if (cur_i < ans_i2 || (cur_i == ans_i2 && cur_j < ans_j2)) {
                ans_i2 = cur_i;
                ans_j2 = cur_j;
            }
        }
        
        // 2. Обновляем лучшие индексы i для следующих шагов (j увеличится)
        // Нам нужен минимальный индекс при равенстве значений, поэтому знак строго < или >
        if (a[j] < a[best_min_i]) {
            best_min_i = j;
        }
        if (a[j] > a[best_max_i]) {
            best_max_i = j;
        }
    }
    
    // Вывод ответа
    cout << ans_i1 << " " << ans_j1 << "\n";
    cout << ans_i2 << " " << ans_j2 << "\n";
    
    return 0;
}
