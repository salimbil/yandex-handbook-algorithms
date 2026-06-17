// Компилятор: C++23 (Clang 18.1.8)
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long weight;
};

int n, m;
vector<vector<Edge>> graph;

// Функция Дейкстры, возвращает расстояния и массив предков (parent)
void dijkstra(int start, vector<long long>& dist, vector<int>& parent) {
    dist.assign(n + 1, INF);
    parent.assign(n + 1, -1);
    dist[start] = 0;

    // {расстояние, вершина}
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& edge : graph[u]) {
            int v = edge.to;
            long long w = edge.weight;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }
}

// Восстановление пути от start до end с помощью массива parent
vector<int> reconstruct_path(int end, const vector<int>& parent) {
    vector<int> path;
    for (int v = end; v != -1; v = parent[v]) {
        path.push_back(v);
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    // Оптимизация ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int V;
    vector<int> O(3);
    if (!(cin >> n >> m >> V >> O[0] >> O[1] >> O[2])) return 0;

    graph.resize(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        graph[u].push_back({v, c});
        graph[v].push_back({u, c});
    }

    // Ключевые вершины: V (индекс 0), O0 (1), O1 (2), O2 (3)
    vector<int> targets = {V, O[0], O[1], O[2]};
    
    // Матрицы для хранения результатов Дейкстры
    vector<vector<long long>> dist(4);
    vector<vector<int>> parent(4);

    for (int i = 0; i < 4; ++i) {
        dijkstra(targets[i], dist[i], parent[i]);
    }

    // Функция, возвращающая индекс ключевой вершины в массиве targets
    auto get_idx = [&](int node) {
        for (int i = 0; i < 4; ++i) {
            if (targets[i] == node) return i;
        }
        return -1;
    };

    long long min_total_dist = INF;
    vector<int> best_order;

    // Перебираем все перестановки индексов заказов (0, 1, 2)
    vector<int> perm = {0, 1, 2};
    do {
        int p1 = O[perm[0]];
        int p2 = O[perm[1]];
        int p3 = O[perm[2]];

        long long d1 = dist[get_idx(V)][p1];
        long long d2 = dist[get_idx(p1)][p2];
        long long d3 = dist[get_idx(p2)][p3];
        long long d4 = dist[get_idx(p3)][V];

        if (d1 < INF && d2 < INF && d3 < INF && d4 < INF) {
            long long current_sum = d1 + d2 + d3 + d4;
            if (current_sum < min_total_dist) {
                min_total_dist = current_sum;
                best_order = {V, p1, p2, p3, V};
            }
        }
    } while (next_permutation(perm.begin(), perm.end()));

    // Склеиваем итоговый путь
    vector<int> final_path;
    for (size_t i = 0; i < best_order.size() - 1; ++i) {
        int from = best_order[i];
        int to = best_order[i + 1];
        int from_idx = get_idx(from);
        
        vector<int> sub_path = reconstruct_path(to, parent[from_idx]);
        
        // При склеивании убираем дублирующуюся начальную вершину (кроме самого первого отрезка)
        if (!final_path.empty()) {
            final_path.insert(final_path.end(), sub_path.begin() + 1, sub_path.end());
        } else {
            final_path.insert(final_path.end(), sub_path.begin(), sub_path.end());
        }
    }

    // Вывод результатов
    cout << final_path.size() << "\n";
    for (size_t i = 0; i < final_path.size(); ++i) {
        cout << final_path[i] << (i + 1 == final_path.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
