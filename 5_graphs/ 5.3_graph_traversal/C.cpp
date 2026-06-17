// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Point {
    int r, c;
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
    Point start, finish;

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'S') start = {i, j};
            if (grid[i][j] == 'F') finish = {i, j};
        }
    }

    vector<vector<int>> p_dir(n, vector<int>(m, -1));
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<Point> q;

    visited[start.r][start.c] = true;
    q.push(start);

    bool found = false;

    while (!q.empty()) {
        Point curr = q.front();
        q.pop();

        if (curr.r == finish.r && curr.c == finish.c) {
            found = true;
            break;
        }

        for (int i = 0; i < 4; ++i) {
            int nr = curr.r + dr[i];
            int nc = curr.c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                if (!visited[nr][nc] && grid[nr][nc] != '#') {
                    visited[nr][nc] = true;
                    p_dir[nr][nc] = i; 
                    q.push({nr, nc});
                }
            }
        }
    }

    if (!found) {
        cout << -1 << "\n";
        return 0;
    }

    string path = "";
    Point curr = finish;

    while (curr.r != start.r || curr.c != start.c) {
        int d = p_dir[curr.r][curr.c];
        path += dir_chars[d];
        curr.r -= dr[d];
        curr.c -= dc[d];
    }

    reverse(path.begin(), path.end());

    cout << path.length() << "\n" << path << "\n";

    return 0;
}
