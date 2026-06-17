// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    if (n == 1) {
        cout << a[0] << " " << a[0] << "\n";
        return 0;
    }
    if (n == 2) {
        cout << a[0] << " " << a[1] << "\n";
        return 0;
    }

    vector<int> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        L[i] = (i - 1 + n) % n;
        R[i] = (i + 1) % n;
    }

    int cur = 0;
    int alive = n;

    while (alive > 2) {
        int l = L[cur];
        int r = R[cur];

        // Определяем минимум
        int mint;
        if (a[l] < a[cur] && a[l] < a[r])
            mint = l;
        else if (a[cur] < a[l] && a[cur] < a[r])
            mint = cur;
        else
            mint = r;

        // Определяем максимум
        int maxt;
        if (a[l] > a[cur] && a[l] > a[r])
            maxt = l;
        else if (a[cur] > a[l] && a[cur] > a[r])
            maxt = cur;
        else
            maxt = r;

        // Удаляем mint
        int ml = L[mint], mr = R[mint];
        R[ml] = mr;
        L[mr] = ml;

        cur = maxt;
        alive--;
    }

    // alive == 2, cur — один из выживших
    int other = R[cur];
    cout << a[cur] << " " << a[other] << "\n";

    return 0;
}
