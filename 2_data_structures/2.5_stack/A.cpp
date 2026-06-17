// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;

    vector<int> st;

    while (q--) {
        int t;
        cin >> t;

        if (t == 1) {
            int x;
            cin >> x;
            st.push_back(x);
            cout << st.back() << '\n';
        } else {
            st.pop_back();
            if (st.empty()) cout << "-1\n";
            else cout << st.back() << '\n';
        }
    }

    return 0;
}
