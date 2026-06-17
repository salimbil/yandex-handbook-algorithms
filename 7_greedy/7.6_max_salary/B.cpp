// Компилятор: C++23 (Clang 18.1.8)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int skill_k = a[k - 1];

    int W = 0, S = 0;
    for (int i = 0; i < n; i++) {
        if (i == k - 1) continue;
        if (a[i] < skill_k) W++;
        else S++;
    }

    int wins = 0;

    while (true) {
        // k не может больше выиграть
        if (W == 0) break;

        // k выигрывает у слабого
        wins++;
        W--;

        // сколько игроков остаётся кроме k
        int rest = W + S;
        if (rest == 0) break;

        int next = (rest + 1) / 2;

        // сильные выбивают друг друга
        S = (S + 1) / 2;
        W = next - S;
    }

    cout << wins << "\n";
    return 0;
}
