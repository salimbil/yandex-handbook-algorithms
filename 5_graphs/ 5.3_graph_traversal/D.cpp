// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct State {
    int r, c, k;
};

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, 1, -1};
char dir_chars[] = {'U', 'D', 'R', 'L'};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, fr = -1, fc = -1;

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'S') { sr = i; sc = j; }
            if (grid[i][j] == 'F') { fr = i; fc = j; }
        }
    }

    int total_states = n * m * 2;
    vector<int> dist(total_states, -1);
    vector<int> p_state(total_states, -1);
    vector<char> p_act(total_states, 0);

    auto get_id = [&](int r, int c, int k) {
        return (r * m + c) * 2 + k;
    };

    queue<State> q;
    int start_id = get_id(sr, sc, 0);
    dist[start_id] = 0;
    q.push({sr, sc, 0});

    int final_state_id = -1;

    while (!q.empty()) {
        State curr = q.front();
        q.pop();

        int curr_id = get_id(curr.r, curr.c, curr.k);

        if (curr.r == fr && curr.c == fc) {
            final_state_id = curr_id;
            break;
        }

        for (int i = 0; i < 4; ++i) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                if (grid[nr][nc] == '#') continue;
                if (grid[nr][nc] == 'D' && curr.k == 0) continue;

                int next_id = get_id(nr, nc, curr.k);
                if (dist[next_id] == -1) {
                    dist[next_id] = dist[curr_id] + 1;
                    p_state[next_id] = curr_id;
                    p_act[next_id] = dir_chars[i];
                    q.push({nr, nc, curr.k});
                }
            }
        }

        if (grid[curr.r][curr.c] == 'K' && curr.k == 0) {
            int next_id = get_id(curr.r, curr.c, 1);
            if (dist[next_id] == -1) {
                dist[next_id] = dist[curr_id] + 1;
                p_state[next_id] = curr_id;
                p_act[next_id] = 'P';
                q.push({curr.r, curr.c, 1});
            }
        }
    }

    if (final_state_id == -1) {
        cout << -1 << "\n";
        return 0;
    }

    string path = "";
    int curr_id = final_state_id;
    while (p_state[curr_id] != -1) {
        path += p_act[curr_id];
        curr_id = p_state[curr_id];
    }

    reverse(path.begin(), path.end());

    cout << path.length() << "\n" << path << "\n";

    return 0;
}
