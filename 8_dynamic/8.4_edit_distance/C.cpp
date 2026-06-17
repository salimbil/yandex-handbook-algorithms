// Компилятор: C++23 (Clang 18.1.8)
#include <bits/stdc++.h>
using namespace std;

// Функция для вычисления расстояния Левенштейна между строками a и b
int levenshtein(const string &a, const string &b) {
    int n = a.size();
    int m = b.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

    // Базовые случаи
    for (int i = 0; i <= n; ++i) dp[i][0] = i; // удаление
    for (int j = 0; j <= m; ++j) dp[0][j] = j; // вставка

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i-1] == b[j-1]) {
                dp[i][j] = dp[i-1][j-1]; // символы совпадают
            } else {
                dp[i][j] = 1 + min({dp[i-1][j],   // удаление
                                    dp[i][j-1],   // вставка
                                    dp[i-1][j-1]  // замена
                                   });
            }
        }
    }
    return dp[n][m];
}

int main() {
    string s;
    cin >> s;
    int n;
    cin >> n;
    
    int min_distance = INT_MAX;
    for (int i = 0; i < n; ++i) {
        string word;
        cin >> word;
        min_distance = min(min_distance, levenshtein(s, word));
    }

    cout << min_distance << endl;
    return 0;
}
