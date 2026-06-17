// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;

struct State {
    int r, c, mask;
};

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, 1, -1};
char dir_chars[] = {'U', 'D', 'R', 'L'};

int dist[50][50][1024];
int p_state[50][50][1024];
char p_act[50][50][1024];

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

    int k;
    if (!(cin >> k)) return 0;

    map<char, int> door_to_id;
    map<char, int> key_to_id;

    for (int i = 0; i < k; ++i) {
        char door, key;
        cin >> door >> key;
        door_to_id[door] = i;
        key_to_id[key] = i;
    }

    int max_mask = 1 << k;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int mask = 0; mask < max_mask; ++mask) {
                dist[i][j][mask] = -1;
                p_state[i][j][mask] = -1;
                p_act[i][j][mask] = 0;
            }
        }
    }

    queue<State> q;
    dist[sr][sc][0] = 0;
    q.push({sr, sc, 0});

    int final_r = -1, final_c = -1, final_mask = -1;

    while (!q.empty()) {
        State curr = q.front();
        q.pop();

        if (curr.r == fr && curr.c == fc) {
            final_r = curr.r;
            final_c = curr.c;
            final_mask = curr.mask;
            break;
        }

        int curr_dist = dist[curr.r][curr.c][curr.mask];

        for (int i = 0; i < 4; ++i) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                char cell = grid[nr][nc];
                if (cell == '#') continue;

                if (door_to_id.count(cell)) {
                    int id = door_to_id[cell];
                    if (!(curr.mask & (1 << id))) continue;
                }

                if (dist[nr][nc][curr.mask] == -1) {
                    dist[nr][nc][curr.mask] = curr_dist + 1;
                    p_state[nr][nc][curr.mask] = (curr.r << 16) | (curr.c << 10) | curr.mask;
                    p_act[nr][nc][curr.mask] = dir_chars[i];
                    q.push({nr, nc, curr.mask});
                }
            }
        }

        char cell = grid[curr.r][curr.c];
        if (key_to_id.count(cell)) {
            int id = key_to_id[cell];
            if (!(curr.mask & (1 << id))) {
                int next_mask = curr.mask | (1 << id);
                if (dist[curr.r][curr.c][next_mask] == -1) {
                    dist[curr.r][curr.c][next_mask] = curr_dist + 1;
                    p_state[curr.r][curr.c][next_mask] = (curr.r << 16) | (curr.c << 10) | curr.mask;
                    p_act[curr.r][curr.c][next_mask] = 'P';
                    q.push({curr.r, curr.c, next_mask});
                }
            }
        }
    }

    if (final_mask == -1) {
        cout << -1 << "\n";
        return 0;
    }

    string path = "";
    int cr = final_r, cc = final_c, cm = final_mask;

    while (true) {
        int parent = p_state[cr][cc][cm];
        if (parent == -1) break;

        path += p_act[cr][cc][cm];
        cr = (parent >> 16) & 0x3F;
        cc = (parent >> 10) & 0x3F;
        cm = parent & 0x3FF;
    }

    reverse(path.begin(), path.end());

    cout << path.length() << "\n" << path << "\n";

    return 0;
}
