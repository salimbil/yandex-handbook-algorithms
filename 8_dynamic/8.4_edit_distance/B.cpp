// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s, t;
    getline(cin, s);
    getline(cin, t);
    
    long long D, I, R;
    cin >> D >> I >> R;
    
    int n = s.size(), m = t.size();
    
    // dp[i][j] - минимальная стоимость превращения s[0..i-1] в t[0..j-1]
    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
    
    // Инициализация
    for (int i = 1; i <= n; ++i) {
        dp[i][0] = i * D;  // удалить все символы из s
    }
    for (int j = 1; j <= m; ++j) {
        dp[0][j] = j * I;  // вставить все символы в t
    }
    
    // Заполнение таблицы
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i-1] == t[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = dp[i-1][j-1] + R;
            }
            
            dp[i][j] = min(dp[i][j], dp[i-1][j] + D);  // удалить из s
            dp[i][j] = min(dp[i][j], dp[i][j-1] + I);  // вставить в s
        }
    }
    
    cout << dp[n][m] << endl;
    
    return 0;
}
