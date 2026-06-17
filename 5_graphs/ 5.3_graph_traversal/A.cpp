// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    // Оптимизация ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> in_degree(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v, t;
        cin >> u >> v >> t;
        int winner = (t == 1) ? u : v;
        int loser = (t == 1) ? v : u;
        
        adj[winner].push_back(loser);
        in_degree[loser]++;
    }

    queue<int> q;
    // Находим всех игроков, которые никому не проиграли
    for (int i = 1; i <= n; ++i) {
        if (in_degree[i] == 0) {
            q.push(i);
        }
    }

    int visited_count = 0;
    bool unique = true;

    while (!q.empty()) {
        // Если в очереди больше одного элемента, выбор неоднозначен
        if (q.size() > 1) {
            unique = false;
            break;
        }

        int curr = q.front();
        q.pop();
        visited_count++;

        for (int neighbor : adj[curr]) {
            in_degree[neighbor]--;
            if (in_degree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // Если мы посетили все N вершин и на каждом шаге выбор был однозначен
    if (unique && visited_count == n) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
