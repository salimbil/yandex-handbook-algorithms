// Компилятор: C++23 (Clang 18.1.8)
#include <bits/stdc++.h>
using namespace std;

struct State {
    int x;
    int used3;
    int dist;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, k;
    cin >> a >> b >> k;

    vector<bitset<61>> visited(b + 1);
    queue<State> q;

    visited[a][0] = true;
    q.push({a, 0, 0});

    while (!q.empty()) {
        auto [x, used3, dist] = q.front();
        q.pop();

        if (x == b) {
            cout << dist << "\n";
            return 0;
        }

        // +1, +2, +3
        for (int d = 1; d <= 3; d++) {
            int nx = x + d;
            if (nx <= b && !visited[nx][used3]) {
                visited[nx][used3] = true;
                q.push({nx, used3, dist + 1});
            }
        }

        // *2
        if (x * 2 <= b && !visited[x * 2][used3]) {
            visited[x * 2][used3] = true;
            q.push({x * 2, used3, dist + 1});
        }

        // *3 (ограничено)
        if (used3 < k && x * 3 <= b && !visited[x * 3][used3 + 1]) {
            visited[x * 3][used3 + 1] = true;
            q.push({x * 3, used3 + 1, dist + 1});
        }
    }

    cout << -1 << "\n";
    return 0;
}
