// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cstring>

using namespace std;

int n, m, k, s;
vector<string> grid;
vector<vector<pair<int,int>>> positions; // possible top-left positions for each window
vector<int> perm;
vector<pair<int,int>> chosen_pos;
bool used[6]; // max k=5, index from 1
int result;

// Check if window with top-left at (r,c) is valid given currently placed windows
bool can_place(int window_id, int r, int c, vector<vector<int>>& board) {
    // Check boundaries
    if (r < 0 || r + s > n || c < 0 || c + s > m) return false;
    
    // Check if all visible cells of this window match
    for (int i = r; i < r + s; i++) {
        for (int j = c; j < c + s; j++) {
            char cell = grid[i][j];
            if (cell == '.') {
                // Cannot place window over empty space
                if (board[i][j] == 0) return false;
            } else if (cell >= '1' && cell <= '9') {
                int visible_id = cell - '0';
                if (visible_id == window_id) {
                    // This cell must show our window
                    if (board[i][j] != 0 && board[i][j] != window_id) return false;
                } else {
                    // This cell shows another window, we can't cover it
                    if (board[i][j] == 0) {
                        // It's not covered yet, but we would cover it - invalid
                        if (window_id > visible_id) {
                            // We might be able to cover it if we're placed after
                            // But we need to check if this cell must show visible_id
                            // Actually, if grid shows visible_id, we can't cover it
                            return false;
                        }
                    }
                }
            }
        }
    }
    return true;
}

void place_window(int window_id, int r, int c, vector<vector<int>>& board) {
    for (int i = r; i < r + s; i++) {
        for (int j = c; j < c + s; j++) {
            if (board[i][j] == 0) {
                board[i][j] = window_id;
            }
        }
    }
}

// Generate all possible positions for a given window
vector<pair<int,int>> get_possible_positions(int window_id) {
    vector<pair<int,int>> pos;
    char target = '0' + window_id;
    
    // Find bounding box of all visible cells of this window
    int min_r = n, max_r = -1, min_c = m, max_c = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == target) {
                min_r = min(min_r, i);
                max_r = max(max_r, i);
                min_c = min(min_c, j);
                max_c = max(max_c, j);
            }
        }
    }
    
    // Window must cover all its visible cells
    // So top-left must be in range [max_r - s + 1, min_r] x [max_c - s + 1, min_c]
    int r_start = max(0, max_r - s + 1);
    int r_end = min(min_r, n - s);
    int c_start = max(0, max_c - s + 1);
    int c_end = min(min_c, m - s);
    
    for (int r = r_start; r <= r_end; r++) {
        for (int c = c_start; c <= c_end; c++) {
            // Quick check: does this position cover all visible cells?
            bool valid = true;
            for (int i = 0; i < n && valid; i++) {
                for (int j = 0; j < m && valid; j++) {
                    if (grid[i][j] == target) {
                        if (i < r || i >= r + s || j < c || j >= c + s) {
                            valid = false;
                        }
                    }
                }
            }
            if (valid) {
                pos.push_back({r, c});
            }
        }
    }
    return pos;
}

// Check if current configuration is valid (all visible cells match)
bool check_configuration(vector<pair<int,int>>& positions, vector<int>& order) {
    vector<vector<int>> board(n, vector<int>(m, 0));
    
    for (int idx = 0; idx < k; idx++) {
        int window_id = order[idx];
        int r = positions[window_id - 1].first;
        int c = positions[window_id - 1].second;
        
        // Place window (only on empty cells)
        for (int i = r; i < r + s; i++) {
            for (int j = c; j < c + s; j++) {
                if (board[i][j] == 0) {
                    board[i][j] = window_id;
                }
            }
        }
    }
    
    // Verify
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.') {
                if (board[i][j] != 0) return false;
            } else if (grid[i][j] >= '1' && grid[i][j] <= '9') {
                if (board[i][j] != (grid[i][j] - '0')) return false;
            }
        }
    }
    return true;
}

void count_ways(int idx, vector<int>& order, vector<pair<int,int>>& pos_choices) {
    if (idx == k) {
        if (check_configuration(pos_choices, order)) {
            result++;
        }
        return;
    }
    
    int window_id = order[idx];
    for (auto& p : positions[window_id - 1]) {
        pos_choices[window_id - 1] = p;
        count_ways(idx + 1, order, pos_choices);
    }
}

void solve() {
    cin >> n >> m >> k >> s;
    grid.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }
    
    // Get possible positions for each window
    positions.resize(k);
    for (int i = 1; i <= k; i++) {
        positions[i-1] = get_possible_positions(i);
    }
    
    result = 0;
    vector<int> order;
    for (int i = 1; i <= k; i++) order.push_back(i);
    
    // Try all permutations of window opening order
    do {
        vector<pair<int,int>> pos_choices(k);
        count_ways(0, order, pos_choices);
    } while (next_permutation(order.begin(), order.end()));
    
    cout << result << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
