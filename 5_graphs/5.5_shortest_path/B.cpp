// Компилятор: C++23 (Clang 18.1.8)
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e18;

int n, m, V, O[3];
vector<vector<pair<int, int>>> g;

bool is_station[100005];
bool is_parking[100005];
bool is_order[100005];

struct State {
    int v, scooter, mask;
    ll dist;
    bool operator>(const State& other) const { return dist > other.dist; }
};

struct ParentInfo {
    int v, scooter, mask;
    char action; // 'M' - move, 'R' - rent, 'D' - drop (оставить)
    int edge_to; // для перемещения
};
ParentInfo parent[100005][2][8];
ll dist[100005][2][8];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m >> V >> O[0] >> O[1] >> O[2];
    g.resize(n + 1);
    
    for (int i = 0; i < m; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        g[u].push_back({v, c});
        g[v].push_back({u, c});
    }
    
    int k; cin >> k;
    for (int i = 0; i < k; i++) {
        int x; cin >> x;
        is_station[x] = true;
    }
    
    int l; cin >> l;
    for (int i = 0; i < l; i++) {
        int x; cin >> x;
        is_parking[x] = true;
    }
    
    for (int i = 0; i < 3; i++) {
        is_order[O[i]] = true;
    }
    
    for (int i = 1; i <= n; i++)
        for (int s = 0; s < 2; s++)
            for (int msk = 0; msk < 8; msk++)
                dist[i][s][msk] = INF;
    
    priority_queue<State, vector<State>, greater<State>> pq;
    dist[V][0][0] = 0;
    pq.push({V, 0, 0, 0});
    
    while (!pq.empty()) {
        State cur = pq.top(); pq.pop();
        if (cur.dist > dist[cur.v][cur.scooter][cur.mask]) continue;
        
        // Если все заказы выполнены и мы на складе
        if (cur.mask == 7 && cur.v == V) {
            // Восстановление пути и состояний самоката
            vector<int> path;
            vector<char> scooter_state;
            
            // Сначала соберём действия в обратном порядке
            vector<pair<int, char>> actions; // (вершина, состояние самоката в этой вершине)
            int v = cur.v, scooter = cur.scooter, mask = cur.mask;
            actions.push_back({v, (char)(scooter + '0')});
            
            while (!(v == V && scooter == 0 && mask == 0)) {
                ParentInfo p = parent[v][scooter][mask];
                if (p.action == 'M') {
                    // Перемещение: добавляем предыдущую вершину
                    actions.push_back({p.v, (char)(p.scooter + '0')});
                } else if (p.action == 'R') {
                    // Аренда: вершина та же, состояние меняется
                    actions.push_back({p.v, (char)(p.scooter + '0')});
                } else if (p.action == 'D') {
                    // Оставление: вершина та же
                    actions.push_back({p.v, (char)(p.scooter + '0')});
                }
                v = p.v;
                scooter = p.scooter;
                mask = p.mask;
            }
            
            reverse(actions.begin(), actions.end());
            
            // Теперь actions содержит последовательность (вершина, состояние_в_вершине)
            // Но в ней могут быть повторы (аренда/оставление без перемещения)
            // Нужно сжать: оставить только уникальные вершины в порядке посещения
            vector<int> final_path;
            vector<char> final_state;
            for (size_t i = 0; i < actions.size(); i++) {
                if (i == 0 || actions[i].first != actions[i-1].first) {
                    final_path.push_back(actions[i].first);
                    final_state.push_back(actions[i].second);
                } else {
                    // Та же вершина — обновляем состояние (последнее действие в ней)
                    final_state.back() = actions[i].second;
                }
            }
            
            cout << final_path.size() << "\n";
            for (size_t i = 0; i < final_path.size(); i++) {
                if (i) cout << " ";
                cout << final_path[i];
            }
            cout << "\n";
            for (char c : final_state) cout << c;
            cout << "\n";
            return 0;
        }
        
        // 1. Аренда самоката (станция, нет самоката)
        if (is_station[cur.v] && cur.scooter == 0) {
            if (dist[cur.v][1][cur.mask] > cur.dist) {
                dist[cur.v][1][cur.mask] = cur.dist;
                parent[cur.v][1][cur.mask] = {cur.v, cur.scooter, cur.mask, 'R', -1};
                pq.push({cur.v, 1, cur.mask, cur.dist});
            }
        }
        
        // 2. Оставление самоката (парковка, есть самокат)
        if (is_parking[cur.v] && cur.scooter == 1) {
            if (dist[cur.v][0][cur.mask] > cur.dist) {
                dist[cur.v][0][cur.mask] = cur.dist;
                parent[cur.v][0][cur.mask] = {cur.v, cur.scooter, cur.mask, 'D', -1};
                pq.push({cur.v, 0, cur.mask, cur.dist});
            }
        }
        
        // 3. Перемещение по рёбрам
        for (auto [to, w] : g[cur.v]) {
            int new_scooter = cur.scooter;
            ll new_dist = cur.dist + (cur.scooter ? (w + 1) / 2 : w);
            int new_mask = cur.mask;
            
            // Если заходим в заказ, который ещё не выполнен
            if (is_order[to]) {
                int idx = -1;
                for (int i = 0; i < 3; i++) if (O[i] == to) idx = i;
                if (idx != -1 && !(cur.mask >> idx & 1)) {
                    // Первое посещение заказа → самокат сбрасывается
                    new_scooter = 0;
                    new_mask |= (1 << idx);
                    // Если заказ — станция, можно сразу арендовать
                    if (is_station[to]) {
                        new_scooter = 1;
                    }
                }
            }
            
            if (dist[to][new_scooter][new_mask] > new_dist) {
                dist[to][new_scooter][new_mask] = new_dist;
                parent[to][new_scooter][new_mask] = {cur.v, cur.scooter, cur.mask, 'M', to};
                pq.push({to, new_scooter, new_mask, new_dist});
            }
        }
    }
    
    cout << -1 << endl;
    return 0;
}
