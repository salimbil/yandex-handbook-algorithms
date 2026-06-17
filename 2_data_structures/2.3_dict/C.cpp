// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <numeric>
#include <map>
#include <utility>

using namespace std;

int main() {
    // Максимальное ускорение ввода-вывода для Яндекса
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    // Карта: { {сокращенный_числитель, сокращенный_знаменатель} -> количество_вхождений }
    map<pair<int, int>, int> frac_counts;
    
    for (int i = 0; i < n; ++i) {
        int num, den;
        cin >> num >> den;
        
        // Находим наибольший общий делитель для сокращения дроби
        int g = std::gcd(num, den);
        num /= g;
        den /= g;
        
        frac_counts[{num, den}]++;
    }
    
    int max_freq = -1;
    pair<int, int> best_frac = {-1, -1};
    
    for (auto const& [frac, count] : frac_counts) {
        if (count > max_freq) {
            max_freq = count;
            best_frac = frac;
        } else if (count == max_freq) {
            // Если частоты равны, выбираем меньшую дробь по значению:
            // a/b < c/d  <=>  a * d < b * c
            long long a = best_frac.first;
            long long b = best_frac.second;
            long long c = frac.first;
            long long d = frac.second;
            
            if (c * b < a * d) {
                best_frac = frac;
            }
        }
    }
    
    // Выводим числитель и знаменатель искомой несократимой дроби
    cout << best_frac.first << " " << best_frac.second << "\n";
    
    return 0;
}
