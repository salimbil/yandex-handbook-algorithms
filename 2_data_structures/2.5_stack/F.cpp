// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    stack<int> st;
    vector<int> dp(n, 0);
    int ans = 0;
    
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 1) {
            st.push(i);
        } else {
            if (!st.empty()) {
                int j = st.top();
                st.pop();
                int len = i - j + 1;
                if (j > 0 && dp[j - 1] > 0) {
                    len += dp[j - 1];
                }
                dp[i] = len;
                ans = max(ans, len);
            } else {
                dp[i] = 0;
            }
        }
    }
    
    cout << ans << '\n';
    return 0;
}
