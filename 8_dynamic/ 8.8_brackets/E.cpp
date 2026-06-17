// Компилятор: C++23 (Clang 18.1.8)
#include <bits/stdc++.h>
using namespace std;

static const long long INF = (long long)4e18;

long long apply(char op, long long a, long long b) {
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    return a * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int m = (s.size() + 1) / 2; // количество чисел
    vector<long long> num(m);
    vector<char> op(m - 1);

    for (int i = 0; i < m; i++)
        num[i] = s[2 * i] - '0';
    for (int i = 0; i + 1 < m; i++)
        op[i] = s[2 * i + 1];

    // dp[l][r][used][0=min,1=max]
    static long long dp[15][15][2][2];

    for (int i = 0; i < m; i++) {
        dp[i][i][0][0] = dp[i][i][0][1] = num[i];
        dp[i][i][1][0] = dp[i][i][1][1] = num[i];
    }

    for (int len = 2; len <= m; len++) {
        for (int l = 0; l + len - 1 < m; l++) {
            int r = l + len - 1;
            for (int used = 0; used <= 1; used++) {
                dp[l][r][used][0] = INF;
                dp[l][r][used][1] = -INF;
            }

            for (int k = l; k < r; k++) {
                for (int ul = 0; ul <= 1; ul++) {
                    for (int ur = 0; ur <= 1; ur++) {
                        for (int tl = 0; tl <= 1; tl++) {
                            for (int tr = 0; tr <= 1; tr++) {
                                long long A = dp[l][k][ul][tl];
                                long long B = dp[k + 1][r][ur][tr];

                                // без замены
                                int used0 = ul | ur;
                                long long v0 = apply(op[k], A, B);
                                dp[l][r][used0][0] = min(dp[l][r][used0][0], v0);
                                dp[l][r][used0][1] = max(dp[l][r][used0][1], v0);

                                // с заменой
                                if (used0 == 0) {
                                    for (char c : {'+', '-', '*'}) {
                                        if (c == op[k]) continue;
                                        long long v = apply(c, A, B);
                                        dp[l][r][1][0] = min(dp[l][r][1][0], v);
                                        dp[l][r][1][1] = max(dp[l][r][1][1], v);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    cout << max(dp[0][m - 1][0][1], dp[0][m - 1][1][1]) << "\n";
    return 0;
}
