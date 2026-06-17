// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

bool canCover(const vector<long long>& x, int k, double R) {
    int count = 1;
    double last_covered = x[0] + 2*R;
    for (size_t i = 1; i < x.size(); ++i) {
        if (x[i] > last_covered) {
            ++count;
            last_covered = x[i] + 2*R;
        }
    }
    return count <= k;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<long long> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }
    sort(x.begin(), x.end());

    double low = 0.0;
    double high = x.back() - x.front(); // максимально возможный R

    // Бинарный поиск с точностью 1e-7
    for (int iter = 0; iter < 60; ++iter) {
        double mid = (low + high) / 2;
        if (canCover(x, k, mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(6) << high << endl;

    return 0;
}
