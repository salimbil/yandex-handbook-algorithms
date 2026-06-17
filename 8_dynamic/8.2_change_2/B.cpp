// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    int n, S;
    cin >> n >> S;
    
    vector<int> dp(S + 1, INF);
    dp[0] = 0;
    
    for (int i = 0; i < n; ++i) {
        int v, c;
        cin >> v >> c;
        
        // бинарное разложение
        int cnt = 1;
        while (c > 0) {
            int take = min(cnt, c);
            int weight = take * v;
            int cost = take;
            
            // 0/1 рюкзак — проход справа налево
            for (int sum = S; sum >= weight; --sum) {
                if (dp[sum - weight] != INF) {
                    dp[sum] = min(dp[sum], dp[sum - weight] + cost);
                }
            }
            
            c -= take;
            cnt <<= 1;
        }
    }
    
    if (dp[S] == INF) {
        cout << -1 << endl;
    } else {
        cout << dp[S] << endl;
    }
    
    return 0;
}
