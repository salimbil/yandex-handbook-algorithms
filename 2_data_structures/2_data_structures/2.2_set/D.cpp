// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    // Оптимизация ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<vector<int>> s(n);
    unordered_map<int, int> counts; // Храним частоту каждого числа во всех множествах
    
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        s[i].resize(k);
        for (int j = 0; j < k; ++j) {
            cin >> s[i][j];
            counts[s[i][j]]++;
        }
    }
    
    int core_size = 0;
    
    // Проверяем корректность структуры лепестков
    for (auto const& [val, count] : counts) {
        if (count == n) {
            core_size++; // Этот элемент принадлежит ядру
        } else if (count > 1) {
            // Элемент встречается больше чем в 1 множестве, но не во всех.
            // Значит, лепестки пересекаются -> это не подсолнечник.
            cout << "NO\n";
            return 0;
        }
    }
    
    // Если прошли проверку, значит это подсолнечник
    cout << "YES\n";
    cout << core_size << "\n";
    
    // Вычисляем размер каждого лепестка
    for (int i = 0; i < n; ++i) {
        int petal_size = 0;
        for (int val : s[i]) {
            if (counts[val] != n) {
                petal_size++;
            }
        }
        cout << petal_size << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    
    return 0;
}
