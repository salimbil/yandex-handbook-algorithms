// Компилятор: C++23 (GCC 14.1)
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAX_VAL = 200005; // Ограничение на максимальное рассматриваемое число

int main() {
    // Оптимизация ввода-вывода
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x, y;
    if (!(cin >> x >> y)) return 0;

    // Если начальное и целевое число совпадают
    if (x == y) {
        cout << 0 << "\n";
        return 0;
    }

    // Массив для хранения минимального количества шагов до каждого числа
    // -1 означает, что число еще не было посещено
    vector<int> dist(MAX_VAL, -1);
    queue<int> q;

    dist[x] = 0;
    q.push(x);

    while (!q.empty()) {
        int curr = q.front();
        q.pop();

        int d = dist[curr];

        // Перебираем все возможные цифры c от 0 до 9
        for (int c = 0; c <= 9; ++c) {
            // Вариант 1: Сложение
            long long next_add = (long long)curr + c;
            if (next_add < MAX_VAL && dist[next_add] == -1) {
                dist[next_add] = d + 1;
                if (next_add == y) {
                    cout << d + 1 << "\n";
                    return 0;
                }
                q.push(next_add);
            }

            // Вариант 2: Вычитание
            long long next_sub = (long long)curr - c;
            if (next_sub >= 0 && next_sub < MAX_VAL && dist[next_sub] == -1) {
                dist[next_sub] = d + 1;
                if (next_sub == y) {
                    cout << d + 1 << "\n";
                    return 0;
                }
                q.push(next_sub);
            }

            // Вариант 3: Умножение
            long long next_mul = (long long)curr * c;
            if (next_mul < MAX_VAL && dist[next_mul] == -1) {
                dist[next_mul] = d + 1;
                if (next_mul == y) {
                    cout << d + 1 << "\n";
                    return 0;
                }
                q.push(next_mul);
            }
        }
    }

    return 0;
}
