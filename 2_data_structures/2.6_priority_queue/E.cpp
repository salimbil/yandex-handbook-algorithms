// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    priority_queue<tuple<long long, int, long long, long long>, 
                   vector<tuple<long long, int, long long, long long>>, 
                   greater<tuple<long long, int, long long, long long>>> pq;

    for (int i = 0; i < n; ++i) {
        long long id, p, s;
        cin >> id >> p >> s;
        pq.emplace(s, id, p, s);
    }

    for (int i = 0; i < m; ++i) {
        auto [time, id, p, s] = pq.top();
        pq.pop();
        cout << id << "\n";
        pq.emplace(time + p, id, p, s);
    }

    return 0;
}
