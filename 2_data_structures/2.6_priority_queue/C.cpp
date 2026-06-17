// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.rbegin(), a.rend());

    long long sum = 0;
    for (int i = 0; i < k; ++i) {
        if (a[i] > 0) {
            sum += a[i];
        } else {
            break;
        }
    }

    cout << sum << "\n";

    return 0;
}
