// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // Множество для хранения абсолютно всех уникальных результатов OR
    unordered_set<int> all_ors;
    
    // Вектор для хранения уникальных OR подмассивов, заканчивающихся в текущей позиции
    vector<int> current_ors;
    
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        
        vector<int> next_ors;
        // Элемент сам по себе образует подмассив длины 1
        next_ors.push_back(a);
        all_ors.insert(a);
        
        // Делаем OR текущего элемента со всеми результатами с предыдущего шага
        for (int val : current_ors) {
            int new_or = val | a;
            // Чтобы не плодить дубликаты в векторе, добавляем только новые значения
            if (next_ors.empty() || next_ors.back() != new_or) {
                // Маленькая оптимизация: проверяем с последним добавленным
                // Но надежнее сделать unique после цикла, так как их мало (до 30 штук)
                next_ors.push_back(new_or);
            }
        }
        
        // Очищаем дубликаты в next_ors, так как порядок элементов после OR мог измениться
        sort(next_ors.begin(), next_ors.end());
        next_ors.erase(unique(next_ors.begin(), next_ors.end()), next_ors.end());
        
        // Добавляем все новые OR в глобальное множество
        for (int val : next_ors) {
            all_ors.insert(val);
        }
        
        // Переходим к следующему шагу
        current_ors = move(next_ors);
    }
    
    // Выводим количество уникальных значений OR
    cout << all_ors.size() << "\n";
    
    return 0;
}
