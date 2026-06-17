// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lcs(const vector<int>& A, const vector<int>& B_shift) {
    int n = A.size();
    int m = B_shift.size();
    vector<vector<int>> dp(2, vector<int>(m + 1, 0));
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (A[i - 1] == B_shift[j - 1]) {
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1;
            } else {
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1]);
            }
        }
    }
    return dp[n % 2][m];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; ++i) cin >> B[i];
    
    // Удвоим B
    vector<int> B2 = B;
    B2.insert(B2.end(), B.begin(), B.end());
    
    int ans = 0;
    for (int start = 0; start < m; ++start) {
        vector<int> shifted(B2.begin() + start, B2.begin() + start + m);
        ans = max(ans, lcs(A, shifted));
    }
    
    cout << ans << "\n";
    
    return 0;
}
